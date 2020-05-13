from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QRadioButton
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
label2 = QRadioButton("check")
button = QPushButton("Ceci est un QPushButton")
button2 = QPushButton("push")


layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(button)
layout.addWidget(button2)


mainWidget.setLayout(layout)


mainWidget.show()
app.exec_()
