import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TouchPin = 13
LedPin   = 15

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

try:
    while True:
        if GPIO.input(TouchPin) == GPIO.LOW:
            print 'LED ON'
            GPIO.output(LedPin, GPIO.LOW)
            time.sleep(0.1)
        else:
            print 'LED OFF'
            GPIO.output(LedPin, GPIO.HIGH)
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH) 
    GPIO.cleanup()   