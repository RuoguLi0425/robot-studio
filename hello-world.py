'''原版'''
from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("COM3", 0.1)

try:
    servo1 = LX16A(11)
    servo2 = LX16A(22)
    servo3 = LX16A(33)
    servo4 = LX16A(44)
    servo5 = LX16A(55)
    servo6 = LX16A(66)
    servo7 = LX16A(77)
    servo8 = LX16A(88)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
    servo7.set_angle_limits(0, 240)
    servo8.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    # servo1.move(sin(t) * 15 + 210)
    # servo2.move(cos(t) * 45 + 90)
    servo3.move(sin(t) * 45 + 180)
    servo4.move(cos(t) * 45 + 180)
    servo5.move(sin(t) * 15 + 210)
    servo6.move(cos(t) * 45 + 90)
    servo7.move(sin(t) * 15 + 210)
    servo8.move(cos(t) * 45 + 90)

    time.sleep(0.05)
    t += 0.1
'''改动电机捕获版本'''
# from math import sin, cos
# from lx16a import *
# import time
#
# while True:
#     try:
#         LX16A.initialize("COM3", 0.1)
#         servo1 = LX16A(1)
#         servo2 = LX16A(2)
#         servo1.set_angle_limits(0, 240)
#         servo2.set_angle_limits(0, 240)
#
#         t = 0
#         while True:
#             servo1.move(sin(t) * 15 + 210)
#             servo2.move(cos(t) * 45 + 90)
#
#             time.sleep(0.05)
#             t += 0.1
#
#     except ServoTimeoutError as e:
#         print(f"Servo {e.id_} is working，Please wait 5 seconds")
#         time.sleep(5)
#
#
#

