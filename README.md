# Weathr — A Current Weather Application for Windows, Mac & Linux

This is an open-source current weather forecaster using OpenWeatherMaps and PyQt5 library.
It is written in Python 3. If you are installing from source, make sure to sign up for
[OpenWeatherMap](https://openweathermap.org/ "OpenWeatherMap") and request a key.

## Install from Source

Currently their is not actual file to download and install
currently, so you have to download from the source. To do so, use the 
command:

```
$ git clone https://github.com/henrybungee/weathr-forecast/
```
Then run the setup.py file. Let me know if the setup.py file isn't working.
Email me and copy and paste the error. Anyway, run this command:

```
$ python setup.py
```
And you can compile from the source code with an IDE
of choice or run the MainWindow.py file. Or simply 
download the repository and run the files.

**I PROMISE THAT I WILL RELEASE AN ACTUAL FILE SOON**

But for now, if you want a copy, just run from the source
or use [PyInstaller](https://www.pyinstaller.org/ "PyInstaller's Homepage")
to compile the MainWindow.py file to a .exe, a .AppImage
or a .app. 

## Features

Weathr is a simple tool. But I can give you
the basic information you need to operate the 
software. For starters, the first time you boot
up, your city should be set to New York. 

![screeshot](https://github.com/henrybungee/weathr-forecast/blob/master/Screenshot%20from%202019-08-30%2011-12-12.png "Screenshot")

To change the city, click on the button that says
"Change City" (Simple enough, huh?). 
When you open the dialog, it's quite self-explanatory.
You have the option of selecting your own city or 
tracking location instead.

**NEW IN 2.6.3:**
UV tracking has been added. There are 5 levels of 
intensity. LOW, MODERATE, HIGH, VERY HIGH, and
EXTREME. Each of these has their own colors. 

   **Note:**
The location tracking is dependent on 
the wifi. If your router's location is 
not the same as where you are, you are 
out of luck.

Also, you can change conversions. By default,
it is the metric system conversions (Celsius,
KPH, etc.) but you can chage to the metric system
and even the ISU (International System of Units).

#### Shortcuts

Change City: Ctrl+Shift+C
Preferences: Ctrl+P

## Conclusion

Weathr is under the GPL v3.0 and all the rules are
to be followed. The breaking of those rules are 
against the GPL. Otherwise, have fun with this little
software and continue to make changes. Also, I think
I need help making the code more efficient.
