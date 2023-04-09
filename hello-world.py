from math import sin, cos, atan, acos, pi
import time
from pylx16a.lx16a import *

LX16A.initialize("COM3", 0.1)

try:
    headL = LX16A(11)
    headR = LX16A(22)
    hipL = LX16A(33)
    hipR = LX16A(44)
    kneeL = LX16A(55)
    kneeR = LX16A(66)
    ankleL = LX16A(77)
    ankleR = LX16A(88)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

# 常量
# headLOffset = 100.56
# headROffset = 82.32
# hipLOffset = 108.48
# hipROffset = 150.96
# kneeLOffset = 152.16
# kneeROffset = 89.28
# ankleLOffset = 132.72
# ankleROffset = 102
#横向移动
headLOffset = 105.36
headROffset = 86.40
hipLOffset = 155.04
hipROffset = 117.12
kneeLOffset = 32.40
kneeROffset = 139.68
ankleLOffset = 110.64
ankleROffset = 126.24

l1 = 8
l2 = 5

stepClearance = 1
stepHeight = 13

def updateServoPos(target1, target2, target3, leg):
    if leg == 'l':
        hipL.move(hipLOffset + target1)
        kneeL.move(kneeLOffset + target2)
        ankleL.move(ankleLOffset + 90 - target3)
    elif leg == 'r':
        hipR.move(hipROffset - target1)
        kneeR.move(kneeROffset - target2)
        ankleR.move(ankleROffset - 90 + target3)

def pos(x, z, leg):
    hipRad2 = atan(x / z)
    hipDeg2 = hipRad2 * (180 / pi)
    z2 = z / cos(hipRad2)
    # hipRad1 = acos(min(1, max(-1, (l1**2 + z2**2 - l2**2) / (2 * l1 * z2))))
    hipRad1 = acos((l1**2 + z2**2 - l2**2) / (2 * l1 * z2))
    hipDeg1 = hipRad1 * (180 / pi)
    # kneeRad = pi - acos(min(1, max(-1, (l1**2 + l2**2 - z2**2) / (2 * l1 * l2))))
    kneeRad = pi - acos((l1**2 + l2**2 - z2**2) / (2 * l1 * l2))
    # ankleRad = pi / 2 + hipRad2 - acos(min(1, max(-1, (l2**2 + z2**2 - l1**2) / (2 * l2 * z2))))
    ankleRad = pi / 2 + hipRad2 - acos((l2**2 + z2**2 - l1**2) / (2 * l2 * z2))
    hipDeg = hipDeg1 + hipDeg2
    kneeDeg = kneeRad * (180 / pi)
    ankleDeg = ankleRad * (180 / pi)

    updateServoPos(hipDeg, kneeDeg, ankleDeg, leg)


    return hipDeg,kneeDeg,ankleDeg


# def takeStep(stepLength, stepVelocity):
#     for i in range(int(stepLength * 2)):
#         x = stepLength - i * 0.5
#         pos(x, stepHeight, 'r')
#         pos(-x, stepHeight - stepClearance, 'l')
#         time.sleep(stepVelocity)
#
#     for i in range(int(stepLength * 2)):
#         x = stepLength - i * 0.5
#         pos(-x, stepHeight - stepClearance, 'r')
#         pos(x, stepHeight, 'l')
#         time.sleep(stepVelocity)

def takeStep(stepLength, stepVelocity):
    hipDeg,kneeDeg,ankleDeg = pos(0, 11, 'r')
    time.sleep(stepVelocity)
    print('r', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    hipDeg,kneeDeg,ankleDeg = pos(0, 11, 'l')
    time.sleep(stepVelocity)
    print('l', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(0.1, 10.9, 'r')
    # time.sleep(stepVelocity)
    # print('r', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(-0.1, 10.9, 'l')
    # time.sleep(stepVelocity)
    # print('l', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(0.1, 10.8, 'r')
    # time.sleep(stepVelocity)
    # print('r', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(-0.1, 10.8, 'l')
    # time.sleep(stepVelocity)
    # print('l', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(0.3, 12.7, 'r')
    # time.sleep(stepVelocity)
    # print('r', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(-0.3, 12.7, 'l')
    # time.sleep(stepVelocity)
    # print('l', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(0.4, 12.6, 'r')
    # time.sleep(stepVelocity)
    # print('r', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(-0.4, 12.6, 'l')
    # time.sleep(stepVelocity)
    # print('l', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(0.5, 12.3, 'r')
    # time.sleep(stepVelocity)
    # print('r', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    # hipDeg,kneeDeg,ankleDeg = pos(-0.5, 12.3, 'l')
    # time.sleep(stepVelocity)
    # print('l', 'hip',hipDeg,'knee', kneeDeg, 'ankle',ankleDeg)
    time.sleep(stepVelocity)
    print('******************************************')

def initialize():
    # for i in range(int(10.7 * 10)):
    #     z = 10.7 - i * 0.1
    #     pos(0, z, 'l')
    #     pos(0, z, 'r')
    #     time.sleep(0.05)
    headL.move(headLOffset)
    headR.move(headROffset)
    hipL.move(hipLOffset)
    hipR.move(hipROffset)
    kneeL.move(kneeLOffset)
    kneeR.move(kneeROffset)
    ankleL.move(ankleLOffset)
    ankleR.move(ankleROffset)
def main():
    initialize()
    # while True:
    #     takeStep(1, 0.005)
    # takeStep(1,1)
    time.sleep(5)
    while True:
        headL.move(headLOffset + 12)
        time.sleep(1)
        headR.move(headROffset-6)
        headL.move(headLOffset-12)
        time.sleep(1)
        headR.move(headROffset+6)
    # hipR.move(hipROffset - 16)
    # hipL.move(hipLOffset + 16)
    # ankleR.move(ankleROffset + 13.7)
    # time.sleep(2)
    # hipL.move(hipLOffset+15)
if __name__ == "__main__":
    main()

