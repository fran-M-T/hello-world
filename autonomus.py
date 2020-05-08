#! /usr/bin/python2.7
import RPi.GPIO as GPIO
import time
import os
from main import main
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(13,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
OFF = GPIO.LOW
ON = GPIO.HIGH

print ("Hello this is starting\n")
print("STEP 0\n")

## Waiting for the input signal from a USB button to copy the file
while(GPIO.input(13) == 0):
        time.sleep(1)
try:
        os.system('cp -r /media/pi/* /home/pi/USB/')
except:
        pass
GPIO.output(16,ON)
os.system('cp /home/pi/USB/*.txt /home/pi/Desktop/Amtp_ShortRange/fitxer_USB.txt') #copy the file as *.txt

## Once USB button has been pressed, wait for start button.

print("STEP1\n")

while(GPIO.input(19) == 0):
        time.sleep(1)
print("Starting main as a new python\n")
print("STEP2\n")
GPIO.output(21,ON)
time.sleep(1)
GPIO.output(21,OFF)
GPIO.output(16,OFF)
time.sleep(0.5)
# Going to the Main project
main()


