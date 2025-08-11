import RPi.GPIO as GPIO

LEFT_IR_PIN = 18
RIGHT_IR_PIN = 27

def setup_ir():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_IR_PIN, GPIO.IN)
    GPIO.setup(RIGHT_IR_PIN, GPIO.IN)

def read_ir():
    left = GPIO.input(LEFT_IR_PIN)
    right = GPIO.input(RIGHT_IR_PIN)
    return left, right

def cleanup_ir():
    GPIO.cleanup([LEFT_IR_PIN, RIGHT_IR_PIN])

