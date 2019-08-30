#!/usr/bin/env python3

#Under the publications of henry the dude
#thats right, you heard me right
#i have no idea what to say but it looks
#proffesional. Cool.

import sys
import requests
import datetime

import AboutWindow as about
import ConversionsWindow as units
import ChangeCityWindow as changeCity
import NoInternet as noInternet

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, \
    QProgressBar, QMessageBox

from urllib.request import urlopen

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        switch_window = QtCore.pyqtSignal(str)

        self.setWindowIcon(QtGui.QIcon("Images/sun.png"))
        self.top = 200
        self.left = 350
        self.width = 700
        self.height = 408
        self.title = "Current Weather — Weathr"

        self.unitChoice = 'C'
        self.speedUnitChoice = 'KPH'

        self.changeCityWindow = changeCity.ChangeCityWindow()
        self.settingsWindow = units.ConversionsWindow(self)
        self.setStyleSheet(
            'QMainWindow {'
            '   background-image: url(Images/sunnysky.jpg);'
            '}'
            'QLabel {'
            '   color: black;'
            '   font-size: 18px;'
            '}'
            )

        self.internetGoneWindow = noInternet.NoInternetWindow()
        self.internetStatus = 1

        self.get_internet()

        if self.internetStatus == 1:
            self.UIComponents()
            self.InitWindow()
        else:
            print('status is 0')
            self.internetGoneWindow.show()

    def InitWindow(self):
        self.move(self.left, self.top)
        self.setFixedSize(self.width, self.height)

        #set window title
        #self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        #self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('Images/iconfinder_weather-01_1530392.png'))
        #show to window
        self.show()

    def UIComponents(self):

        # deal with the speed unit (good thing I dont. it's annoying)
        with open('src/saves/speed.txt', 'r'):
            if 'KPH' in open('src/saves/speed.txt').read():
                self.speedUnitChoice = 'KPH'
                self.settingsWindow.kphRadio.setChecked(True)
            elif 'MPH' in open('src/saves/speed.txt').read():
                self.speedUnitChoice = 'MPH'
                self.settingsWindow.mphRadio.setChecked(True)

        with open('src/saves/temp.txt', 'r'):
            if 'C' in open('src/saves/temp.txt').read():
                self.unitChoice = 'C'
                self.settingsWindow.cRadioTemp.setChecked(True)
            elif 'F' in open('src/saves/temp.txt').read():
                self.unitChoice = 'F'
                self.settingsWindow.fRadioTemp.setChecked(True)
            elif 'K' in open('src/saves/temp.txt').read():
                self.unitChoice = 'K'
                self.settingsWindow.kRadioTemp.setChecked(True)

        # all the weather labels will go in here:
        self.cityDisplayName = QLabel(self)
        self.cityDisplayName.setStyleSheet("font-weight: bold; font-size: 25px;")
        self.cityDisplayName.setText("City Weather")
        self.cityDisplayName.move(15, 10)
        self.cityDisplayName.resize(600, 30)

        #create the icon here and resize it:
        self.imageIconLabel = QLabel(self)
        self.icon = QPixmap('Images/iconfinder_weather-01_1530392.png')
        self.imageIconLabel.setPixmap(self.icon)
        self.imageIconLabel.setGeometry(0, 43, 200, 90)

        #set the reload weather progress bar
        self.reloadProgressbar = QProgressBar(self)
        self.reloadProgressbar.setGeometry(15, 320, 315, 20)
        self.reloadProgressbar.setMaximum(100)
        self.reloadProgressbar.hide()

        #create the refresh label
        self.refreshLabel = QLabel(self)
        self.refreshLabel.move(10, 380)
        self.refreshLabel.resize(600, 30)

        #weather labels
        self.weatherTemp = QLabel(self)
        self.weatherTemp.move(15, 135)
        self.weatherTemp.resize(600, 30)
        self.descWeather = QLabel(self)
        self.descWeather.move(100, 135)
        self.descWeather.resize(600, 30)
        self.humidityLabel = QLabel(self)
        self.humidityLabel.move(15, 185)
        self.humidityLabel.resize(600, 30)
        self.windSpeedLabel = QLabel(self)
        self.windSpeedLabel.move(15, 210)
        self.windSpeedLabel.resize(600, 30)
        self.windDegreeLabel = QLabel(self)
        self.windDegreeLabel.move(15, 235)
        self.windDegreeLabel.resize(600, 30)
        self.countryLabel = QLabel(self)
        self.countryLabel.move(15, 260)
        self.countryLabel.resize(600, 30)

        if self.internetStatus == 1:
            self.getWeather()
        else:
            pass

        self.cityBtn = QPushButton(QIcon('Images/marker.png'), "Change City", self)
        self.cityBtn.move(15, 350)
        self.cityBtn.resize(120, 30)
        self.cityBtn.setStyleSheet('background-color: #7c807e;')
        self.cityBtn.clicked.connect(self.changeCityWindow.show)
        self.cityBtn.clicked.connect(self.close)
        self.cityBtn.setShortcut('Ctrl+Shift+C')


        self.settingsBtn = QPushButton(QIcon('Images/gearsettings.png'), "Preferences", self)
        self.settingsBtn.move(140, 350)
        self.settingsBtn.resize(120, 30)
        self.settingsBtn.setStyleSheet('background-color: #7c807e;')
        self.settingsBtn.clicked.connect(self.openUnitsMenu)
        self.settingsBtn.clicked.connect(self.close)
        self.settingsBtn.setToolTip('Open the Preferences to change the settings')
        self.settingsBtn.setShortcut('Ctrl+P')

        #create the about window button
        self.aboutBtn = QPushButton(QIcon('Images/qmark.svg'), "", self)
        self.aboutBtn.move(300, 350)
        self.aboutBtn.resize(30, 30)
        self.aboutBtn.clicked.connect(self.openAboutWindow)
        self.aboutBtn.setStyleSheet('background-color: #7c807e;')

        #create the reload button
        self.reloadBtn = QPushButton(QIcon('Images/refresh.png'), "", self)
        self.reloadBtn.move(265, 350)
        self.reloadBtn.resize(30, 30)
        self.reloadBtn.setStyleSheet('background-color: #7c807e;')
        self.reloadBtn.clicked.connect(self.reloadWeather)
        self.reloadBtn.setShortcut('Ctrl+R')

    def openAboutWindow(self):
        self.aboutWindow = about.AboutWindow()
        self.aboutWindow.show()
        self.settingsWindow.close()

    def openUnitsMenu(self):
        self.aboutWindow = about.AboutWindow()
        self.settingsWindow = units.ConversionsWindow(self)
        self.settingsWindow.show()
        self.aboutWindow.close()

    def getWeather(self):

        # put it into text field in the main window
        fread = open("src/saves/startupcity.txt", "r")
        if fread.mode == "r":
            self.contents = fread.read()
            print(self.contents)

        self.cityName = self.contents

        if self.contents == '' or self.contents == ' ':
            self.changeCityWindow.show()
            with open('src/saves/startupcity.txt', "w") as f:
                f.write('New York')
            self.close()

        #if you are viewing the source code, the key will be x'd out. Get your own key at openweathermap.org when testing
        self.api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=YOUR_API_KEY_HERE&q='
        self.inputtedCity = self.contents

        self.url = self.api_address + self.inputtedCity
        self.json_data = requests.get(self.url).json()

        if self.json_data["cod"] == "404":
            #self.changeCityWindow.show()
            self.cityError = QMessageBox.critical(self.changeCityWindow, 'City Not Found!', 'The city inputted wasn\'t found. Loading backup city "New York" instead.', QMessageBox.Ok)
            self.changeCityWindow.cancelBtn.setDisabled(True)
            with open('src/saves/startupcity.txt', "w") as f:
                f.write('New York')
            self.close()

        self.tempData = int(self.json_data["main"]["temp"])
        self.tempDataFormatted = round(self.tempData)

        self.tempDataFormattedC = int(self.tempData) - 273.15
        self.tempDataRoundedC = round(self.tempDataFormattedC)

        self.tempDataFormattedF = int(self.tempData) * 9/5 - 459.67
        self.tempDataRoundedF = round(self.tempDataFormattedF)

        self.windData = self.json_data["wind"]["speed"]
        self.windDataFormattedKPH = int(self.json_data["wind"]["speed"]) * 3.6
        self.windDataRoundedKPH = round(self.windDataFormattedKPH)

        self.windDataFormattedMPH = int(self.windDataRoundedKPH) / 1.609
        self.windDataRoundedMPH = round(self.windDataFormattedMPH)

        if self.unitChoice == 'C':
            self.weatherTemp.setText(str(self.tempDataRoundedC) + "° C")

        elif self.unitChoice == 'F':
            self.weatherTemp.setText(str(self.tempDataRoundedF) + "° F")

        elif self.unitChoice == 'K':
            self.weatherTemp.setStyleSheet('font-size: 12px;')
            self.weatherTemp.setText(str(self.tempData) + "° K")

        #change the title
        self.setWindowTitle(self.json_data["name"]+ ', ' +self.json_data["sys"]["country"])

        self.weatherTemp.setStyleSheet('font-weight: bold; font-size: 25px;')
        self.descWeather.setStyleSheet('font-weight: bold; font-size: 20px;')

        self.descData = self.json_data["weather"][0]["description"]
        self.descWeather.setText(str(self.descData))
        self.humidityData = self.json_data["main"]["humidity"]
        self.humidityLabel.setText("Humidity               " +str(self.humidityData)+ "%")
        if self.speedUnitChoice == 'KPH':
            self.windSpeedLabel.setText("Wind Speed        " +str(self.windDataRoundedKPH)+ " KPH")
        elif self.speedUnitChoice == 'MPH':
            self.windSpeedLabel.setText("Wind Speed        " +str(self.windDataRoundedMPH)+ " MPH")
        self.countryData = self.json_data["sys"]["country"]
        self.countryLabel.setText("Country                 " +str(self.countryData))

        self.cityDisplayName.setText(self.json_data["name"]+ ", " +self.json_data["sys"]["country"])
        self.windDegreeLabel.setText("Pressure            " +str(self.json_data["main"]["pressure"]) + " hPa")

        #change the icons
        if self.json_data["weather"][0]["main"] == "Clear":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-01_1530392.png'))
        elif self.json_data["weather"][0]["main"] == "Clouds":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-02_1530391.png'))
        elif self.json_data["weather"][0]["main"] == "Thunderstorm":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-23_1530363.png'))
        elif self.json_data["weather"][0]["main"] == "Rain":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-31_1530364.png'))
        elif self.json_data["weather"][0]["main"] == "Drizzle" or self.json_data["weather"][0]["description"] == "light rain" or self.json_data["weather"][0]["description"] == "moderate rain":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-30_1530365.png'))
        elif self.json_data["weather"][0]["main"] == "Snow" or self.json_data["weather"][0]["description"] == "freezing rain":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-24_1530371.png'))
        elif self.json_data["weather"][0]["main"] == "Haze" or self.json_data["weather"][0]["main"] == "Smoke" or self.json_data["weather"][0]["main"] == "Fog" or self.json_data["weather"][0]["description"] == "mist":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-27_1530368.png'))
        elif self.json_data["weather"][0]["main"] == "Dust" or self.json_data["weather"][0]["main"] == "Sand":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-28_1530367.png'))
        elif self.json_data["weather"][0]["main"] == "Tornado":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfind_weather-29_1530366 (1).png'))

        #handle the backgrounds
        if self.json_data["weather"][0]["main"] == "Clear":
            self.setStyleSheet('QMainWindow { background-image: url(Images/sunnysky.jpg);}')
        elif self.json_data["weather"][0]["main"] == "Clouds":
            self.setStyleSheet('QMainWindow { background-image: url(Images/clouds.png);}')
        elif self.json_data["weather"][0]["main"] == "Thunderstorm":
            self.setStyleSheet('QMainWindow { background-image: url(Images/thunder.png);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Rain":
            self.setStyleSheet('QMainWindow { background-image: url(Images/rain.jpg);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Drizzle" or self.json_data["weather"][0]["description"] == "light rain" or self.json_data["weather"][0]["description"] == "moderate rain":
            self.setStyleSheet('QMainWindow { background-image: url(Images/drizzle.jpg);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Snow" or self.json_data["weather"][0]["description"] == "freezing rain":
            self.setStyleSheet('QMainWindow { background-image: url(Images/snow.jpg);}')
        elif self.json_data["weather"][0]["main"] == "Haze" or self.json_data["weather"][0]["main"] == "Smoke" or self.json_data["weather"][0]["main"] == "Fog" or self.json_data["weather"][0]["description"] == "mist":
            self.setStyleSheet('QMainWindow { background-image: url(Images/mist.jpg);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Dust" or self.json_data["weather"][0]["main"] == "Sand":
            self.setStyleSheet('QMainWindow { background-image: url(Images/tornado.jpg);}')
        elif self.json_data["weather"][0]["main"] == "Tornado":
            self.setStyleSheet('QMainWindow { background-image: url(Images/tornado.jpg);}')

    def reloadWeather(self):

        self.currentDateTime = datetime.datetime.now()
        self.dateTimeMessage = self.currentDateTime.strftime("Last Refreshed on %a %-l:%M %p on %Y/%m/%d")

        self.reloadProgressbar.show()
        self.count = 0
        self.TIME_LIMIT = 100
        while self.count < self.TIME_LIMIT:
            self.count += 1
            self.reloadProgressbar.setValue(self.count)
            if self.count >= self.TIME_LIMIT:
                self.reloadProgressbar.hide()

        self.refreshLabel.setText(self.dateTimeMessage)
        self.refreshLabel.setStyleSheet('font-size: 12px;')

        #change the temperature
        if self.unitChoice == 'C':
            self.weatherTemp.setText(str(self.tempDataRoundedC) + "° C")

        elif self.unitChoice == 'F':
            self.weatherTemp.setText(str(self.tempDataRoundedF) + "° F")

        elif self.unitChoice == 'K':
            self.weatherTemp.setStyleSheet('font-size: 12px;')
            self.weatherTemp.setText(str(self.tempData) + "° K")

        #change the other labels
        self.humidityLabel.setText("Humidity               " + str(self.humidityData) + "%")
        if self.speedUnitChoice == 'KPH':
            self.windSpeedLabel.setText("Wind Speed        " + str(self.windDataRoundedKPH) + " KPH")
        elif self.speedUnitChoice == 'MPH':
            self.windSpeedLabel.setText("Wind Speed        " + str(self.windDataRoundedMPH) + " MPH")
        self.countryData = self.json_data["sys"]["country"]
        self.countryLabel.setText("Country                 " + str(self.countryData))

        self.cityDisplayName.setText(self.json_data["name"] + ", " + self.json_data["sys"]["country"])
        self.windDegreeLabel.setText("Pressure            " + str(self.json_data["main"]["pressure"]) + " hPa")

        print(self.windSpeedLabel.text())
        print(self.weatherTemp.text())

        #change the imagery
        if self.json_data["weather"][0]["main"] == "Clear":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-01_1530392.png'))
        elif self.json_data["weather"][0]["main"] == "Clouds":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-02_1530391.png'))
        elif self.json_data["weather"][0]["main"] == "Thunderstorm":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-23_1530363.png'))
        elif self.json_data["weather"][0]["main"] == "Rain":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-31_1530364.png'))
        elif self.json_data["weather"][0]["main"] == "Drizzle" or self.json_data["weather"][0]["description"] == "light rain" or self.json_data["weather"][0]["description"] == "moderate rain":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-30_1530365.png'))
        elif self.json_data["weather"][0]["main"] == "Snow" or self.json_data["weather"][0]["description"] == "freezing rain":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-24_1530371.png'))
        elif self.json_data["weather"][0]["main"] == "Haze" or self.json_data["weather"][0]["main"] == "Smoke" or self.json_data["weather"][0]["main"] == "Fog" or self.json_data["weather"][0]["description"] == "mist":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-27_1530368.png'))
        elif self.json_data["weather"][0]["main"] == "Dust" or self.json_data["weather"][0]["main"] == "Sand":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-28_1530367.png'))
        elif self.json_data["weather"][0]["main"] == "Tornado":
            self.imageIconLabel.setPixmap(QPixmap('Images/iconfinder_weather-29_1530366 (1).png'))

        #handle the backgrounds
        if self.json_data["weather"][0]["main"] == "Clear":
            self.setStyleSheet('QMainWindow { background-image: url(Images/sunnysky.jpg); background-size: cover;}')
        elif self.json_data["weather"][0]["main"] == "Clouds":
            self.setStyleSheet('QMainWindow { background-image: url(Images/clouds.png); background-size: cover;}')
        elif self.json_data["weather"][0]["main"] == "Thunderstorm":
            self.setStyleSheet('QMainWindow { background-image: url(Images/thunder.png);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Rain":
            self.setStyleSheet('QMainWindow { background-image: url(Images/rain.jpg);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Drizzle" or self.json_data["weather"][0]["description"] == "light rain" or self.json_data["weather"][0]["description"] == "moderate rain":
            self.setStyleSheet('QMainWindow { background-image: url(Images/drizzle.jpg);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Snow" or self.json_data["weather"][0]["description"] == "freezing rain":
            self.setStyleSheet('QMainWindow { background-image: url(Images/snow.jpg);}')
        elif self.json_data["weather"][0]["main"] == "Haze" or self.json_data["weather"][0]["main"] == "Smoke" or self.json_data["weather"][0]["main"] == "Fog" or self.json_data["weather"][0]["description"] == "mist":
            self.setStyleSheet('QMainWindow { background-image: url(Images/mist.jpg);} QLabel { color: white; }')
        elif self.json_data["weather"][0]["main"] == "Dust" or self.json_data["weather"][0]["main"] == "Sand":
            self.setStyleSheet('QMainWindow { background-image: url(Images/tornado.jpg);}')
        elif self.json_data["weather"][0]["main"] == "Tornado":
            self.setStyleSheet('QMainWindow { background-image: url(Images/tornado.jpg);}')

    def get_internet(self):
        try:
            urlopen('http://twitter.com', timeout=10)
            print('Internets on')
            self.internetStatus = 1
        except:
            print('Internets Off')
            self.internetStatus = 0

    def closeEvent(self, event):

        self.tray_icon.showMessage("Refreshed Weather", "Refreshed the weather on %a %-l:%M %p on %c",
                                   QSystemTrayIcon.Information, 5000)

        self.aboutWindow.close()
        self.changeCityWindow.close()
        self.settingsWindow.close()

if __name__ == "__main__":

    App = QApplication(sys.argv)
    App.setStyle('QtCurve')
    window = Window()
    sys.exit(App.exec_())