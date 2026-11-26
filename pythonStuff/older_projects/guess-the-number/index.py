from random import randint

keep_looping = True
attempt_num = 0
random_number = randint(1,100)

first_try = r"""
Wow! You got it on your first try! Take this pass as a reward! You will now have access to unlimited access to E-Books when shown to the librarian.

IIIIIIIIIIIII| |IIIIIIIIIIIIIIIII| |IIIIIIIIIIIII
|_|___|___|__| |__|___|___|___|__| |__|___|___|_|
|___|___|___|| ||___|___|___|___|| ||___|___|___|
|_|       |__| |__|           |__| |__|       |_|
|_|_______|_|| ||_|___________|_|| ||_|_______|_|
|_|___|___|__| |__|___|___|___|__| |__|___|___|_|
|___|___|___|| ||___|___|___|___|| ||___|___|___|
|_|___|___|__| |_Public_Library__| |__|___|___|_|
|___|___|___|| ||___|___|___|___|| ||___|___|___|
|_|       |__| |__|___|___|___|__| |__|  ScS  |_|
|_|_______|_|| ||___|   |   |___|| ||_|_______|_|
|_|___|___|__| |__@ |   |   |_@__| |__|___|___|_|
|___|_/^\___|| ||___|  揉`  |___|| ||___/^\_|___|
|_|__<===>|__|_|__|_|   |   |_|__|_|__|<===>__|_|
     ][o][  |_______|___|___|_______|  ][o][
     <===>          |       |          <===>
______\T/________,_,|,_,o,_,|,_,________\T/______
|L_L_L_L_L_L_L_L_|"|"|"|y|"|"|"|_L_L_L_L_L_L_L_L|
|_L_L_L_L_L_L_L_L| | | |y| | | |L_L_L_L_L_L_L_L_|
|L_L_L_L_L_L_L_L_|_|_|_|y|_|_|_|_L_L_L_L_L_L_L_L|

"""

while keep_looping:
    attempt_num += 1
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess == random_number and attempt_num == 1:
        print(first_try)
        keep_looping = False
    elif user_guess > 100 or user_guess < 0:
        print("That is invalid. Please try again.")
        attempt_num -= 1
    elif user_guess == random_number:
        print(f"You guessed the number exactly!\nYou took {attempt_num} attempts to get the right answer.")
        keep_looping = False
    elif user_guess > random_number:
        print("A bit too high...")
    elif user_guess < random_number: 
        print("A bit too low...")
    
        