import RPi.GPIO as GPIO

# ����� ������ ��� �������
RIGHT_IR_PIN = 27
LEFT_IR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RIGHT_IR_PIN, GPIO.IN)
GPIO.setup(LEFT_IR_PIN, GPIO.IN)

def read_ir_sensors():
    right = GPIO.input(RIGHT_IR_PIN) == 0  # 0 ������ ��� ����
    left = GPIO.input(LEFT_IR_PIN) == 0
    return right, left
