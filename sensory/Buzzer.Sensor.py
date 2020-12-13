import RPi.GPIO as GPIO
import time
    
GPIO.setmode(GPIO.BOARD)

led_pin = 11
Sensor_pin = 13
Buzzer_pin = 15

GPIO.setup(Sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(Buzzer_pin, GPIO.OUT, initial=GPIO.LOW)
    
def sens(null):
    print "Stop"
    GPIO.output(led_pin, GPIO.HIGH)
    GPIO.output(Buzzer_pin, GPIO.HIGH)
    
GPIO.add_event_detect(Sensor_pin, GPIO.FALLING, callback=sens, bouncetime=10)
try:
    while True:
        time.sleep(2)
        print "Wait"
        if GPIO.input(Sensor_pin) == 2:
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(Buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()  