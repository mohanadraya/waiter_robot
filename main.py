import time
from sensors.ir_sensor import setup_ir, read_ir, cleanup_ir
from motors.motor_driver import setup_motors, move_forward, turn_left, turn_right, stop_motors, cleanup_motors


def follow_line():
    setup_ir()
    setup_motors()
    print("line folowing")


    try:

        while True:
            left, right = read_ir()
            print(left ,"  " ,right)
            if left == 0 and right == 0:
                move_forward()
            elif left == 1 and right == 1:
                turn_left()
            elif left == 0 and right == 1:
                turn_right()
            else:
                stop_motors()
                print("robot stop")

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("ropor foreced stop.")

    finally:
        stop_motors()
        cleanup_ir()
        cleanup_motors()

if __name__ == "__main__":
    follow_line()


