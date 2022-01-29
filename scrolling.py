#!/usr/local/bin/python3
import math
from time import sleep
from pynput.mouse import Controller, Button, Listener
import threading

mouse = Controller()
running = False

def scroll():

    start_x, start_y = mouse.position

    while running:

        new_x, new_y = mouse.position
        distance_y = abs(start_y - new_y)
        distance_x = abs(start_x - new_x)

        sleep(0.01)
        if new_y < start_y:
            mouse.scroll(0, math.ceil(distance_y / 50))
        elif new_y > start_y:
            mouse.scroll(0, - math.ceil(distance_y / 50))  

        if new_x < start_x:
            mouse.scroll(math.ceil(distance_x / 50), 0)
        elif new_y > start_y:
            mouse.scroll(- math.ceil(distance_x / 50), - math.ceil(distance_x / 50))      

def on_click(x, y, button, pressed):
    global running # to assing value to global variable (instead of local variable)
    
    if button == Button.middle: 
        if pressed:
            running = True
            threading.Thread(target=scroll).start()
        else:
            running = False

with Listener(
        on_click=on_click) as listener:
    listener.join()