import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11,50)
p.start(0)
period = range(0,181,30)

def update_duty(angle):
	duty = float(angle)/18.0 + 2.5
	print(f"Angle: {angle}, Duty cycle: {duty:.2f}")
	p.ChangeDutyCycle(duty)
	time.sleep(.5)
	
try:	
	while True:	
		for forward_angle in period:
			update_duty(forward_angle)
			
		for backward_angle in reversed(period):
			update_duty(backward_angle)
			
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()   
    
