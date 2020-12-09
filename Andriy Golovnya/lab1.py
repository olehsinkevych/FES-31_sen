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
        #Світиться червоний діод
        print "Red pin ON"
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(7)
        #Вимикається червоний діод
        print "Red pin OFF"
        GPIO.output(red_pin, GPIO.LOW)
        
        #Світиться жовтий діод
        print "Yellow pin ON"
        GPIO.output(yellow_pin, GPIO.HIGH)
        time.sleep(5)
        #Вимикається жовтий діод
        print "Yellow pin OFF"
        GPIO.output(yellow_pin, GPIO.LOW)
        
        #Світиться зелений діод 5 секунд
        print "Green pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(5)
        #Зелений діод блимає декілька раз
        for i in range(3):
            print "Green pin OFF"
            GPIO.output(green_pin, GPIO.LOW)
            time.sleep(0.7)
            print "Green pin ON"
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(0.7)
        #Вимикається зелений діод
        print "Green pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
        #Кінець циклу; Зелений діод вимикається; цикл починається спочатку; вмикається червоний діод.

        

except KeyboardInterrupt:
    # pass
    GPIO.cleanup()
