import os
import sys
import scipy
import numpy as np
import matplotlib.image as img
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QImage


class NUC():
    def __init__(self,inputFile,fileType,bandType,gainNum,timeNum):
        self.inputFile = inputFile
        self.fileType = fileType
        self.bandType = bandType
        self.gainNum = gainNum
        self.timeNum = timeNum
        self.fileEnd=False
        self.threadClose=False
        self.nFrame=0

    def openFile(self):
        (file, ext) = os.path.splitext(self.inputFile)
        (Path, filename) = os.path.split(file)
        filePath = os.path.dirname(Path)
        saveFilePath = filePath + "\\" + "nonuniformityCorrection_result"
        if not os.path.exists(saveFilePath):
            os.mkdir(saveFilePath)  # 创建一个文件夹
        saveFileName = "NUC_" + filename + ".raw"
        saveHeadName="NUC_" + filename + ".hdr"
        savePath = os.path.join(saveFilePath, saveFileName)  # 存储的文件路径
        saveHeadPath=os.path.join(saveFilePath, saveHeadName)
        self.saveFile = open(savePath, mode='wb')
        self.saveHeadFile = open(saveHeadPath, mode='w', encoding='utf-8')
        if not os.path.exists(saveFilePath + "\\" + "RImage"):
            os.mkdir(saveFilePath+ "\\" + "RImage")
        self.RPath = saveFilePath + "\\" + "RImage"
        if not os.path.exists(saveFilePath + "\\" + "GImage"):
            os.mkdir(saveFilePath + "\\" + "GImage")
        self.GPath = saveFilePath + "\\" + "GImage"
        if not os.path.exists(saveFilePath + "\\" + "BImage"):
            os.mkdir(saveFilePath + "\\" + "BImage")
        self.BPath = saveFilePath + "\\" + "BImage"

    def closeFile(self):
        if self.nFrame!=0:
            text = "ENVI\n" + "samples = 1030\n" + "lines=1024\n" + "bands =" + str(self.nFrame) + "\n" + "header offset = 0\n" + "file type = ENVI Standard\n" + "data type = 4\n" + "interleave = bsq\n" + "byte order = 0"
            self.saveHeadFile.write(text)
            self.saveFile.close()
            self.saveHeadFile.close()
            nucImg.finishedInfo.emit("已完成非均匀性校正")
        else:
            self.threadClose = True

    def imageSave(self,image,outCount):
        if self.bandType=="Blue":
            BWritePath = os.path.join(self.BPath, "第" + str(outCount + 1) + "帧B图.png")
            img.imsave(BWritePath, image, cmap="gray")
        elif self.bandType=="Green":
            GWritePath = os.path.join(self.GPath, "第" + str(outCount + 1) + "帧G图.png")
            img.imsave(GWritePath, image, cmap="gray")
        else:
            RWritePath = os.path.join(self.RPath, "第" + str(outCount + 1) + "帧R图.png")
            img.imsave(RWritePath, image, cmap="gray")

    def grayProcess(self,gray, truncated_value=2, maxout=255, minout=0):  # Linear2% 线性拉伸
        low_value = np.percentile(gray, truncated_value)
        high_value = np.percentile(gray, 100 - truncated_value)
        truncated_gray = np.clip(gray, low_value, high_value)
        processed_gray = ((truncated_gray - low_value) / (high_value - low_value)) * (maxout - minout)
        return processed_gray

    def imageNuc(self):
        # 获取对应的非均匀性校正参数
        exePath = os.path.dirname(sys.executable)  # 这个软件使用
        # exePath = os.path.dirname(__file__)  # 这个当前测试使用
        nucFilePath = exePath + "\\" + "matrix"
        nucFileName=self.fileType + "_" + self.bandType + "_" + self.gainNum + "_" + self.timeNum + ".mat"
        nucFile=os.path.join(nucFilePath,nucFileName)
        # 进行非均匀性校正
        if os.path.exists(nucFile):
            nucData=scipy.io.loadmat(nucFile)
            K=np.transpose(nucData["K_XY"])
            B=np.transpose(nucData["B_XY"])
            inputPath=open(self.inputFile, mode="rb")
            fileSize = os.path.getsize(self.inputFile)
            bitNum = B.shape[0] * (B.shape[1] + 6) * 2
            self.nFrame=int(fileSize/ bitNum)
            for i in range(self.nFrame):
                inputData=np.frombuffer(inputPath.read(bitNum), dtype=">u2").reshape(B.shape[0],B.shape[1]+6)  # 数据大小端问题
                usedData=inputData[:,5:-1]
                usedData=K*usedData+B
                self.imageSave(usedData,i)
                outData=np.hstack((inputData[:,0:5],usedData))
                outData=np.column_stack((outData,inputData[:,-1]))
                self.saveFile.write(outData.astype('<f'))

                grayImg=(self.grayProcess(usedData,2, 255, 0)).astype(np.uint8)
                QtImg=QImage(grayImg.data,grayImg.shape[1],grayImg.shape[0],grayImg.shape[1], QImage.Format.Format_Indexed8)
                nucImg.QtImage.emit(QtImg)
                nucImg.nFrameStr.emit("第"+str(i+1)+"帧图像")
            self.fileEnd=True
        else:
            nucImg.finishedInfo.emit("没有找到非均匀性校正系数文件，请存储相关文件")
            self.threadClose=True


class imageSignals(QObject):
    QtImage=Signal(QImage)
    finishedInfo=Signal(str)
    nFrameStr=Signal(str)

nucImg=imageSignals()

if __name__=="__main__":
    fileType = "NonuniformityCorrection"
    bandType = "Blue"
    gainNum = "1x"
    timeNum = "60ms"
    inputFile=r"D:\cxy\研究\小行星探测项目\小行星数据预处理\1x增益\1x增益\拍摄图像\60ms\Result_60_img\Blue_Band.raw"
    myTest=NUC(inputFile,fileType,bandType,gainNum,timeNum)
    myTest.openFile()
    myTest.imageNuc()
    myTest.closeFile()