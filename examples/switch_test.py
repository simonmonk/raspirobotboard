import RPi.GPIO as GPIO
from raspirobotboard import *

rr = RaspiRobot()

while True:
    print("SW1=" + str(rr.sw1_closed()) + " SW2=" + str(rr.sw2_closed()))
    input("check again")
    
    
