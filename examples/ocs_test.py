import RPi.GPIO as GPIO
import time

oc_1_pin = 22
oc_2_pin = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(oc_1_pin, GPIO.OUT)
GPIO.setup(oc_2_pin, GPIO.OUT)

GPIO.output(oc_1_pin, 0)
GPIO.output(oc_2_pin, 0)

input("oc1 on")
GPIO.output(oc_1_pin, 1)

input("oc1 off")
GPIO.output(oc_1_pin, 0)

input("oc2 on")
GPIO.output(oc_2_pin, 1)

input("oc2 on")
GPIO.output(oc_2_pin, 0)

input("done")
