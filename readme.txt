文档中的文件主要分为3类：实现功能的文件、线程文件、ui设计文件

1. 实现功能的文件

dataTransformation.py  实现数据解包，生成图像的功能
fileSave.py 是将非均匀性校正系数、盲元位置矩阵数据，按照特定格式存储到软件运行目录（具体格式可以参考软件使用说明）
nonuniformityCorrection.py 是实现图像非均匀性校正功能
blindPixelRemoval.py 是实现盲元补偿（盲元剔除）功能

2. 线程文件

unPackingWorker.py  解包功能的线程
nucWorker.py   非均匀性校正的线程
brpWorker.py  盲元剔除的线程

3. ui设计相关文件
ui使用ui Designer设计完成，存储于该目录的“uiFile”文件; 
主界面的 mainWindow.ui 文件被转换成mainWindow.py 文件；
subWindows.py 主要用于加载子界面文件，unPacking.ui \ saveFile.ui \ NUC.ui\BRP.ui

4. GUI.py
该文件是软件最终的UI界面、信号与槽函数、画图事件等的配置


