from gpiozero import LED, Button
from subprocess import call

button = Button(2)
def print_thing():
    print ("button pressed")

button.when_pressed = print_thing