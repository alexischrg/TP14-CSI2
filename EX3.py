from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("France")

        self.icon = QIcon("fr-flag.png")
        self.setWindowIcon(self.icon)

        self.layout = QVBoxLayout()

        self.label = QLabel("Hello World")
        self.label.setAlignment(Qt.AlignCenter)
        self.progrBar = QProgressBar()
        self.progrBar.setValue(99)
        self.lineEdit = QLineEdit()
        self.button = QPushButton("Click me !")
        self.button.setToolTip("1% restant")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progrBar)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()