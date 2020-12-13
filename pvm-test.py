import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

pwm = GPIO.PWM(13, 50)
pwm.start(0)

try:
    pwm.ChangeDutyCycle(50)
    input('F=50Hz, DC=50%. Press Enter...')
    pwm.ChangeDutyCycle(20)
    input('F=50Hz, DC=20%. Press Enter...')
    pwm.ChangeFrequency(10)
    pwm.ChangeDutyCycle(80)
    input('F=10Hz, DC=80%. Press Enter...')
    pwm.ChangeDutyCycle(10)
    input('F=10Hz, DC=10%. Press Enter to exit...')
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()