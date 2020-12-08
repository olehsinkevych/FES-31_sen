import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
    
LED_pin = 11
buzzer_pin = 15
Sensor_pin = 13
GPIO.setup(Sensor_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.LOW)
    
def sensosr(null):
    print "stop"
    GPIO.output(LED_pin, GPIO.HIGH)
    GPIO.output(buzzer_pin, GPIO.HIGH)
    
GPIO.add_event_detect(Sensor_pin, GPIO.FALLING, callback=sensosr(), bouncetime=10)
try:
    while True:
        time.sleep(3)
        print "wait 3 sec."
        if GPIO.input(Sensor_pin) == 1:
            GPIO.output(LED_pin, GPIO.LOW)
            GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()