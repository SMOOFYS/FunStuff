from wizardlib import *
"""
###################### HINTS #########################

Make sure to import wizardlib

You'll need two functions:
    - remove_balloon(balloon)
    - add_balloon(x, y)


######################################################
"""
def remove_balloon(balloon):
    global caught_balloon
    vanish(balloon)
    caught_balloon += 1
    update_text(caught_balloon_text, f"Balloons caught: {caught_balloon}")
    
# Just an idea that wasn't working: def add_balloon(x, y, time, time_left, time_right): 

def add_balloon(x, y, time):
    balloon = add_image("balloon.png", 105)
    click(balloon, remove_balloon)
    position_element(balloon, x , y)
    animate_up(balloon, y + 255, time)
    # Just an idea that wasnt working: animate_left(balloon, x-15, time_left)
    # Just an idea that wasnt working: animate_right(balloon, x+30, time_right)

      
    
caught_balloon = 0

# Just an idea that wasnt working:add_balloon(300, 600, 5, 1, 2)
# Just an idea that wasnt working:add_balloon(500, 700, 6, 1, 2)
# Just an idea that wasnt working:add_balloon(700, 550, 8, 1, 2)
# Just an idea that wasnt working:add_balloon(900, 800, 4, 1, 2)
# Just an idea that wasnt working:add_balloon(1100, 570, 7, 1, 2)
# Just an idea that wasnt working:add_balloon(1300, 900, 3, 1, 2)


add_balloon(300, 600, 5)
add_balloon(500, 700, 6)
add_balloon(700, 550, 8)
add_balloon(900, 800, 4)
add_balloon(1100, 570, 7)
add_balloon(1300, 900, 3)


add_background("balloon-background.jpg")
caught_balloon_text = add_text(f"Balloons caught: {caught_balloon}", 20)
position_element(caught_balloon_text, 350, 100)






