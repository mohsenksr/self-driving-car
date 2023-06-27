import random
import time

import RPi.GPIO as GPIO

from statics import FRONT_SENSOR_TRIGGER_PIN, FRONT_SENSOR_ECHO_PIN, PROXIMITY_THRESHOLD


def is_left_empty():
    return False
    return random.randint(0, 1) < 0.8


def is_right_empty():
    return False
    return random.randint(0, 1) < 0.8


def is_front_empty():
    pulse_start = 0
    pulse_end = 0
    # Set trigger to HIGH
    GPIO.output(FRONT_SENSOR_TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(FRONT_SENSOR_TRIGGER_PIN, GPIO.LOW)
    # Wait for echo to go high
    while GPIO.input(FRONT_SENSOR_ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    # Wait for echo to go low
    while GPIO.input(FRONT_SENSOR_ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    # Calculate distance

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound = 343 meters per second (17150 = 34300 / 2)
    distance = round(distance, 2)
    return distance > PROXIMITY_THRESHOLD
