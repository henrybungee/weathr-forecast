from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox, QRadioButton, QLineEdit, QCheckBox

class NoInternetWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Internet, Please?')
        self.top = 200
        self.left = 350
        self.width = 500
        self.height = 400
        #self.mainWindow = mainWindow
        self.cityName = ''

        self.InitUI()
        self.setGeometry(self.left, self.top, self.width, self.height)

    def InitUI(self):
        self.label = QLabel(self)
        self.label.setText('<h3>No Internet!</h3>')
        self.label.move(200, 20)

        self.noInternetImage = QPixmap('Images/nointernet.png')
        self.imageLabel = QLabel(self)
        self.imageLabel.setPixmap(self.noInternetImage)
        self.imageLabel.move(180, 80)
        self.explainationLabel = QLabel(self)
        self.explainationLabel.setWordWrap(True)
        self.explainationLabel.setText('Your Internet is down. Please try reconnecting to the internet.')
        self.explainationLabel.resize(300, 60)
        self.explainationLabel.move(110, 200)

        #create the close button
        self.closeBtn = QPushButton(self)
        self.closeBtn.setText('Close')
        self.closeBtn.move(15, 360)
        self.closeBtn.setStyleSheet('background-color: #2a42f7;')
        self.closeBtn.clicked.connect(self.close)