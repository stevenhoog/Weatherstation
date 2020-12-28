import Adafruit_DHT
import time

# GPIO port
port = 17
count = 0

while True:
  count = time.perf_counter()

  humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, port)

  humidity = round(humidity, 2)
  temperature = round(temperature, 2)

  print(time.perf_counter()-count)

  if humidity is not None and temperature is not None:

    print('Temperatuur: {0:0.1f}*C'.format(temperature))
    print('Luchtvochtigheid: {0:0.1f}%'.format(humidity))

  else:

    print('Geen data ontvangen')
