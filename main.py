from enum import Enum
import time
import RPi.GPIO as GPIO

from statics import *
from dc_motor import start_motor, stop_motor

# from distances import is_front_empty, is_right_empty, is_left_empty
from distances import is_right_empty, is_left_empty

from light_sensor import is_enviromental_lights_enough
from light import turn_light_off, turn_light_on
from servo_motor import change_line_to_left, change_line_to_right


def is_front_empty():
    if elapsed_time % 10 == 0 and (elapsed_time // 10) % 2 == 0:
        print("Front is empty")
    elif elapsed_time % 10 == 0 and (elapsed_time // 10) % 2 == 1:
        print("Front is full")
    return (elapsed_time // 10) % 2 == 0

class MachineState(Enum):
    LINE1_MOVE = 1
    LINE1_BREAK = 2
    LINE2_MOVE = 3
    LINE2_BREAK = 4
    LINE3_MOVE = 5
    LINE3_BREAK = 6

class LightState(Enum):
    ON = 1
    OFF = 2

try:
    #initialize raspberry
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FRONT_SENSOR_TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(FRONT_SENSOR_ECHO_PIN, GPIO.IN)
    GPIO.setup(LEFT_SENSOR_ECHO_PIN, GPIO.IN)
    GPIO.setup(RIGHT_SENSOR_ECHO_PIN, GPIO.IN)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.setup(DC_MOTOR_PIN, GPIO.OUT)


    light_state = LightState.OFF
    machine_state = MachineState.LINE2_MOVE
    turn_light_off()
    stop_motor()
    

    start_command = input("type START to start machine\n")
    while not start_command == "START":
        start_command = input("type START to start machine\n")

    elapsed_time = 0
    start_motor()


    while True:
        print(f"time: {elapsed_time} {machine_state} {light_state}")
        time.sleep(1)
        elapsed_time += 1
        
        if is_enviromental_lights_enough():
            light_state = LightState.OFF
            turn_light_off()
        else:
            light_state = LightState.ON
            turn_light_on()

        if machine_state == MachineState.LINE1_MOVE:
            if is_front_empty():
                continue
            elif is_right_empty():
                machine_state = MachineState.LINE2_MOVE
                change_line_to_right()
            else:
                machine_state = MachineState.LINE1_BREAK
                stop_motor()
        
        elif machine_state == MachineState.LINE1_BREAK:
            if is_front_empty():
                machine_state = MachineState.LINE1_MOVE
                start_motor()
        
        elif machine_state == MachineState.LINE2_MOVE:
            if is_front_empty():
                continue
            elif is_right_empty():
                machine_state = MachineState.LINE3_MOVE
                change_line_to_right()
            elif is_left_empty():
                machine_state = MachineState.LINE1_MOVE
                change_line_to_left()
            else:
                machine_state = MachineState.LINE2_BREAK
                stop_motor()
        
        elif machine_state == MachineState.LINE2_BREAK:
            if is_front_empty():
                machine_state = MachineState.LINE2_MOVE
                start_motor()
        
        elif machine_state == MachineState.LINE3_MOVE:
            if is_front_empty():
                continue
            if is_left_empty():
                machine_state = MachineState.LINE2_MOVE
                change_line_to_left()
            else:
                machine_state = MachineState.LINE3_BREAK
                stop_motor()
        
        elif machine_state == MachineState.LINE3_BREAK:
            if is_front_empty():
                machine_state = MachineState.LINE3_MOVE
                start_motor()

except KeyboardInterrupt:
    print("Measurement stopped by user")
finally:
    GPIO.cleanup()