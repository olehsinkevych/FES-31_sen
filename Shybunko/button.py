import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED_pin = 11
Sensor_pin = 13
buzzer_pin = 15
GPIO.setup(Sensor_pin, GPIO.IN)
GPIO.

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
green_light = 11
yellow_light = 13
red_light = 15
PIN_button = 37

led_labels = {'red': False, 'yellow': False, 'green': False}

GPIO.setup(green_light, GPIO.OUT)
GPIO.setup(yellow_light, GPIO.OUT)
GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(PIN_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def call(arg):
    GPIO.output(green_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.LOW)
    GPIO.output(red_light, GPIO.LOW)
    if led_labels['red']:
        GPIO.output(red_light, GPIO.HIGH)
        led_labels['red'] = False
        led_labels['yellow'] = True
        print('red', led_labels)
    elif led_labels['yellow']:
        GPIO.output(yellow_light, GPIO.HIGH)
        led_labels['yellow'] = False
        led_labels['green'] = True
        print('yellow', led_labels)
    else:
        GPIO.output(green_light, GPIO.HIGH)
        led_labels['green'] = False
        led_labels['red'] = True
        print('green', led_labels)


GPIO.add_event_detect(PIN_button, GPIO.FALLING, callback=call, bouncetime=200)

try:
    led_labels['red'] = True
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()