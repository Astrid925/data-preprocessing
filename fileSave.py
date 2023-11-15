import os
import sys
import scipy


class FileSave():
    def __init__(self,inputFile,fileType,bandType,gainNum,timeNum):
        self.inputFile=inputFile
        self.fileType=fileType
        self.bandType=bandType
        self.gainNum=gainNum
        self.timeNum=timeNum

    def saveFile(self):
        filePath = os.path.dirname(sys.executable) #这个软件使用
        # filePath = os.path.dirname(__file__)  # 这个当前测试使用
        saveFilePath=filePath+"\\"+"matrix"
        if not os.path.exists(saveFilePath):
            os.mkdir(saveFilePath)      #创建一个文件夹
        matData=scipy.io.loadmat(self.inputFile)
        saveFileName = self.fileType + "_" + self.bandType + "_" + self.gainNum + "_" + self.timeNum + ".mat"
        savePath = os.path.join(saveFilePath, saveFileName)
        scipy.io.savemat(savePath,matData)  #覆盖存储


if __name__=="__main__":
    #fileType="blindPixelRemoval"
    fileType="nonuniformityCorrection"
    bandType="blueBand"
    gainNum="60ms"
    timeNum="1x"
    inputFile=r"D:\cxy\研究\小行星探测项目\小行星数据预处理\1x增益\1x增益\60ms\Blue_Band_KB_XY_60ms.mat"
    myTest=FileSave(inputFile,fileType,bandType,gainNum,timeNum)
    myTest.saveFile()