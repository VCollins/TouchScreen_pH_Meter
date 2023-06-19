# phSensorReaderTouchScreen
A Python-based program to read data from an analog pH sensor, connected to a Raspberry Pi 3B and display it on a touchscreen unit.

The pH sensor device is provided by DFRobot (https://community.dfrobot.com/makelog-308045.html) but this is a personal project, no commercial sponsorship or any endorsements apply. This project is also not intended to be used as a market product, but rather as a proof of concept.

Dependencies (at the time of development):

Raspbery Pi 3B with Raspbian installed

Python v3.10 - Available at https://www.python.org/downloads/release/python-3100/

Microsoft Visual Studio Build Tools must be installed for pip to build and install other dependencies (if attempting to build pip packages in Windows 11). Available at: https://visualstudio.microsoft.com/visual-cpp-build-tools/

Spidev 3.6 - Available at: https://pypi.org/project/spidev/

RPi.GPIO 0.7.1 - Available at https://pypi.org/project/RPi.GPIO/

tkinter v8.6.10 - Normally installed as part of the standard Python libraries

I used a Waveshare 7-inch touchscreen device with a resolution of 1024 x 600 for testing, while development was done in Visual Studio Code.

This project is available under the Creative Commons License suite.