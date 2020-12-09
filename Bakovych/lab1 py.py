import RPi.GPIO as GPIO
import time

print "initialization"
GPIO.setmode(GPIO.BOARD)

green_pin = 11
red_pin = 15
yellow_pin = 13

GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)

try:
    while True:
        print "Red pin ON"
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(10)
        print "Red pin OFF"
        GPIO.output(red_pin, GPIO.LOW)
        
        
        print "Yellow pin ON"
        GPIO.output(yellow_pin, GPIO.HIGH)
        time.sleep(2)
        print "Yellow pin OFF"
        GPIO.output(yellow_pin, GPIO.LOW)
        
        
        print "Green pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(5)
        print "Green pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
        
        print "Green pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(1)
        print "Green pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
        
        print "Green pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(1)
        print "Green pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
        
        print "Green pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(1)
        print "Green pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
        

except KeyboardInterrupt:
    GPIO.cleanup()
