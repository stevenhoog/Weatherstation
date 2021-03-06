# Import GPIO library
import RPi.GPIO as GPIO

# Import sleep library
from time import sleep

class DHT11:

  # Constructor
  def __init__(self, port):
    self.port = port
    self.temperature = 0
    self.humidity = 0

   # If a 1 occurs more than 3 times in l, return 1
  @staticmethod
  def toBits(l):
    return 1 if len(l) > 3 else 0

  # Divide list in chunks of n values
  @staticmethod
  def chunks(l, n):
      # Lazy iterator
      for i in range(0, len(l), n):
          yield l[i:i + n]
  
  # List of bytes to integer values
  @staticmethod
  def byteToInt(l):
    return int(''.join(map(str,l)),2)

  def activateSensor(self):

    #### Activate sensor ####

    # set up the GPIO channels  - output
    GPIO.setup(self.port, GPIO.OUT)
    # Make sure GPIO has default status of HIGH
    GPIO.output(self.port, GPIO.HIGH)
    # Set GPIO pin to LOW for 18 milliseconds to ensure DHT11 has detected the signal
    GPIO.output(self.port, GPIO.LOW)
    sleep(0.018)


  def read(self):

    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BCM)

    data = [] # Define data array

    self.activateSensor()


    # Set GPIO pin to HIGH
    GPIO.output(self.port, GPIO.HIGH)
    sleep(0.00002)

    ### READ BINARY VALUES ###

    # prepare to read the pin
    GPIO.setup(self.port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for i in range(0,500):
      data.append(GPIO.input(self.port))

    # Zeroes serve as seperators
    bitsList = list(filter(None,''.join(map(str,data)).split("0")))


    # Make bits of list values
    data = list(map(self.toBits, bitsList))
    chunkList = list(self.chunks(data,8))
    

    if (len(bitsList) == 41):
      print(f"BITSLIST LENGTH: {len(bitsList)}")
      print(chunkList)
  
    '''
    binaryList = list(map(self.byteToInt, chunkList))
    print(binaryList)

    # If data is correct
    if len(data) >= 40 and sum(binaryList[:4]) == binaryList[4]:
      print(binaryList[:-1])
    '''