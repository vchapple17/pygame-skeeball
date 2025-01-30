# import RPi.GPIO as GPIO
from gpiozero import LED

from time import sleep

led = LED("GPIO17") # or just 17

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
