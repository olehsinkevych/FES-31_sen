import RPi.GPIO as GPIO
import time

LED = 11
CLAP = 40 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(CLAP,GPIO.IN)
#GPIO.setup(CLAP,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
	clapp = False
	while True:
		if  GPIO.input(CLAP)
			clapp = not clapp
			GPIO.output(LED,clapp)
			print("ON" if clapp else "OFF")
			time.sleep(3)

if __name__ == '__main__':

    try:
        main() 
    except KeyboardInterrupt:
        print("Done.")
        GPIO.cleanup()			

