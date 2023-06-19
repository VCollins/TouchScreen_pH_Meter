#import relevant libraries
import sys
import time
import spidev
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import *

# set up GPIO pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
servo = GPIO.PWM(21, 50)
servo.start(2.5)
msg = " "

# set up SPI for pH Sensor as main program focus
spiMain = spidev.SpiDev() #create spi object
spiMain.open(0, 0) #open spi port 0, device (CS) 0, for the MCP3008
spiMain.max_speed_hz=1000000

#configure analog to digital chip pin configuration
def readadc(adcnum): #read out the ADC
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spiMain.xfer2([1, (8 + adcnum) << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout

class pHReaderFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #program statements for frame properties
        self.geometry('400x400')
        self.resizable(False, False)
        self.grid()
        self.frameButton = tk.Button(self, text="Quit", command=self.destroy).grid(column=0, row=1, padx=100, pady=20)
        self.frameLabel = tk.Label(self, text=" ").grid(column=0, row=0, padx=100, pady=20)
        self.frameButton.pack()
        #start frame loop running
        self.mainLoop()
    
    def mainLoop(self):
        global msg
        #call readadc function to retrieve input from pH sensor device
        while True:
            returnedValue = readadc(1) #read adc channel 1
            calculatedValue = float(returnedValue / 1024) * (3.3 / 1000) #reading is in millivolts
            gainvalue = 4665
            calibrationValue = 1.045
            pHValue = (14 - (gainvalue * calculatedValue * calibrationValue))
            msg = "pH Value: " + str(round(pHValue, 2))
            #introduce slight delay before updating label
            time.sleep(5) 
            #update Label value
            self.frameLabel.configure(text=msg)
            time.sleep(5)

if __name__=="__main__":
    app = pHReaderFrame()
    app.mainloop()