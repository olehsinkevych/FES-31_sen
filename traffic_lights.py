import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

red = ["red", 1, 3]
yellow = ["yellow", 2, 1]
green = ["green", 3, 5]

GPIO.setup(green[1], GPIO.OUT)
GPIO.setup(yellow[1], GPIO.OUT)
GPIO.setup(red[1], GPIO.OUT)


def turnlights(colour):
    print(f"Now is lighting: {colour[0].upper()}".center(40))
    GPIO.output(colour[1], True)
    countdown(colour[-1])


def countdown(sec):
    for i in range(sec, 0, -1):
        print(f"Wait:{i:02d}".center(40), end="\r")
        sleep(1)

try:
    while True:
		turnlights(red)
		turnlights(yellow)
		GPIO.output(red[1], False)
		GPIO.output(yellow[1], False)
		turnlights(green)
		GPIO.output(green[1], False)
		turnlights(yellow)
		GPIO.output(yellow[1], False)
        
except KeyboardInterrupt:
    GPIO.cleanup()

    
