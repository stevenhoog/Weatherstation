import RPi.GPIO as GPIO
from time import sleep

# Specify gpio pin
port = 17

# Specify last state
laststate = 1

# Set max timings
MAX_TIMINGS = 85
data = [0,0,0,0,0]
j = 0
 
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up the GPIO channels  - output
GPIO.setup(port, GPIO.OUT)

# Set pin low
GPIO.output(port, 0)
sleep(0.018)
GPIO.setup(port, GPIO.IN)


for i in range(MAX_TIMINGS):
  # While state of gpio doesn't change
  counter = 0
  while GPIO.input(port) == laststate:
    counter += 1
    sleep(0.0000001)
    if counter == 255:
      break
  laststate = GPIO.input(port)
  if counter == 255:
    break
  
  # ignore first 3 transitions
  if (i >= 4) and (i % 2 == 0):
    # Bitwise Left Shift
    data[int(j / 8)] << 1
    if counter > 16:
      data[(j / 8)] |= 1
    j += 1

  print(data)


  # Set up GPIO channel - input
  #print(GPIO.input(port))

