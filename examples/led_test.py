from raspirobotboard import *
import time

rr = RaspiRobot()

while True:
    rr.set_led1(True)
    rr.set_led2(False)
    time.sleep(0.5)
    rr.set_led1(False)
    rr.set_led2(True)
    time.sleep(0.5)

