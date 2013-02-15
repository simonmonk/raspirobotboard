import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

while True:
    pin = int(input("pin"))
    state = int(input("state"))
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, state)

