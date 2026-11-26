"""
############## HINTS ###########################

Don't forget to import wizardlib!

You'll need to:
    - Add a background image
    - Add and position an image of Mars
    - Add and position some title text (can also change the color if you wish)
    - Add and position at least 3 facts about Mars
        - You can pull these from mars-facts.txt if you wish

################################################
"""

from wizardlib import *

add_background("space.jpg")

mars = add_image("mars.png", 250)

position_element(mars, "right", 0)

title = add_text("Mars Trivia!", 50)

position_element(title, "center", 70)

set_text_color(title, "#ffcccb")

fact_1 = add_text("1. Mars and Earth have approximately the same landmass.", 24)

position_element(fact_1, "center", 300)

set_text_color(fact_1, "#ffcccb")

fact_2 = add_text("2. Pieces of Mars have fallen to Earth.", 24)

position_element(fact_2, "center", 500)

set_text_color(fact_2, "#ffcccb")

fact_3 = add_text("3. There are signs of liquid water on Mars.", 24)

position_element(fact_3, "center", 700)

set_text_color(fact_3, "#ffcccb")
