import os
import sys
import matplotlib.image as img
import scipy
import numpy as np
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QImage


class BlindPixelRemoval():
    def __init__(self,inputFile,fileType,bandType,gainNum,timeNum):
        self.inputFile = inputFile
        self.fileType = fileType
        self.bandType = bandType
        self.gainNum = gainNum
        self.timeNum = timeNum
        self.fileEnd = False
        self.threadClose=False
        self.nFrame=0

    def openFile(self):
        (file, ext) = os.path.splitext(self.inputFile)
        (Path, filename) = os.path.split(file)
        filePath = os.path.dirname(Path)
        saveFilePath = filePath + "\\" + "blindPixelRemoval_result"
        if not os.path.exists(saveFilePath):
            os.mkdir(saveFilePath)  # 创建一个文件夹
        saveFileName = "BPR_" + filename + ".raw"
        saveHeadName = "BPR_" + filename + ".hdr"
        savePath = os.path.join(saveFilePath, saveFileName)  # 存储的文件路径
        saveHeadPath = os.path.join(saveFilePath, saveHeadName)
        self.saveFile = open(savePath, mode='wb')
        self.saveHeadFile = open(saveHeadPath, mode='w', encoding='utf-8')
        if not os.path.exists(saveFilePath + "\\" + "RImage"):
            os.mkdir(saveFilePath + "\\" + "RImage")
        self.RPath = saveFilePath + "\\" + "RImage"
        if not os.path.exists(saveFilePath + "\\" + "GImage"):
            os.mkdir(saveFilePath + "\\" + "GImage")
        self.GPath = saveFilePath + "\\" + "GImage"
        if not os.path.exists(saveFilePath + "\\" + "BImage"):
            os.mkdir(saveFilePath + "\\" + "BImage")
        self.BPath = saveFilePath + "\\" + "BImage"

    def closeFile(self):
        if self.nFrame != 0:
            text = "ENVI\n" + "samples = 1030\n" + "lines=1024\n" + "bands =" + str(self.nFrame) + "\n" + "header offset = 0\n" + "file type = ENVI Standard\n" + "data type = 4\n" + "interleave = bsq\n" + "byte order = 0"
            self.saveHeadFile.write(text)
            self.saveFile.close()
            self.saveHeadFile.close()
        else:
            self.threadClose=True
    def imageSave(self, image, outCount):
        if self.bandType == "Blue":
            BWritePath = os.path.join(self.BPath, "第" + str(outCount + 1) + "帧B图.png")
            img.imsave(BWritePath, image, cmap="gray")
        elif self.bandType == "Green":
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

    def blindPixelRemoval(self):
        # 获取对应的盲元标记文件
        exePath = os.path.dirname(sys.executable)  # 这个软件使用
        # exePath = os.path.dirname(__file__)  # 这个当前测试使用
        flagFilePath = exePath + "\\" + "matrix"
        flagFileName = self.fileType + "_" + self.bandType + "_" + self.gainNum + "_" + self.timeNum + ".mat"
        flagFile = os.path.join(flagFilePath, flagFileName)
        # 进行非均匀性校正
        if os.path.exists(flagFile):
            nucData = scipy.io.loadmat(flagFile)
            flag = np.transpose(nucData["FlagDH"])
            inputPath = open(self.inputFile, mode="rb+")
            fileSize = os.path.getsize(self.inputFile)
            bitNum = flag.shape[0] * (flag.shape[1] + 6) * 4
            self.nFrame = int(fileSize / bitNum)
            for i in range(self.nFrame):
                inputData = np.array(np.frombuffer(inputPath.read(bitNum), dtype="<f").reshape(flag.shape[0], flag.shape[1] + 6)) # 数据大小端问题
                inputData.flags.writeable = True   # 开启可写模式
                usedData = inputData[:, 5:-1]
                tempData=np.pad(usedData,(1,1),"constant") #考虑在边缘区域的盲元，这里用
                pos=np.argwhere(flag==1)
                usedData[pos[:, 0], pos[:, 1]]=(tempData[pos[:,0],pos[:,1]+1]+tempData[pos[:,0]+2,pos[:,1]+1]+tempData[pos[:,0]+1,pos[:,1]]+tempData[pos[:,0]+1,pos[:,1]+2])/4
                self.imageSave(usedData, i)
                outData = np.hstack((inputData[:, 0:5], usedData))
                outData = np.column_stack((outData, inputData[:, -1]))
                self.saveFile.write(outData.astype('<f'))
                grayImg = (self.grayProcess(usedData, 2, 255, 0)).astype(np.uint8)
                QtImg = QImage(grayImg.data, grayImg.shape[1], grayImg.shape[0], grayImg.shape[1],QImage.Format_Indexed8)
                brpImg.QtImage.emit(QtImg)
                brpImg.nFrameStr.emit("第" + str(i + 1) + "帧图像")
            self.fileEnd = True
            brpImg.finishedInfo.emit("已完成盲元补偿")
        else:
            brpImg.finishedInfo.emit("没有找到盲元定位文件，请存储相关文件")
            self.threadClose=True

class imageSignals(QObject):
    QtImage=Signal(QImage)
    finishedInfo=Signal(str)
    nFrameStr = Signal(str)

brpImg=imageSignals()

if __name__=="__main__":
    fileType="blindPixelRemoval"
    # fileType="nonuniformityCorrection"
    bandType="blueBand"
    gainNum="60ms"
    timeNum="1x"
    inputFile=r"D:\cxy\研究\小行星探测项目\小行星数据预处理\1x增益\1x增益\拍摄图像\60ms\nonuniformityCorrection_result\NUC_Blue_Band.raw"
    myTest=BlindPixelRemoval(inputFile,fileType,bandType,gainNum,timeNum)
    myTest.openFile()
    myTest.blindPixelRemoval()
    myTest.closeFile()