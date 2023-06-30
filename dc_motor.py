import RPi.GPIO as GPIO

from client import send_report
from statics import DC_MOTOR_PIN


def start_motor():
    send_report("DCMotor", "on")
    GPIO.output(DC_MOTOR_PIN, GPIO.HIGH)


def stop_motor():
    send_report("DCMotor", "off")
    GPIO.output(DC_MOTOR_PIN, GPIO.LOW)
