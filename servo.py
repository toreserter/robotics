#!/usr/bin/python

from __future__ import division
import time
import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')

GPIO.setmode(GPIO.BCM)
#GPIO Pins of engines
engine1F = 4
engine1B = 17
engine2F = 27
engine2B = 22
pinList = [4, 17, 27, 22]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

current_mode = "servo"
# Import the PCA9685 module.
import Adafruit_PCA9685
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(0x40, 2)
# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
max_degree = 60
def_increase = 2

pwm.set_pwm_freq(60)
def convertAxis(value, axis_max):
    facteur=axis_max/245
    new_value=int(round((value/facteur)+75, 0)*2)
    return new_value

def set_degree(channel, d):
    degree_pulse = servo_min
    degree_pulse += int((servo_max - servo_min) / max_degree) * d
    pwm.set_pwm(channel, 0 ,degree_pulse)

def change_mode():
    global current_mode
    if current_mode == "servo":
        current_mode = "dc"
        print('DC Mode activated')
    else:
        current_mode = "servo"
        print('Servo Mode activated')
   

change_mode()
for event in gamepad.read_loop():
    e_code=event.code
    e_type=event.type
    e_value=event.value
    #for i in pinList:
        #GPIO.output(i, GPIO.LOW) #reset engines
    #print(str(e_type)+' - '+str(e_code)+' - '+str(e_value))
    print("code: " + str(e_code) + ", type: " + str(e_type) + ", value: " + str(e_value) ) # for debugging
    if e_type == 3:
        if e_code == 0: #joystick left
            e_value = e_value * -1 # because of reverse move
            servo_pos=str(convertAxis (e_value + 32768, 32768 * 2)) # adding another 32768 because it has negative values
            pwm.set_pwm(0, 0, int(servo_pos))
        elif e_code == 4: #up-down
            servo_pos=str(convertAxis (e_value + 32768, 32768 * 2)) # adding another 32768 because it has negative values
            pwm.set_pwm(1, 0, int(servo_pos))
        elif e_code == 2: #gas left
            if e_value > 100:
                GPIO.output(engine1B, GPIO.HIGH)
                GPIO.output(engine2B, GPIO.HIGH)
            else:
                GPIO.output(engine1B, GPIO.LOW)
                GPIO.output(engine2B, GPIO.LOW)
        elif e_code == 5: #gas right
            if e_value > 100:
                GPIO.output(engine1F, GPIO.HIGH)
                GPIO.output(engine2F, GPIO.HIGH)
            else:
                GPIO.output(engine1F, GPIO.LOW)
                GPIO.output(engine2F, GPIO.LOW)
    elif e_type == 1:
        if e_code == 304 and e_value == 1: # A button switch servo - dc motors
            change_mode()



                    #servo_pos=str(convertAxis (e_value, 256))
                    #pwm.set_pwm(0, 0, int(servo_pos))
                    #print('Servo pos:' + servo_pos + ' Y value:' + str(e_value))
# Helper function to make setting a servo pulse width simpler.
#def set_servo_pulse(channel, pulse):
#    pulse_length = 1000000    # 1,000,000 us per second
#    pulse_length //= 50       # 60 Hz
#    print('{0}us per period'.format(pulse_len
