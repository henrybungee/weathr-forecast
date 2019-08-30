from PyQt5 import QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QLabel
#import MainWindow as main

class AboutWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle('About Weathr')

        self.top = 220
        self.left = 430
        self.width = 500
        self.height = 350

        self.setGeometry(self.left, self.top, self.width, self.height)

        #define version etc.:
        self.VERSION = '2.6.3'
        self.VERSION_TYPE = 'Alpha'
        self.DESCRIPTION = 'Weathr is a current weather application written in Python using the Qt 5 library and OpenWeatherMap. With this application you have the power to see the current weather, as well as change your location and metric conversions.'

        self.labelTitle = QLabel(self)
        self.labelTitle.move(197, 20)
        self.labelTitle.setText("<h3>About Weathr</h3>")
        self.labelTitle.setStyleSheet('font-weight:bold;')

        self.versionInfo = QLabel(self)
        self.versionInfo.move(15, 75)
        self.versionInfo.setText('Version ' +self.VERSION)

        self.stable = QLabel(self)
        self.stable.setText(self.VERSION_TYPE)
        self.stable.move(15, 95)

        self.creatorName = QLabel(self)
        self.creatorName.setText('Created by Henry Lunger')
        self.creatorName.move(15, 115)

        self.emailMe = QLabel(self)
        self.emailMe.setWordWrap(True)
        self.emailMe.setText(self.DESCRIPTION)
        self.emailMe.move(15, 155)

        self.legalNote = QLabel(self)
        self.legalNote.setText('Powered by OpenWeatherMap\nCopyright© Henry Lunger 2019 CE')
        self.legalNote.move(15, 300)
        self.legalNote.setStyleSheet('color: grey;')