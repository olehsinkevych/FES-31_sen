import RPi.GPIO as GPIO
import time

LED = 11
CLAP = 40 

#GPIO.setup(CLAP,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(CLAP,GPIO.IN)


def main():
	clap = False
	while True:
		if  GPIO.input(CLAP)
			clap = not clap
			GPIO.output(LED,clap)
			print("Light on" if clap else "Light off")
			time.sleep(3)

if __name__ == '__main__':

    try:
        main() 
    except KeyboardInterrupt:
        print("All done.\nCleaning up")
        GPIO.cleanup()			

