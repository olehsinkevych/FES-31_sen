import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TouchPin = 13
LedPin   = 15

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource

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

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    destroy()
