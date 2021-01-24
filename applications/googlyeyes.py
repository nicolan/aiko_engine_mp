# Great googly moogly
#
# Put up some woogly boogly googly eyes on the screens and use the sliders/buttons to wiggle them.

import aiko.mqtt as mqtt
from machine import Pin, TouchPad
import aiko.event as event
import aiko.oled as oled
import aiko.mqtt as mqtt
import aiko.common as common
from aiko.common import map_value
import aiko.button as button


titles = ["SwagBadge", "LCA2021", "Googly Eyes"]
title_index = 0

iris, eye = None, None

# sliders
bottom_left = 12
top_left = 15
bottom_right = 14
top_right = 27

# Buttons on screens
button_left = 16
button_right = 17

eye_size=10

currentpos = [50,20]

# Display a rotating title
def titlebar():
    global title_index
    oled.set_title(titles[title_index])
    oled.write_title()
    title_index = (title_index + 1) % len(titles)

def draw_eyes(x=50,y=20):
    global eye_size
    oled.oleds[0].blit(eye,0,0)
    oled.oleds[0].blit(iris,x,y)
    oled.oleds[1].blit(eye,0,0)
    oled.oleds[1].blit(iris,x,y)
    oled.oleds_show() 
#    for deltax in range(eye_size):
#        for deltay in range(eye_size):
#            oled.oleds[0].pixel(x+deltax, y+deltay, oled.BG)
#            oled.oleds[1].pixel(x+deltax, y+deltay, oled.BG)
            # print("drawing at "+str(x+deltax)+", "+str(y+deltay))
    

def wink_handler(pin_number, state):
#    print("Button {}: {}".format(pin_number, "press" if state else "release"))

    screen = None
    if pin_number == button_left: screen = oled.oleds[0]
    if pin_number == button_right: screen = oled.oleds[1]

    if screen == None: return
    
    if state:
        screen.fill(oled.BG)
        screen.fill_rect(32, 24, 64, 8, oled.FG)
        screen.show()
    else:
        draw_eyes(currentpos[0],currentpos[1])
      
def googly_handler(pin_number, state, value):

    # if value is None: return
    if state == 0: return
    if value == None: return
    
#    print("Slider {}: {} {}".format(pin_number, state, value))

    x = currentpos[0]
    y = currentpos[1]
    if pin_number == bottom_left or pin_number == top_left: 
        x = int(map_value(value, 0, 100, 35,60))
    elif pin_number == bottom_right or pin_number == top_right: 
        y = int(map_value(value, 0, 100, 30,55))
        y = 64-y
#    print("Drawing eyes at {},{}".format(x,y))
    currentpos[0] = x
    currentpos[1] = y
    draw_eyes(x, y)
        
def initialise():
    global iris, eye
    iris = oled.load_image("/applications/googlyeye/iris.pbm")  
    eye = oled.load_image("/applications/googlyeye/eyeball.pbm")

    oled.show_title = False
    oled.oleds_clear(oled.BG)
    button.initialise(poll_rate=1000) 
    draw_eyes()
#    event.add_timer_handler(titlebar, 5000)    
    
    
    button.add_button_handler(wink_handler, [button_left, button_right])
    
    button.add_slider_handler(googly_handler, bottom_left, top_left)
    button.add_slider_handler(googly_handler, bottom_right, top_right)    
