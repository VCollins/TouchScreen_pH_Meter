#import relevant libraries
import time
import spidev
import RPi.GPIO as GPIO
import sys
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

#configure device and call readadc function to retrieve input from pH sensor device
def main():
    global msg
    root = Tk()
    frame = Frame(root, width=400, height=400)
    frame.grid()
    frameButton = Button(frame, text="Quit", command=root.destroy).grid(column=0, row=1, padx=100, pady=20)
    frameLabel = Label(frame, text=msg).grid(column=0, row=0, padx=100, pady=20)
    while True:
        returnedValue = readadc(1) #read adc channel 1
        calculatedValue = float(returnedValue / 1024) * (3.3 / 1000) #reading is in millivolts
        gainvalue = 4665
        calibrationValue = 1.045
        pHValue = (14 - (gainvalue * calculatedValue * calibrationValue))
        msg = "pH Value: " + str(round(pHValue, 2))
        time.sleep(5)
        print(msg)
        #update Label value
        frameLabel.config(text = msg)
        #place updated widget in GUI window
        #frameLabel.pack()
        root.mainloop()
        time.sleep(10)

main()