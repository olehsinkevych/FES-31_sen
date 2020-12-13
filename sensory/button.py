import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
red_led = 15, yellow_led = 13, green_led = 11

PIN_button = 37

led = {'first': False, 'second': False,'third': False}

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.setup(PIN_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def call(arg):
   GPIO.output(red_led, GPIO.LOW)
   GPIO.output(yellow_led, GPIO.LOW)
   GPIO.output(green_led, GPIO.LOW)
   
   if led['first']:
      for i in range(3):
        GPIO.output(red_led, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(red_led, GPIO.LOW)
      led['first'] = False
      led['second'] = True
      print "1 mode is activated"
   elif led['second']:
      for i in range(3):
        GPIO.output(yellow_led, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(yellow_led, GPIO.LOW)
      led['second'] = False
      led['third'] = True
      print "2 mode is activated"
   else:
      for i in range(3):
        GPIO.output(green_led, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(green_led, GPIO.LOW)
      led['third'] = False
      led['first'] = True
      print "3 mode is activated"
   

GPIO.add_event_detect(PIN_button, GPIO.FALLING, callback=call, bouncetime=200)

try:
   led['first'] = True
   while True:
      pass 

except KeyboardInterrupt:
    GPIO.cleanup()