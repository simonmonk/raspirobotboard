#raspirobotboard.py Library

import RPi.GPIO as GPIO
import serial
import time

DEVICE = '/dev/ttyAMA0'
BAUD = 9600

LEFT_GO_PIN = 17
LEFT_DIR_PIN = 4
RIGHT_GO_PIN = 10
RIGHT_DIR_PIN = 25   
SW1_PIN = 11
SW2_PIN = 9
LED1_PIN = 7
LED2_PIN = 8
OC1_PIN = 22
OC2_PIN = 21

class RaspiRobot:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(LEFT_GO_PIN, GPIO.OUT)
        GPIO.setup(LEFT_DIR_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_GO_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_DIR_PIN, GPIO.OUT)

        GPIO.setup(LED1_PIN, GPIO.OUT)
        GPIO.setup(LED2_PIN, GPIO.OUT)
        GPIO.setup(OC1_PIN, GPIO.OUT)
        GPIO.setup(OC2_PIN, GPIO.OUT)

        GPIO.setup(SW1_PIN, GPIO.IN)
        GPIO.setup(SW2_PIN, GPIO.IN)
        
        self.ser = None



    def set_motors(self, left_go, left_dir, right_go, right_dir):
        GPIO.output(LEFT_GO_PIN, left_go)
        GPIO.output(LEFT_DIR_PIN, left_dir)
        GPIO.output(RIGHT_GO_PIN, right_go)
        GPIO.output(RIGHT_DIR_PIN, right_dir)

    def forward(self, seconds=0):
        self.set_motors(1, 0, 1, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def stop(self):
        self.set_motors(0, 0, 0, 0)
 
    def reverse(self, seconds=0):
        self.set_motors(1, 1, 1, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()
    
    def left(self, seconds=0):
        self.set_motors(1, 0, 1, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds=0):
        self.set_motors(1, 1, 1, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def sw1_closed(self):
        return not GPIO.input(SW1_PIN)

    def sw2_closed(self):
        return not GPIO.input(SW2_PIN)

    def set_led1(self, state):
        GPIO.output(LED1_PIN, state)

    def set_led2(self, state):
        GPIO.output(LED2_PIN, state)

    def set_oc1(self, state):
        GPIO.output(OC1_PIN, state)

    def set_oc2(self, state):
        GPIO.output(OC2_PIN, state)    

    def get_range_inch_raw(self):
        msg = 'R000'
        if self.ser == None:
            self.ser = serial.Serial(DEVICE, BAUD)
        if self.ser.inWaiting() > 4:
            msg = self.ser.read(5)
        reading = int(msg[1:4])
        return reading

    def get_range_inch(self):
        readings = []
        for i in range(0, 9):
            reading = self.get_range_inch_raw()
            if reading > 0:
                readings.append(reading)
        self.ser.flushInput()
        if len(readings) == 0:
               return 0
        else:
            return sum(readings) / len(readings)

    def get_range_cm(self):
        return int(self.get_range_inch() * 2.5)
        
    def test(self):
        raw_input("forward")
        self.forward(2)

        raw_input("left")
        self.left(2)

        raw_input("right")
        self.right(2)

        raw_input("reverse")
        self.reverse(2)

        raw_input("stop")
        self.stop()


        raw_input("End of test")
