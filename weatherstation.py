from modules.dht11 import DHT11

# Import sleep library
from time import sleep

dht11 = DHT11(17)

while True:
	dht11.read()
	sleep(0.02)