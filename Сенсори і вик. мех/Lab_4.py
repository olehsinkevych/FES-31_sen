import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TouchPin = 13
LedPin   = 15

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

hlop = False
print ("Start")

try:
    while True:
		if GPIO.input(TouchPin):
			hlop = True
        		print ("We have found!")
		elif GPIO.input(LedPin) and GPIO.input(TouchPin):
			state = False
			print ("We have lost!")

except KeyboardInterrupt:
    	GPIO.output(LedPin, GPIO.HIGH)
	GPIO.cleanup()