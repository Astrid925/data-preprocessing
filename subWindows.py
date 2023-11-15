import os
import sys

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QMessageBox, QFileDialog, QApplication
from PySide6.QtUiTools import QUiLoader
from fileSave import FileSave

# 定义信号函数
class MySignals(QObject):
    imageInfo=Signal(tuple)
    packInfo=Signal(str,int)

Info=MySignals()  #全局实例化

exePath = os.path.dirname(sys.executable)  # 这个软件使用
# exePath = os.path.dirname(__file__)  # 这个当前测试使用
#存储文件
class saveFileWindow:
    def __init__(self):
        filePath=exePath+"//"+"saveFile.ui"
        self.saveFileUI=QUiLoader().load(filePath)
        self.saveFileUI.fileOptionBnt.clicked.connect(self.fileOption)
        self.saveFileUI.okBnt.clicked.connect(self.saveNewFile)

    def saveNewFile(self):
        if len(self.saveFileUI.fileEdit.text()) !=0:
            newFile=FileSave(self.saveFileUI.fileEdit.text(),self.saveFileUI.fileTypeBox.currentText(),self.saveFileUI.bandTypeBox.currentText(),
                             self.saveFileUI.gainBox.currentText(),self.saveFileUI.timeBox.currentText())
            newFile.saveFile()
            QMessageBox.information(self.saveFileUI,"提示","已完成文件存储")

    def fileOption(self):
        filePath=QFileDialog.getOpenFileName()
        if len(filePath[0]) !=0:
           self.saveFileUI.fileEdit.setText(filePath[0])
        else:
            QMessageBox.warning(self.saveFileUI,"警告","文件路径错误,请输入正确的文件路径")
# 数据解包
class unPackingWindow:
    def __init__(self):
        filePath = exePath + "//" + "unPacking.ui"
        self.unPackingUI=QUiLoader().load(filePath)
        self.unPackingUI.fileOptionBnt.clicked.connect(self.packOption)
        self.unPackingUI.startBnt.clicked.connect(self.packInfo)

    def packOption(self):
        filePath = QFileDialog.getOpenFileName()
        if len(filePath[0]) != 0:
            self.unPackingUI.fileEdit.setText(filePath[0])
        else:
            QMessageBox.warning(self.unPackingUI, "警告", "文件路径错误,请输入正确的文件路径")

    def packInfo(self):
        if len(self.unPackingUI.fileEdit.text()) !=0:
            Info.packInfo.emit(self.unPackingUI.fileEdit.text(),int(self.unPackingUI.packLenBox.currentText()))

# 非均匀性校正
class NUCWindow:
    def __init__(self):
        filePath = exePath + "//" + "NUC.ui"
        self.nucUI=QUiLoader().load(filePath)
        self.nucUI.fileOptionBnt.clicked.connect(self.nucFileOption)
        self.nucUI.okBnt.clicked.connect(self.fileInfo)

    def nucFileOption(self):
        filePath = QFileDialog.getOpenFileName()
        if len(filePath[0]) != 0:
            self.nucUI.fileEdit.setText(filePath[0])
        else:
            QMessageBox.warning(self.nucUI, "警告", "文件路径错误,请输入正确的文件路径")

    def fileInfo(self):
        if len(self.nucUI.fileEdit.text()) !=0:
            nucImageInfo = (self.nucUI.fileEdit.text(), self.nucUI.fileTypeBox.currentText(), self.nucUI.bandTypeBox.currentText(),
                             self.nucUI.gainBox.currentText(), self.nucUI.timeBox.currentText())
            Info.imageInfo.emit(nucImageInfo)

# 盲元补偿
class BRPWindow:
    def __init__(self):
        filePath = exePath + "//" + "BRP.ui"
        self.brpUI=QUiLoader().load( filePath)
        self.brpUI.fileOptionBnt.clicked.connect(self.brpFileOption)
        self.brpUI.okBnt.clicked.connect(self.fileInfo)

    def brpFileOption(self):
        filePath = QFileDialog.getOpenFileName()
        if len(filePath[0]) != 0:
            self.brpUI.fileEdit.setText(filePath[0])
        else:
            QMessageBox.warning(self.brpUI, "警告", "文件路径错误,请输入正确的文件路径")

    def fileInfo(self):
        if len(self.brpUI.fileEdit.text()) != 0:
            brpFileInfo=(self.brpUI.fileEdit.text(), self.brpUI.fileTypeBox.currentText(),self.brpUI.bandTypeBox.currentText(),
                         self.brpUI.gainBox.currentText(), self.brpUI.timeBox.currentText())
            Info.imageInfo.emit(brpFileInfo)



if __name__ == '__main__':
    app = QApplication([])
    window = NUCWindow()
    window.nucUI.show()
    app.exec_()