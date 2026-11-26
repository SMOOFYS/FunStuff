from wizardlib import *
from random import randint 


def check_guess():
    guess = int(input("Take a guess: "))
    if guess == random_number:
        add_text("Good job! You got it!")
        win_img = add_image("win.jpg")
        position_element(win_img, "center", 500)
    else:
        add_text("sorry, that's incorrect!")
        lose_img = add_image("lose.jpg")
        position_element(lose_img, "center", 500)



guess_button = add_button("Take A Guess")
position_element(guess_button, "center", 75)

click(guess_button, check_guess)


add_background("bg.png")

random_number = randint(1, 10)


guess_text = add_text("Guess a number between 1 and 10")
position_element(guess_text, "center", 50)


