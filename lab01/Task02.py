from pyqtgraph import PlotWidget,mkPen
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,math

class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.windowSetting()

        self.windowObjects()
        self.windowLayout()
        self.setCentralWidget(self.centralwidget)
        

    def windowSetting(self):
        self.setWindowTitle("B19102104 Muhammad Umar Anzar")
        self.resize(800,600)
        self.center()

    def windowLayout(self):
        self.mainWindowLayout_V = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainWindowLayout_H = QtWidgets.QHBoxLayout(self.centralwidget)
        self.homeLayout_H = QtWidgets.QHBoxLayout(self.main)

        self.mainWindowLayout_V.addWidget(self.header)
        self.mainWindowLayout_V.addLayout(self.mainWindowLayout_H)
        self.mainWindowLayout_H.addWidget(self.leftGroup)
        self.mainWindowLayout_H.addWidget(self.main)
        self.mainWindowLayout_H.addWidget(self.rightContact)
        self.homeLayout_H.addWidget(self.post)
        
                
    def windowObjects(self):
        #Intialize widgets
        self.centralwidget = QtWidgets.QWidget(self)
        self.header = PlotWidget(self.centralwidget)
        self.main = PlotWidget(self.centralwidget)
        self.leftGroup = PlotWidget(self.centralwidget)
        self.rightContact = PlotWidget(self.centralwidget)

        self.post = PlotWidget(self.main)
        self.post.setMaximumSize(QtCore.QSize(500, 500))
        #Size
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.leftGroup.setMaximumSize(QtCore.QSize(200, 16777215))
        self.rightContact.setMaximumSize(QtCore.QSize(200, 16777215))

        self.plot()

    def plot(self):
        #Title name
        self.header.setTitle("Header|Sin")
        self.leftGroup.setTitle("Group|Log")
        self.rightContact.setTitle("Contact|inverse exp")
        self.main.setTitle("Home|exp")
        self.post.setTitle("Posts|Sigmoid")

        #backgroundColor
        self.header.setBackground('#e4e6eb')
        self.leftGroup.setBackground('#242526')
        self.rightContact.setBackground('#242526')
        self.main.setBackground('#242526')
        self.post.setBackground('#3a3b3c')

        #plot
        penColor = mkPen(color=(66,103,178))
        X = range(1,100)

        Y = [math.sin(i) for i in X]
        self.header.plot(X,Y,pen=penColor)

        Y = [math.exp(i) for i in X]
        self.main.plot(X,Y,pen=penColor)

        Y = [1/math.exp(i) for i in X]
        self.rightContact.plot(X,Y,pen=penColor)

        Y = [math.log(i) for i in X]
        self.leftGroup.plot(X,Y,pen=penColor)

        X = range(-50,50)
        Y = [1/(1+math.exp(-i)) for i in X]
        self.post.plot(X,Y,pen=penColor)        

    def center(self):
        #Determines the center of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        x,y = cp.x() , cp.y()
        #Center the window
        x= x - self.width()//2
        y = y - self.height()//2
        #apply new axis
        self.move(x,y)
        



app = QtWidgets.QApplication(sys.argv)
MainWindow = MyApp()


MainWindow.show()
sys.exit(app.exec_())
