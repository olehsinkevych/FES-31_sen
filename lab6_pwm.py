import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

pwm = GPIO.PWM(13, 50)
pwm.start(0)

try:
	while True:
		for frequency in range(10,101,10):
   	 		pwm.ChangeFrequency(frequency)
    		for duty in range(0,100,2):
        		print(f"Frequency: {frequency}Hz, Duty cycle: {duty}")
        		pwm.ChangeDutyCycle(duty)
        		time.sleep(0.1)
    		time.sleep(0.5)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
