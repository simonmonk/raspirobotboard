'''
To make the serial port accessible you must stop the kernal
using it by following the instructions here:

www.irrational.net/2012/04/19/using-the-raspberry-pis-serial-port

Note. MaxSorar has inverted TTL output so you get giggerish.
Single transistor invertor does the trick.

'''

import serial
import time

DEVICE = '/dev/ttyAMA0'
BAUD = 9600

ser = serial.Serial(DEVICE, BAUD)
while 1:
    msg = ser.read(5)
    print(msg)
              
