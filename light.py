import RPi.GPIO as GPIO
from statics import LIGHT_PIN

def turn_light_on():
    GPIO.output(LIGHT_PIN, GPIO.HIGH)

def turn_light_off():
    GPIO.output(LIGHT_PIN, GPIO.LOW)
