from time import sleep
import RPi.GPIO as GPIO

data = [0, 0, 0, 0, 0]
MAX_TIMINGS = 85


def Read(port):
    laststate = 1  # HIGH
    counter = 0
    j = 0
    i = 0

    data = [0, 0, 0, 0, 0]

    # ---------- Reading ------------------------

    GPIO.setmode(GPIO.BCM)

    #  pull pin down for 18 milliseconds
    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.LOW)
    sleep(0.018)

    # prepare to read the pin
    GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # detect change and read data
    for i in range(MAX_TIMINGS):

        counter = 0

        while GPIO.input(port) == laststate:

            counter += 1
            sleep(0.01)

            if counter == 255:
                break

        laststate = GPIO.input(port)

        if counter == 255:
            break

    # ---------- Parsing ------------------------

    # ignore first 3 transitions
    if ((i >= 4) and (i % 2 == 0)):

        # shove each bit into the storage bytes
        data[j / 8] <<= 1

        if (counter > 16):
            data[j / 8] |= 1

        j += 1

    if ((j >= 40) and (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))):

        h = (float)((data[0] << 8) + data[1]) / 10

        if h > 100:
            h = data[0]

        c = (float)(((data[2] & 0x7F) << 8) + data[3]) / 10

        if c > 125:
            c = data[2]

        if data[2] & 0x80:
            c = -c

        f = c * 1.8 + 32

        print(f"Humidity = %.1f %% Temperature = %.1f *C (%.1f *F)\n", h, c, f)
    else:
        print("Data not good, skip")


while True:
    Read(17)

    # wait 2 seconds before next read
    sleep(2)
