from gpiozero import Button
from time import sleep

button = Button(4)

while True:
    if button.is_pressed:
        print("HIGH")
    else:
        print("LOW")
    sleep(1)
