from wizardlib import *

########## FUNCTION DEFINITIONS ###############
def count_clicks():
    global num_clicks
    num_clicks += 1
    update_text(num_clicks_text, f"Num clicks: {num_clicks}")

def end_game():
    global num_clicks
    clear()
    clicks_per_second = num_clicks / time
    if clicks_per_second > 3:
        win_text = add_text(f"Congratulations! You got a CPS of {clicks_per_second} clicks per second!", 20)
        position_element(win_text, "center", 150)
        win_image = add_image("win.jpg", 200)
        position_element(win_image, "center", 250)        
    if clicks_per_second < 3:
        lose_text = add_text(f"You got a CPS of {clicks_per_second} clicks per second. Try again and get a clicking speed above 3!", 20)
        position_element(lose_text, "center", 150)
        lose_image = add_image("lose.jpg", 200)
        position_element(lose_image, "center", 250)


########### STARTER CODE ######################

add_background("bg.png")

title_text = add_text("Pizza Clicker", 60)
position_element(title_text, "center", 130)

time = 5

time_text = add_text(f"You have {time} seconds to get as many clicks as you can!", 20)
position_element(time_text, "center", 210)

description_text = add_text("You win a pizza if you average over 3 clicks per second", 20)
position_element(description_text, "center", 250)

num_clicks = 0

num_clicks_text = add_text(f"Num clicks: {num_clicks}")
position_element(num_clicks_text, "center", 500)

pizza = add_image("pizza.png", 200)
position_element(pizza, "center", 300)
###############################################

click(pizza, count_clicks)
set_timeout(end_game, 5)



    
