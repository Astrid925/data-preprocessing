from PySide6.QtCore import QThread
from nonuniformityCorrection import NUC

class NUCWorker(QThread):
     def __init__(self,parent=None):
         super(NUCWorker, self).__init__(parent)

     def init(self,inputFile,fileType,bandType,gainNum,timeNum):
         self.inputFile = inputFile
         self.fileType = fileType
         self.bandType = bandType
         self.gainNum = gainNum
         self.timeNum = timeNum
         if not self.isRunning():
             self.start()

     def run(self):
         nucImage = NUC(self.inputFile, self.fileType, self.bandType, self.gainNum,  self.timeNum)
         nucImage.openFile()
         while (nucImage.fileEnd==False):
            nucImage.imageNuc()
            if nucImage.threadClose==True:
                break
         nucImage.closeFile()
         self.quit()


