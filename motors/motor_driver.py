import RPi.GPIO as GPIO
import time

LEFT_MOTOR_PIN = 22
RIGHT_MOTOR_PIN = 23

def setup_motors():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_MOTOR_PIN, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_PIN, GPIO.OUT)

    global left_pwm, right_pwm
    left_pwm = GPIO.PWM(LEFT_MOTOR_PIN, 50)  # 50Hz
    right_pwm = GPIO.PWM(RIGHT_MOTOR_PIN, 50)
    left_pwm.start(0)  
    right_pwm.start(0)

def stop_motors():
    left_pwm.ChangeDutyCycle(0)
    right_pwm.ChangeDutyCycle(0)

def move_forward():
    left_pwm.ChangeDutyCycle(12)
    right_pwm.ChangeDutyCycle(6)

def turn_left():
    left_pwm.ChangeDutyCycle(0)   
    right_pwm.ChangeDutyCycle(6)  

def turn_right():
    left_pwm.ChangeDutyCycle(12)   
    right_pwm.ChangeDutyCycle(0)  

def cleanup_motors():
    left_pwm.stop()
    right_pwm.stop()
    GPIO.cleanup([LEFT_MOTOR_PIN, RIGHT_MOTOR_PIN])



def stop():
    pwm.ChangeDutyCycle(0)


def cleanup():
    pwm.stop()
    GPIO.cleanup()
