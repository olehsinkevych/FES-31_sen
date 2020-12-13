import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
pwm = GPIO.PWM(15, 50)
pwm.start(0)

try:
	while True:
		for fr in range(10,101,10):
   	 		pwm.ChangeFrequency(fr)
    		for d in range(0,100,2):
        		print(f"Frequency: {fr}Hz, Duty cycle: {d}")
        		pwm.ChangeDutyCycle(d)
        		time.sleep(.1)
    		time.sleep(.5)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
