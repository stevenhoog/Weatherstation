import RPi.GPIO as GPIO

def callback(channel):
    print(GPIO.input(channel))
 
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
 
# set up the GPIO channels - input
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
while True:
    print(GPIO.input(4))


