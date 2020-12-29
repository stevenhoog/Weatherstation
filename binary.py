# Import GPIO library
import RPi.GPIO as GPIO

# Import sleep library
from time import sleep

# Determine whether bit data is a 1 or 0
def toBits(l):
  # If 1 occurs more than 3 times, it counts as a 1
  return 1 if len(l) > 3 else 0

def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def toBinary(l):
  return int(''.join(map(str,l)),2)

# Specify gpio pin
port = 17

def read_dht11():

  # to use Raspberry Pi board pin numbers
  GPIO.setmode(GPIO.BCM)

  data = [] # Define data array

  #### Activate sensor ####

  # set up the GPIO channels  - output
  GPIO.setup(port, GPIO.OUT)
  # Make sure GPIO has default status of HIGH
  GPIO.output(port, GPIO.HIGH)
  # Set GPIO pin to LOW for 18 milliseconds to ensure DHT11 has detected the signal
  GPIO.output(port, GPIO.LOW)
  sleep(0.018)

  # Set GPIO pin to HIGH
  GPIO.output(port, GPIO.HIGH)
  sleep(0.00002)

  ### READ BINARY VALUES ###

  # prepare to read the pin
  GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  for i in range(0,500):
    data.append(GPIO.input(port))

  # Zeroes serve as seperators
  bitsList = list(filter(None,''.join(map(str,data)).split("0")))

  # Make bits of list values
  data = list(map(toBits, bitsList))[:-1]
  chunkList = list(chunks(data,8))
  binaryList = list(map(toBinary, chunkList))

  # If data is correct
  if len(data) >= 40 and sum(binaryList[:4]) == binaryList[4]:
    print(binaryList[:-1])
#  else:
#    sleep(1)
    #read_dht11()
    #return float(str(binaryList[0])+"."+str(binaryList[1]), float(str(binaryList[2])+"."+str(binaryList[3])

while True:
  read_dht11()
  sleep(0.02)
