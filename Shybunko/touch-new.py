import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TouchPin = 13
LedPin   = 15

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def touch_call(channel):
    print "Event detected"
    GPIO.output(LedPin, GPIO.HIGH)
    print "Led_on"
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW)
    print "Led_off"

GPIO.add_event_detect(TouchPin, GPIO.RISING, callback=touch_call, bouncetime=100)

try:
    print "start"
    while True:
        print "wait_touch"
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
