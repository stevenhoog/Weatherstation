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
    for i in range(0, n):
        yield l[i::n]

def toBinary(l):
  return ''.join(map(str,l))


# Specify gpio pin
port = 17

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

def read_dht11():

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

  for i in range(0,600):
    data.append(GPIO.input(port))

  print(data)
  bitsList = list(filter(None,''.join(map(str,data)).split("0")))
  print(bitsList)
  data = list(map(toBits, bitsList))[:-1]
  print(data)
  print(len(data))
  chunkList = list(chunks(data,5))
  print(chunkList);
#binaryList = list(map(toBinary, chunkList))
  #print(binaryList)
  #print(bin(int(binaryList[0], 2) & int(binaryList[1],2) & int(binaryList[2],2) & int(binaryList[3],2)))

read_dht11()
sleep(1)
#binarySum = bin(int(binaryList[0], 2) + int(binaryList[1],2) + int(binaryList[2],2) + int(binaryList[3],2))
#print(binarySum)
