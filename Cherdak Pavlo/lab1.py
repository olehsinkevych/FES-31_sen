import RPi.GPIO as GPIO
import time

print "////////////"
GPIO.setmode(GPIO.BOARD)

red_pin = 15
green_pin = 11
yellow_pin = 13

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)

try:
    while True:
        print "Red pin ON"
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(7)
        print "Red pin OFF"
        GPIO.output(red_pin, GPIO.LOW)
        
        print "Yellow pin ON"
        GPIO.output(yellow_pin, GPIO.HIGH)
        time.sleep(5)
        print "Yellow pin OFF"
        GPIO.output(yellow_pin, GPIO.LOW)
        
        print "Green pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(5)
        
        for i in range(3):
            print "Green pin OFF"
            GPIO.output(green_pin, GPIO.LOW)
            time.sleep(0.7)
            print "Green pin ON"
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(0.7)
        print "Green pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
       

  
except KeyboardInterrupt:
    # pass
    GPIO.cleanup()
