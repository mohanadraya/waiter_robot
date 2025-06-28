from motors.motor_driver import move_left, move_right, stop, cleanup
from sensors.ir_sensor import read_ir_sensors
import time

try:
    while True:
        right_ir, left_ir = read_ir_sensors()
        print(f"Right IR: {right_ir}, Left IR: {left_ir}")

        if right_ir and not left_ir:

            move_right()
        elif left_ir and not right_ir:

            move_left()
#        else:

#            stop()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("robot stop")
    cleanup()

