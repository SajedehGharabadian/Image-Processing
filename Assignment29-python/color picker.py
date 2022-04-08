import cv2
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class ColorPicker(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()

        
        self.ui.hslider_R.valueChanged.connect(self.setValue_R)
        self.ui.hslider_G.valueChanged.connect(self.setValue_G)
        self.ui.hslider_B.valueChanged.connect(self.setValue_B)


        
    def setValue_R(self, value):    
        self.ui.line_R.setText(str(value))
        self.value_R = int(self.ui.line_R.text())
        self.value_G = int(self.ui.line_G.text())
        self.value_B = int(self.ui.line_B.text())

        if self.value_R == 255 and self.value_G == 255 and self.value_B == 255:
            self.ui.textEdit.setStyleSheet(f"background-color: rgb({self.value_R},{self.value_G},{self.value_B}); color:black")
            self.ui.textEdit.setPlainText(f"rgb( {self.value_R},{self.value_G},{self.value_B})")

        else:
            self.ui.textEdit.setStyleSheet(f"background-color: rgb({self.value_R},{self.value_G},{self.value_B}); color:white")
            self.ui.textEdit.setPlainText(f"rgb( {self.value_R},{self.value_G},{self.value_B})")


    
    def setValue_G(self, value):    
        self.ui.line_G.setText(str(value))
        self.value_R = int(self.ui.line_R.text())
        self.value_G = int(self.ui.line_G.text())
        self.value_B = int(self.ui.line_B.text())
        
        if self.value_R == 255 and self.value_G == 255 and self.value_B == 255:
            self.ui.textEdit.setStyleSheet(f"background-color: rgb({self.value_R},{self.value_G},{self.value_B}); color:black")
            self.ui.textEdit.setPlainText(f"rgb( {self.value_R},{self.value_G},{self.value_B})")

        else:
            self.ui.textEdit.setStyleSheet(f"background-color: rgb({self.value_R},{self.value_G},{self.value_B}); color:white")
            self.ui.textEdit.setPlainText(f"rgb( {self.value_R},{self.value_G},{self.value_B})")


        
    def setValue_B(self, value):    
        self.ui.line_B.setText(str(value))
        self.value_R = int(self.ui.line_R.text())
        self.value_G = int(self.ui.line_G.text())
        self.value_B = int(self.ui.line_B.text())
        if self.value_R == 255 and self.value_G == 255 and self.value_B == 255:
            self.ui.textEdit.setStyleSheet(f"background-color: rgb({self.value_R},{self.value_G},{self.value_B}); color:black")
            self.ui.textEdit.setPlainText(f"rgb( {self.value_R},{self.value_G},{self.value_B})")

        else:
            self.ui.textEdit.setStyleSheet(f"background-color: rgb({self.value_R},{self.value_G},{self.value_B}); color:white")
            self.ui.textEdit.setPlainText(f"rgb( {self.value_R},{self.value_G},{self.value_B})")

            







app = QApplication([])

window = ColorPicker()

app.exec()

