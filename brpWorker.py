from PySide6.QtCore import QThread
from blindPixelRemoval import BlindPixelRemoval

class BRPWorker(QThread):
     def __init__(self,parent=None):
         super(BRPWorker, self).__init__(parent)

     def init(self,inputFile,fileType,bandType,gainNum,timeNum):
         self.inputFile = inputFile
         self.fileType = fileType
         self.bandType = bandType
         self.gainNum = gainNum
         self.timeNum = timeNum
         if not self.isRunning():
             self.start()

     def run(self):
         brpImage = BlindPixelRemoval(self.inputFile, self.fileType, self.bandType, self.gainNum,  self.timeNum)
         brpImage.openFile()
         while (brpImage.fileEnd==False):
            brpImage.blindPixelRemoval()
            if brpImage.threadClose==True:
                break
         brpImage.closeFile()
         self.quit()


