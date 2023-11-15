# -*- coding: utf-8 -*-
# import resource
from PySide6.QtCore import Slot, QPoint
from PySide6.QtGui import QImage, QPainter, Qt, QPixmap, QFont
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtUiTools import QUiLoader
from dataTransformation import packImg
from nonuniformityCorrection import nucImg
from blindPixelRemoval import brpImg
from subWindows import saveFileWindow,unPackingWindow,NUCWindow,BRPWindow,Info
from nucWorker import NUCWorker
from brpWorker import BRPWorker
from unPackingWorker import packWorker
from mainWindow import Ui_MainWindow


class mainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        self.setupUi(self)
        # connect signal and slot
        self.actSaveFile.triggered.connect(self.open_saveFileUI)
        self.actUnpacking.triggered.connect(self.open_unPackingUI)
        self.actNUC.triggered.connect(self.open_nucUI)
        self.actBPR.triggered.connect(self.open_brpUI)
        # subwindows
        self.fileGUI=saveFileWindow()
        self.packGUI = unPackingWindow()
        self.nucGUI = NUCWindow()
        self.brpGUI=BRPWindow()
        # multi-Thread
        self.nucThread=NUCWorker()
        self.brpThread=BRPWorker()
        self.packThread=packWorker()
        # connect signal and slot
        packImg.QtImage.connect(self.getOneImage)
        packImg.finishedInfo.connect(self.packFinished)
        packImg.nFrameStr.connect(self.nFrameGet)

        nucImg.QtImage.connect(self.getOneImage)
        nucImg.finishedInfo.connect(self.nucFinished)
        nucImg.nFrameStr.connect(self.nFrameGet)

        brpImg.QtImage.connect(self.getOneImage)
        brpImg.finishedInfo.connect(self.brpFinished)
        brpImg.nFrameStr.connect(self.nFrameGet)
        # 初始化一个 QImage 全局变量
        self.QtImg=QImage(1024,1024,QImage.Format.Format_ARGB32_Premultiplied)
        self.nFrame=""
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(QFont("Microsoft YaHei UI",10,QFont.Bold))

    def paintEvent(self,event):
        painter = QPainter(self)
        img=self.QtImg.scaled(self.imageLabel.size(), Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        x=self.imageLabel.geometry().x()
        y=self.imageLabel.geometry().y()
        painter.drawImage(QPoint(x,y),img)

    @Slot(QImage)
    def getOneImage(self,QtImage):
        self.QtImg = QtImage
        self.update()

    @Slot(str)
    def nFrameGet(self, frameStr):
        self.nFrame = frameStr
        self.titleLabel.setText(self.nFrame)

    # 文件存储
    def open_saveFileUI(self):
        self.fileGUI.saveFileUI.show()


    # 数据解包
    def open_unPackingUI(self):
        self.packGUI.unPackingUI.show()
        Info.packInfo.connect(self.packInfoGet)

    @Slot(str,int)
    def packInfoGet(self,fileStr,packLen):
        self.packThread.init(fileStr,packLen)

    @Slot(str)
    def packFinished(self, Info):
        QMessageBox.information(self, "提示", Info)

    # 非均匀性校正
    def open_nucUI(self):
        self.nucGUI.nucUI.show()
        Info.imageInfo.connect(self.nucImageInfoGet)

    @Slot(tuple)
    def nucImageInfoGet(self,Info):
        self.nucThread.init(Info[0],Info[1],Info[2],Info[3],Info[4])

    @Slot(str)
    def nucFinished(self, Info):
        QMessageBox.information(self, "提示", Info)

    # 盲元补偿
    def open_brpUI(self):
        self.brpGUI.brpUI.show()
        Info.imageInfo.connect(self.brpImageInfoGet)

    @Slot(tuple)
    def brpImageInfoGet(self,Info):
       self.brpThread.init(Info[0], Info[1],Info[2],Info[3], Info[4])

    @Slot(str)
    def brpFinished(self, Info):
        QMessageBox.information(self, "提示", Info)

if __name__ == '__main__':
    app = QApplication([])
    window = mainWindow()
    window.show()
    app.exec_()