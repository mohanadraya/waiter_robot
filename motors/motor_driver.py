import RPi.GPIO as GPIO
import time


MOTOR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)


pwm = GPIO.PWM(MOTOR_PIN, 50)
pwm.start(0) 


def move_right():
    pwm.ChangeDutyCycle(6)


def move_left():
    pwm.ChangeDutyCycle(9)


def stop():
    pwm.ChangeDutyCycle(0)


def cleanup():
    pwm.stop()
    GPIO.cleanup()
