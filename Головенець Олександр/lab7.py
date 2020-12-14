import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11,50)
pwm.start(0)
period = range(0,181,30)

def pwm_duty(angle):
	duty = float(angle)/18.0 + 2.5
	print(f"Angle: {angle}, Duty: {duty:.2f}")
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	
try:	
	while True:	
		for forward_angle in period:
			pwm_duty(forward_angle)
			
		for backward_angle in reversed(period):
			pwm_duty(backward_angle)
			
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()   
    
