import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
def pick():
    GPIO.output(17, GPIO.LOW)
def drop():
    GPIO.output(17, GPIO.HIGH)