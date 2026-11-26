"""
######################### HINTS ####################################

Don't forget to import wizardlib!

Your app should:
    - Add a background image
    - Choose a word that the user should guess and store it in a variable
    - Add and position some text giving the user a hint about the word
    - Add a button the user can press to guess the word
    - When the button is clicked, you should run a function
        - This function should:
            - Ask the user for their guess
            - Clear the page
            - Check if the guess is correct
                - If correct, show and position a win message and win image
                - If incorrect, show and position a lose message and lose image

####################################################################
"""
from wizardlib import * 

def check_guess():
    guess = str(input("Take a guess: "))
    # You can add .lower to the function to force it to compare to always a lowercase, forcing answers to always start with a lowercase
    if guess.lower == "function":
        add_text("Good job! You got it!")
        win_img = add_image("win.jpg")
        position_element(win_img, "center", 500)
    else:
        lose_txt = add_text("sorry, that's incorrect!")
        lose_img = add_image("lose.jpg")
        position_element(lose_img, "center", 500)



guess_button = add_button("Take A Guess")
position_element(guess_button, "center", 75)

click(guess_button, check_guess)


add_background("bg.png")

random_word = "function" 
random_word = "Function"


guess_text = add_text("Guess a word: furple, schism, plane, or function *hint: It's related to math!")
position_element(guess_text, "center", 50)