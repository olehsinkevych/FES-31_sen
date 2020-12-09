import RPi.GPIO as GPIO
import time

TOUCH = 13
LED = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
#GPIO.output(LED, GPIO.HIGH)
GPIO.setup(TOUCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    state = False
    while True:

        if GPIO.input(TOUCH):
            state = True
            print("Touch detected!")

        elif GPIO.input(LED) and GPIO.input(TOUCH):
            state = False

        GPIO.output(LED, state)
        print("Touch change")
        time.sleep(0.5)

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print("All done.")
        GPIO.cleanup()
