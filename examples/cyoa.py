# examples/cyoa.py
#
# Choose your own adventure game engine
#
# Story files in configuration/cyoa/*.py
# Use the main cyoa config file to select which story to use.
#
# Usage
# ~~~~~
# # mpfs [/]> put examples/cyoa.py 
# # mpfs [/]> put configuration/cyoa.py
# # mpfs [/]> put examples/configuration/cyoa_your_story_file.py
# mpfs [/]> repl
# MicroPython v1.13 on 2020-09-02; ESP32 module with ESP32
# Type "help()" for more information.
# >>> import examples.cyoa as cyoa
# >>> from examples.cyoa import run
# >>> run()
#
import uos
import os
import utime
import aiko.event as event
import aiko.oled as oled
import aiko.common as common
from machine import Pin

import configuration.cyoa

current_story_node = None
game = None
lock = None
selected = None
scrollerpos = 1

buttonR = Pin(17, Pin.IN, Pin.PULL_UP)
buttonL = Pin(16, Pin.IN, Pin.PULL_UP)
downL = 12
upL = 15
downR = 14
upR = 27

def random(min, max, r_max=255):
    r = uos.urandom(1)[0] & r_max
    r = r / r_max * (max - min) + min
    if r >= max:
        r = min
    return int(r)


def timer_handler():
    # Detect restart handling (button push?)
    # Detect switch status and set values for reading.
    # If switch status changes, trigger next node, update pointer
    global current_story_node, game, lock
    if lock == 1:
        return

    # top left slider = restart
    if common.touch_pins_check([upL]):
        oled.oleds_clear(0)
        new_game()
        return
    # top right slider = abort
    if common.touch_pins_check([upR]):
        oled.oleds_clear(0)
        end_game()
        return
        
    lock=1
    
    pressed=None
    # bottom left slider is pin 12, bottom right slider is pin 14
    if common.touch_pins_check([downL]):
        pressed=0
    if common.touch_pins_check([downR]):
        pressed=1
    if pressed is None:
        lock=None
        return
    if pressed >= len(current_story_node["choices"]):
        lock=None
        return
    new_node_name=current_story_node["choices"][pressed][1]
    new_node = game.story[new_node_name]
#    oled.log("You chose "+current_story_node["choices"][pressed][0])
    current_story_node=new_node
    render_node(current_story_node)
    utime.sleep(5)
    lock=None
    

def new_game():
    global current_story_node
    global game
    print("Game name: "+game.story["name"])
    oled.log("Game: "+game.story["name"])
    current_story_node = game.story['start']
    # Find start node and render it, then finish, record pointer to current place in story.
    render_node(current_story_node)

def end_game():
    oled.log("The end!")
    event.remove_timer_handler(timer_handler)
    event.terminate()

# Modified rom https://www.codespeedy.com/solve-word-wrap-problem-in-python/
# Takes a string and a width and returns an array of string portions nicely broken on 
# word borders.
def word_wrapper(string, width):
    new_string=[]
    while len(string)>width:
        #find the position of nearest whitespace char to left of "width"
        index=width-1
        #check the char in the index of string of given width
        #if it is space then continue
        #else reduce the index to check for the space.
        while not string[index].isspace():
            index=index-1
        #remove the line from original string and add it to the new string
        line=string[0:index]
        new_string.append(line) #add those line to new_string variable
        string=''+string[index+1:]#updating the string to the remaining words
    #finally string will be left with less than the width.
    #adding those to the output
    new_string.append(string)
    return new_string
    
def render_node(node):
    # work out what type it is, print stuff to oleds
    width=2* int(oled.oleds[0].width / oled.font_size)
    lines = word_wrapper(node['text'],width)
    for line in lines:
        oled.log(line)
    
    if (node["type"] == "end"):
        end_game()
        return

    # other node types: start, or text
    i=0
    slider=["L","R"]
    for choice in node["choices"]:
        oled.log(slider[i]+" "+choice[0])
        i = i+1

def get_game_list():
    gamelist = []
    files = os.listdir("examples/configuration")
    for f in files:
        if f.lower().startswith("cyoa_"):
            gamelist.append(f[:-3])
    return gamelist

# Display the items in a menu, highlighting the currently selected one      
def draw_menu(items):
    global scrollerpos
    i = 1

    oled.oleds_clear(oled.bg)
    bg = oled.bg
    fg = oled.fg
    
    oled.oleds_text("Choose your adventure:",0,10*i,fg)
    for item in items:
        if i==scrollerpos:
            oled.oleds[0].fill_rect(0, 11*(i+1), 2*oled.font_size, oled.font_size, fg)
            oled.oleds_text(" >",0,11*(i+1), bg)
            oled.oleds_text(item, 2*oled.font_size, 11*(i+1), fg)
        else:
            for oleder in oled.oleds:
                oleder.fill_rect(0, 11*(i+1), oleder.width-10, oled.font_size, bg)
            oled.oleds_text("  "+item, 0, 11*(i+1), fg)
        i=i+1
    oled.oleds_text("Push screen to select",0,11*(i+1), fg)
    oled.oleds_show()

# Use the slider buttons to move up and down in the list
# Use either screen button to confirm the choice
# 12 and 14 is down, 15 and 27 is up
# screen buttons are 16 and 17
def menu_handler():
    global selected, scrollerpos, menu
    # If button is pushed
    #    remove this handler
    #    set menu selection global
    #    reset selected to none
    if not(buttonL.value()) or not(buttonR.value()):
        selected = menu[scrollerpos-1]
        scrollerpos = None
        event.terminate()
        return
    # If up/down is pressed, move up/down (and wrap to start/end)
    #    this means move the selected pointer (Global) up/down
    #    and redraw menu
    if common.touch_pins_check([downL]) or common.touch_pins_check([downR]):
        scrollerpos = scrollerpos +1
        if (scrollerpos > len(menu)):
            scrollerpos = 1
        draw_menu(menu)
    if common.touch_pins_check([upL]) or common.touch_pins_check([upR]):
        scrollerpos = scrollerpos-1
        if (scrollerpos < 1):
            scrollerpos = len(menu)
        draw_menu(menu)
    else:
        # If nothing is pressed, do nothing
        return
    
def run():
    global game, menu
    
    oled.title = "CYOA 0.0"
    oled.oleds_clear(0)
    
    gamelist = get_game_list()
    if gamelist == []:
        print("No games found.")
        oled.log("No games found.")
        return
        
    menu = gamelist
    draw_menu(gamelist)
    event.add_timer_handler(menu_handler,500)
    try:
        event.loop()
    finally:
        event.remove_timer_handler(menu_handler)
    
    print("Selected: "+selected)    
    # Read config file, find story name (error)
    # Trim the .py off the filename
    storyname = selected
    print("CYOA game file: "+storyname)
    game = __import__("examples.configuration."+storyname, globals(), locals(), [storyname],0)
    # Load story config (error)
    new_game()

    event.add_timer_handler(timer_handler,1000)
    try:
        event.loop()
    finally:
        event.remove_timer_handler(timer_handler)
