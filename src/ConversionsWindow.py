from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QPushButton, QLabel, QMessageBox, QRadioButton, QLineEdit
import MainWindow as main

class ConversionsWindow(QtWidgets.QDialog):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Preferences — Weathr')

        self.top = 200
        self.left = 350
        self.width = 600
        self.height = 430
        self.mainWindow = mainWindow

        self.setGeometry(self.left, self.top, self.width, self.height)

        self.labelTitle = QLabel(self)
        self.labelTitle.move(197, 20)
        self.labelTitle.setText("<h3>Weather Preferences</h3>")
        self.labelTitle.setStyleSheet('font-weight:bold;')

        #THE TEMPERATURE GROUP BOX

        #create the groupbox
        self.temperatureGroupbox = QGroupBox('Temperature Units', self)
        self.temperatureGroupbox.move(15, 50)

        #create the temperature radio buttons
        self.cRadioTemp = QRadioButton("Celsius (Metric System)", self)
        self.fRadioTemp = QRadioButton("Fahrenheit (Imperial System)", self)
        self.kRadioTemp = QRadioButton("Kelvin (Standard International Unit)", self)

        self.cRadioTemp.setChecked(True)
        if self.cRadioTemp.isChecked():
            self.unitChoice = 'C'

        #create the temp vbox
        self.vboxTemp = QVBoxLayout(self)
        self.vboxTemp.addWidget(self.cRadioTemp)
        self.vboxTemp.addWidget(self.fRadioTemp)
        self.vboxTemp.addWidget(self.kRadioTemp)
        self.vboxTemp.addStretch(1)

        #add items to the temp vbox
        self.temperatureGroupbox.setLayout(self.vboxTemp)

        #check the correct radio button
        if self.mainWindow.unitChoice == 'C':
            self.cRadioTemp.setChecked(True)
        elif self.mainWindow.unitChoice == 'F':
            self.fRadioTemp.setChecked(True)
        elif self.mainWindow.unitChoice == 'K':
            self.kRadioTemp.setChecked(True)

        #THE SPEED GROUP BOX

        #create the speed groupbox
        self.speedGroupbox = QGroupBox('Speed Units', self)
        self.speedGroupbox.move(15, 200)

        #create the radio buttons for groupbox
        self.kphRadio = QRadioButton('Kilometers Per Hour (Metric System)', self)
        self.mphRadio = QRadioButton('Miles Per Hour (Imperial System)', self)

        self.kphRadio.setChecked(True)

        #create the speed vbox
        self.speedVbox = QVBoxLayout(self)
        self.speedVbox.addWidget(self.kphRadio)
        self.speedVbox.addWidget(self.mphRadio)

        #add items to the groupbox
        self.speedGroupbox.setLayout(self.speedVbox)

        # check the correct speed radio button
        if self.mainWindow.speedUnitChoice == 'KPH':
            self.kphRadio.setChecked(True)
        elif self.mainWindow.speedUnitChoice == 'MPH':
            self.mphRadio.setChecked(True)

        self.saveBtn = QPushButton(self)
        self.saveBtn.setText('Save Preferences')
        self.saveBtn.move(15, 390)
        self.saveBtn.clicked.connect(self.checkRadioButtons)
        self.saveBtn.clicked.connect(self.reloadWeather)

        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setText('Cancel')
        self.cancelBtn.move(485 ,390)
        self.cancelBtn.clicked.connect(self.reloadWeather)

    def reloadWeather(self):
        self.mainGetWeather = main.Window()
        self.mainGetWeather.getWeather()
        self.close()

    def checkRadioButtons(self):

        f = open('src/saves/speed.txt', 'r+')
        f.truncate(0)

        ftemp = open('src/saves/temp.txt', 'r+')
        ftemp.truncate(0)

        #save data
        if self.kphRadio.isChecked():
            with open("src/saves/speed.txt", "w") as f:
                f.write("KPH")
            self.mainWindow.speedUnitChoice = 'KPH'
        elif self.mphRadio.isChecked():
            with open("src/saves/speed.txt", "w") as f:
                f.write("MPH")
            self.mainWindow.speedUnitChoice = 'MPH'

        #save temperature unit data
        if self.cRadioTemp.isChecked():
            print("Celsius")
            with open("src/saves/temp.txt", "w") as f:
                f.write('C')
            self.mainWindow.unitChoice = 'C'
        elif self.fRadioTemp.isChecked():
            print("Fahrenheit")
            with open("src/saves/temp.txt", "w") as f:
                f.write('F')
            self.mainWindow.unitChoice = 'F'
        elif self.kRadioTemp.isChecked():
            print("Kelvin")
            with open("src/saves/temp.txt", "w") as f:
                f.write('K')
            self.mainWindow.unitChoice = 'K'

        #deals with speed XD
        if self.kphRadio.isChecked():
            print("KPH")
            self.mainWindow.speedUnitChoice = 'KPH'

        elif self.mphRadio.isChecked():
            print("MPH")
            self.mainWindow.speedUnitChoice = 'MPH'