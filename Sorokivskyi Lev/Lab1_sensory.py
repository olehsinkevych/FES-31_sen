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
            #Засвічується червоний світлодіод
        print "Red Pin ON"
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(7)
            #Вимикається червоний світлодіод
        print "Red Pin OFF"
        GPIO.output(red_pin, GPIO.LOW)

            #Засвічується жовтий світлодіод
        print "Yellow Pin ON"
        GPIO.output(yellow_pin, GPIO.HIGH)
        time.sleep(5)
            #Вимикається жовтий світлодіод
        print "Yellow Pin OFF"
        GPIO.output(yellow_pin, GPIO.LOW)

            #Засвічується зелений світлодіод на 5 секунд
        print "Green Pin ON"
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(5)
            #Зелений світлодіод заблимає декілька раз
        for i in range(3):
            print "Green Pin OFF"
            GPIO.output(green_pin, GPIO.LOW)
            time.sleep(0.7)
            print "Green Pin ON"
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(0.7)
            #Вимикається зелений світлодіод
        print "Green Pin OFF"
        GPIO.output(green_pin, GPIO.LOW)
            #Зелений світлодіод вимикається, цикл починається спочатку, ввімкнеться червоний світлодіод. Кінець циклу.



except KeyboardInterrupt:
    # pass
    GPIO.cleanup()
