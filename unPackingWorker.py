from PySide6.QtCore import QThread
from dataTransformation import DataConcat

class packWorker(QThread):
     def __init__(self,parent=None):
         super(packWorker, self).__init__(parent)

     def init(self,inputFile,pkLen):
         self.inputFile = inputFile
         self.pkLen = pkLen
         if not self.isRunning():
             self.start()

     def run(self):
         packImage = DataConcat(self.inputFile,self.pkLen)
         packImage.openFile()
         while (packImage.fileEnd==False):
            packImage.dataProcess()
         packImage.closeFile()
         self.quit()


