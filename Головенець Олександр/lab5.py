import RPi.GPIO as GPIO
import time

LED = 11
MICRO = 40 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(MICRO,GPIO.IN)


def action():

	sound = False
	while True:
		if  GPIO.input(MICRO):
			sound = not sound
			GPIO.output(LED,sound)
			print("LED ON" if sound else "LED_OFF")
			time.sleep(0.5)

if __name__ == '__main__':

    try:
        action() 
    except KeyboardInterrupt:
        print("DONE")
        GPIO.cleanup()			

