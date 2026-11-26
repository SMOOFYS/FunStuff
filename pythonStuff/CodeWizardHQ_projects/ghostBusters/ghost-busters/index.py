from wizardlib import *


############ FUNCTION DEFINITIONS UP HERE ###############


    
def remove_ghost(ghost):
    global ghosts_caught
    ghosts_caught += 1
    update_text(caught_text, f"Ghosts caught: {ghosts_caught}")
    vanish(ghost)
    if ghosts_caught == 6:
        win_text = add_text("Good job! you got all 6 ghosts!", 50)
        position_element(win_text, "center", 250)
    
def add_ghost(x, y, time):
    ghost = add_image("ghost.png", 100)
    click(ghost, remove_ghost)
    position_element(ghost, x, y)
    animate_up(ghost, y + 200, time)

#########################################################

add_ghost(300, 600, 5)
add_ghost(500, 700, 6)
add_ghost(700, 550, 8)
add_ghost(900, 800, 4)
add_ghost(1100, 570, 7)
add_ghost(1300, 900, 3)

########### STARTER CODE ##################################

add_background("ghost-background.jpg")

ghosts_caught = 0

caught_text = add_text(f"Ghosts caught: {ghosts_caught}")
position_element(caught_text, 350, 100)



###########################################################
