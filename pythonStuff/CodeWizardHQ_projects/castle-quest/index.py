from wizardlib import *

######## DEFINE FUNCTIONS BELOW ###################
def hit_wall():
    global health
    health -= 25
    position_element(knight, start_x, start_y)
    update_text(health_text, f"Health: {health}")
    if health == 0:
        clear()
        lose_text = add_text("Nice try. Try again to reach the castle!", 35)
        position_element(lose_text, "center", 170)
        play_audio(lose_audio)
    
    
def win_condition():
    clear()
    if health == 100:
        win_text = add_text("Good job! You touched the castle without getting hit!", 35)
        position_element(win_text, "center", 170)
    elif health < 100:
        win_text2 = add_text("Good job, you won! Now try getting a run with no hits now!", 35)
        position_element(win_text2, "center", 170)
    play_audio(win_audio)
        
def lose_condition():
    clear()
    lose_text = add_text("Nice try. Try again to reach the castle!", 35)
    position_element(lose_text, "center", 170)
    play_audio(lose_audio)
    
        
def check_key(key):
    if key == "w":
        move_up(knight, 10)
    elif key == "a":
        move_left(knight, 10)
    elif key == "s":
        move_down(knight, 10)
    elif key == "d":
        move_right(knight, 10)

def add_wall(x, y, make_vertical):
    boundary = add_image("wall.png", 145)
    position_element(boundary, x, y)    
    if make_vertical:
        rotate_element(boundary, 90)
    check_collision(boundary, knight, hit_wall)
    
def add_ghost(x, y, animate_vertical):
    ghost = add_image("ghost.png", 75)
    position_element(ghost, x, y)
    if animate_vertical:
        animate_down(ghost, 65, 1.5, True)
    else:
        animate_right(ghost, 65, 1.5, True)
    check_collision(ghost, knight, lose_condition)
################ STARTER CODE ######################

add_background("background.png")

title_text = add_text("Castle Quest", 64)
position_element(title_text, "center", 0)

castle = add_image("castle.png", 400)
position_element(castle, "right", 200)

mountains = add_image("mountains.png", 500)
position_element(mountains, -100, 600)

health = 100
health_text = add_text(f"Health: {health}", 42)
position_element(health_text, 100, 100)

knight = add_image("knight.png", 50)
start_x = 200
start_y = 500
position_element(knight, start_x, start_y)

####################################################

keydown(check_key)
# horizontal walls
add_wall(135, 175, False)
add_wall(275, 175, False)
add_wall(415, 175, False)
add_wall(555, 175, False)
# vertical walls
add_wall(80, 255, True)
add_wall(80, 390, True)
add_wall(340, 395, True)
add_wall(80, 530, True)
add_wall(340, 530, True)
add_wall(80, 670, True)
add_wall(340, 670, True)
add_wall(615, 255, True)
add_wall(615, 390, True)

add_ghost(230, 350, False)
add_ghost(500, 350, False)
add_ghost(650, 540, True)

check_collision(castle, knight, win_condition)
win_audio = add_audio("win.mp3")
lose_audio = add_audio("lose.mp3")

