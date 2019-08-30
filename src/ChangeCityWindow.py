from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox, QRadioButton, QLineEdit, QCheckBox

import MainWindow as main
import geocoder

class ChangeCityWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Change The City — Weathr')
        self.top = 200
        self.left = 350
        self.width = 400
        self.height = 400
        self.cityName = ''

        self.InitUI()
        self.setWindowIcon(QIcon('Images/weather.ico'))
        self.setGeometry(self.left, self.top, self.width, self.height)


    def InitUI(self):

        #create a styled header
        self.header = QLabel(self)
        self.header.setText('<h3>Change the City</h3>')
        self.header.move(130, 10)

        #create the form and the explination label
        self.cityLabel = QLabel(self)
        self.cityLabel.setText('Change the City:')
        self.cityLabel.move(15, 30)

        #create input field
        self.cityInputField = QLineEdit(self)
        self.cityInputField.resize(180, 32)
        self.cityInputField.move(15, 55)
        self.cityInputField.setPlaceholderText('Enter a City...')

        #create header for settings
        self.headerSettings = QLabel(self)
        self.headerSettings.setText('<h4>Location Settings</h4>')
        self.headerSettings.move(15, 100)

        #create settings for the location settings
        self.locationLabel = QLabel(self)
        self.locationLabel.setText('NOTE: Location tracking is dependent on the internet and the IP. Note that the IP might not contain an accurate location. Also, if this is checked, whatever you put into the text field above will be ignored.')
        self.locationLabel.setWordWrap(True)
        self.locationLabel.move(15, 130)

        self.turnOnLocationTracking = QCheckBox(self)
        self.turnOnLocationTracking.setText('Track location instead')
        self.turnOnLocationTracking.move(15, 220)
        self.turnOnLocationTracking.stateChanged.connect(self.getLocation)
        self.turnOnLocationTracking.stateChanged.connect(self.cityInputField.setDisabled)

        self.coordinatesLabel = QLabel(self)
        self.coordinatesLabel.move(15, 245)
        self.coordinatesLabel.setText('<h4>Your Location will Be Displayed Here</h4>')
        self.coordinatesLabel.resize(600, 30)

        #create the save btn
        self.saveBtn = QPushButton(self)
        self.saveBtn.setText('Save Preferences')
        self.saveBtn.move(15, 360)
        self.saveBtn.clicked.connect(self.saveFunction)

        #create the cancel Btn
        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setText('Cancel')
        self.cancelBtn.move(300, 360)
        self.cancelBtn.clicked.connect(self.cancel)


    def getLocation(self):

        self.g = geocoder.ip('me')
        print(self.g.latlng)
        self.coordinatesLabel.setText('<h4>Your Location Is In ' +str(self.g.state)+ ', ' +str(self.g.city)+ '</h4>')


    def saveFunction(self):

        #self.reloadWeather()
        #self.close()

        #check "weather" or not (hahaha get it? weather?) the location button is checked
        if self.turnOnLocationTracking.isChecked():

            #write to the text file
            with open('src/saves/startupcity.txt', 'w') as f:
                f.write(self.g.city)

            self.reloadWeather()
            self.close()
            
        #run if location tracking isn't checked.
        elif self.turnOnLocationTracking.isChecked() != True:

            if self.cityInputField.text() == '' or self.cityInputField.text() == ' ':
                self.dlg = QMessageBox.critical(self, 'Blank Form', 'Fill in the form. The form cannont be blank',
                                                QMessageBox.Ok)
                self.cancelBtn.setDisabled(True)
                self.mainGetWeather.close()
                self.show()

            else:
                #write to text file
                # write to the text file
                with open('src/saves/startupcity.txt', 'w') as f:
                    f.write(self.cityInputField.text())

                self.reloadWeather()
                self.close()
    def reloadWeather(self):

        self.mainGetWeather = main.Window()
        self.mainGetWeather.getWeather()
        self.close()

    def cancel(self):
        self.mainGetWeather = main.Window()
        self.close()
        self.mainGetWeather.show()