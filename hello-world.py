from math import sin, cos, atan, acos, pi
from math import cos, pi

import time
from lx16a import *

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    headL = LX16A(11)
    hipL = LX16A(22)
    kneeL = LX16A(33)
    ankleL = LX16A(44)
    headR = LX16A(55)
    hipR = LX16A(66)
    kneeR = LX16A(77)
    ankleR = LX16A(88)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()



headLOffset = 134.40   #1
hipLOffset = 148.32    #2
kneeLOffset = 45.36    #3
ankleLOffset = 174  #4
headROffset = 82.08    #5
hipROffset = 152.40    #6
kneeROffset = 162.72      #7
ankleROffset = 59.76      #8

move_time = 400

def initialize():
    headL.move(headLOffset,move_time)
    headR.move(headROffset,move_time)
    hipL.move(hipLOffset,move_time)
    hipR.move(hipROffset,move_time)
    kneeL.move(kneeLOffset,move_time)
    kneeR.move(kneeROffset,move_time)
    ankleL.move(ankleLOffset,move_time)
    ankleR.move(ankleROffset,move_time)

a=0.2

def main():
    while 1:
        initialize()
        ankleR.move(ankleROffset - 13, move_time)
        ankleL.move(ankleLOffset - 13, move_time)
        time.sleep(a)
        hipL.move(hipLOffset + 39, move_time)
        time.sleep(a)
        kneeL.move(kneeLOffset + 40, move_time)
        time.sleep(a)
        ankleR.move(ankleROffset , move_time)
        ankleL.move(ankleLOffset , move_time)
        time.sleep(a)
        ankleR.move(ankleROffset + 15, move_time)

        ankleL.move(ankleLOffset + 15 , move_time)
        time.sleep(a)
        hipR.move(hipROffset + 30, move_time)
        time.sleep(a)
        kneeL.move(kneeLOffset + 20 , move_time)

        kneeR.move(kneeROffset - 23, move_time)
        time.sleep(a)
        ankleR.move(ankleROffset , move_time)
        ankleL.move(ankleLOffset  , move_time)
        time.sleep(a)



if __name__ == "__main__":
    main()
