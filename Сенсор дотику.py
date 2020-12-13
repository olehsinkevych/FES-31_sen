import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TouchPin = 13
LedPin   = 15

GPIO.setmode(GPIO.BOARD)       
GPIO.setup(LedPin, GPIO.OUT)  
GPIO.output(LedPin, GPIO.HIGH)  
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:

    while True:
        if GPIO.input(TouchPin) == GPIO.LOW:
            print '...led on'
            GPIO.output(LedPin, GPIO.LOW)  # led on
            time.sleep(0.1)
        else:
            print 'led off...'
            GPIO.output(LedPin, GPIO.HIGH) # led off
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH) 
    GPIO.cleanup()   
