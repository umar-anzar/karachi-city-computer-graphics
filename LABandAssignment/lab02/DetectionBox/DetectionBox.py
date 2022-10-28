from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
from PIL import Image
import numpy as np

class Ui(QtWidgets.QMainWindow):

    # Constructor
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__() 

        # Load the .ui file
        uic.loadUi('basic.ui', self) 

        # Show the GUI
        self.show() 

        # Allow user to drop file
        self.setAcceptDrops(True)

        # Button function
        self.btn_convert.clicked.connect(self.convert)
        self.bool_convert = False


    # Coordinate class
    class Coordinate:
        def __init__(self,x,y):
            self.x = x
            self.y = y

    # Events
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            self.file_path = event.mimeData().urls()[0]#only select first file
            self.file_path = self.file_path.toLocalFile()
            
            # Show Image
            self.setImage(self.file_path)

            self.bool_convert = True
            event.accept()
        else:
            event.ignore()

    def setImage(self,file_path):
        self.label_photo.setPixmap(QPixmap(file_path))
        
    def convert(self):
        # If image is load
        if self.bool_convert:
            
            # Load Image from file path and convert into numpy array
            with Image.open(self.file_path) as im:
                im = im.convert('1')
                arr = np.array(im)

            # Two List of Black spot to save row and columns     
            black_arr_x = []
            black_arr_y = []
            for i in range(len(arr)): # y axis row
                for j in range(len(arr[i])): # x axis column
                    if arr[i][j]==False:
                        black_arr_y.append(i)
                        black_arr_x.append(j)
            
            # Calculating Max and Min x corners
            max_x, max_y = max(black_arr_x), max(black_arr_y)
            min_x, min_y = min(black_arr_x), min(black_arr_y)


            # Corner Points
            '''
            D-------------C
            |             |
            |             |
            |             |
            |             |
            A-------------B
            '''
            
            # Four Coordinate of Rectangle
            A = self.Coordinate(min_x, max_y)#left bottom
            B = self.Coordinate(max_x, max_y)#right bottom
            C = self.Coordinate(max_x, min_y)#right top
            D = self.Coordinate(min_x, min_y)#left top

            # Draw Two Horizontal Line
            for i in range(A.x,B.x):
                #arr[row][column]
                arr[A.y][i] = False
                arr[D.y][i] = False

            # Draw Two Vertical Line
            for i in range(D.y,A.y):
                arr[i][A.x] = False
                arr[i][C.x] = False


            # Saving Detected Image
            name = self.file_path.split('.')
            file_path = name[0]+'detected.'+name[1]
            image = Image.fromarray(arr)
            image.save(file_path)

            # Showing Detected Image
            self.setImage(file_path)
            
            self.bool_convert = False

        else:
            pass

        

# Execute GUI
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
