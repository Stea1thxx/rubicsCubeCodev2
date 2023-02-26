import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
piu = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 18, 23, 24, 25, 8, 7]
for pin in piu:
    GPIO.setup(pin, GPIO.OUT)
#step (purple) is pulse to take one step, 800 steps per rotation
#direction (orange) is high for clockwise, low for anticlockwise
#enable (white) is active low.

ustp = 2
udir = 3
uena = 4

fstp = 17
fdir = 27
fena = 22

lstp = 10
ldir = 9
lena = 11

bstp = 5
bdir = 6
bena = 13

rstp = 18
rdir = 23
rena = 24

dstp = 25
ddir = 8
dena = 7

steps = ["U2", "R1", "L3", "F2", "D1", "B3"]

for step in steps:
    match step[0]:
        case "U":
            GPIO.output(uena, GPIO.LOW)
            GPIO.output(udir, GPIO.HIGH)
            for i in range(200*step[1]):
                GPIO.output(ustp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(ustp, GPIO.LOW)
                sleep(0.0001)
            GPIO.output(uena, GPIO.HIGH)
        case "F":
            GPIO.output(fena, GPIO.LOW)
            GPIO.output(fdir, GPIO.HIGH)
            for i in range(200*step[1]):
                GPIO.output(fstp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(fstp, GPIO.LOW)
                sleep(0.0001)
            GPIO.output(fena, GPIO.HIGH)
        case "L":
            GPIO.output(lena, GPIO.LOW)
            GPIO.output(ldir, GPIO.HIGH)
            for i in range(200*step[1]):
                GPIO.output(lstp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(lstp, GPIO.LOW)
                sleep(0.0001)
            GPIO.output(lena, GPIO.HIGH)
        case "B":
            GPIO.output(bena, GPIO.LOW)
            GPIO.output(bdir, GPIO.HIGH)
            for i in range(200*step[1]):
                GPIO.output(bstp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(bstp, GPIO.LOW)
                sleep(0.0001)
            GPIO.output(bena, GPIO.HIGH)
        case "R":
            GPIO.output(rena, GPIO.LOW)
            GPIO.output(rdir, GPIO.HIGH)
            for i in range(200*step[1]):
                GPIO.output(rstp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(rstp, GPIO.LOW)
                sleep(0.0001)
            GPIO.output(rena, GPIO.HIGH)
        case "D":
            GPIO.output(dena, GPIO.LOW)
            GPIO.output(ddir, GPIO.HIGH)
            for i in range(200*step[1]):
                GPIO.output(dstp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(dstp, GPIO.LOW)
                sleep(0.0001)
            GPIO.output(dena, GPIO.HIGH)