import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
red_led = 15
yellow_led = 13
green_led = 11

PIN_button = 37

mods = {'first': False,
        'second': False,
        'third': False}

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.setup(PIN_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def call(arg):
   GPIO.output(red_led, GPIO.LOW)
   GPIO.output(yellow_led, GPIO.LOW)
   GPIO.output(green_led, GPIO.LOW)
   
   if mods['first']:
      for i in range(3):
        GPIO.output(red_led, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(red_led, GPIO.LOW)
      mods['first'] = False
      mods['second'] = True
      print "the first mode is activated"
   elif mods['second']:
      for i in range(3):
        GPIO.output(yellow_led, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(yellow_led, GPIO.LOW)
      mods['second'] = False
      mods['third'] = True
      print "the second mode is activated"
   else:
      for i in range(3):
        GPIO.output(green_led, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(green_led, GPIO.LOW)
      mods['third'] = False
      mods['first'] = True
      print "the third mode is activated"
   

GPIO.add_event_detect(PIN_button, GPIO.FALLING, callback=call, bouncetime=200)

try:
   mods['first'] = True
   while True:
      pass 

except KeyboardInterrupt:
    GPIO.cleanup()