from wizardlib import *

add_background("space.jpg")

moon = add_image("moon.png", 250)
# 1750 horizontally
position_element(moon, "right", 0)

Title = add_text("Moon Trivia!", 50)

position_element(Title, "center", 70)

set_text_color(Title, "palevioletred")

Fact_1 = add_text(
    "1. The Moon is Earth's only permanent natural satellite.", 24)

set_text_color(Fact_1, "white")

position_element(Fact_1, 'center', 300)

Fact_2 = add_text(
    "2. There is water on the Moon!", 24)

set_text_color(Fact_2, "white")

position_element(Fact_2, 'center', 500)

Fact_3 = add_text(
    "3. The Moon was made when a rock smashed into Earth.", 24)

set_text_color(Fact_3, "white")

position_element(Fact_3, 'center', 700)

