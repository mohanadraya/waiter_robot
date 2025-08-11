import RPi.GPIO as GPIO
import time

MOTOR_PIN = 22  # ����� ��� ���

def setup_motor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_PIN, GPIO.OUT)
    global pwm
    pwm = GPIO.PWM(MOTOR_PIN, 50)  # 50Hz
    pwm.start(0)

def test_servo():
    print("Neutral (7.5) - ����")
    pwm.ChangeDutyCycle(7.5)
    time.sleep(2)

    print("���� ����� (6.0) - �����/���� ������ ����")
    pwm.ChangeDutyCycle(6.0)
    time.sleep(3)

    print("Neutral (7.5) - ����")
    pwm.ChangeDutyCycle(7.5)
    time.sleep(2)

    print("���� ����� (9.0) - �����/���� �������� �����")
    pwm.ChangeDutyCycle(9.0)
    time.sleep(3)

    print("Neutral (7.5) - ����")
    pwm.ChangeDutyCycle(7.5)
    time.sleep(2)

def cleanup_motor():
    pwm.stop()
    GPIO.cleanup([MOTOR_PIN])

if __name__ == "__main__":
    setup_motor()
    try:
        test_servo()
    finally:
        cleanup_motor()
