import RPi.GPIO as GPIO

from statics import DC_MOTOR_PIN


def start_motor():
    GPIO.output(DC_MOTOR_PIN, GPIO.HIGH)


def stop_motor():
    GPIO.output(DC_MOTOR_PIN, GPIO.LOW)
