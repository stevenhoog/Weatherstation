from modules.dht11 import DHT11
import DHT11Generator

# Import sleep library
from time import sleep

testData = [40, 0, 18, 3]

dht11 = DHT11(17)

while True:
    # Create test data
    generatedData = DHT11Generator.CreateData(testData)

    # Pass data to dht11 parse function
    result = dht11.ParseData(generatedData)

    # Check if parser past test
    if result == testData:
        print("CORRECT")
    else:
        # Otherwise try again
        print("DID NOT WORK")

    sleep(2)
