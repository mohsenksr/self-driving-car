import RPi.GPIO as GPIO

from client import send_report
from statics import LIGHT_PIN


def turn_light_on():
    send_report("Light", "on")

    GPIO.output(LIGHT_PIN, GPIO.HIGH)


def turn_light_off():
    send_report("Light", "off")

    GPIO.output(LIGHT_PIN, GPIO.LOW)
