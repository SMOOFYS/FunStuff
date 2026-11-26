from random import randint
keep_looping = True  
attempt = 1
random_number = randint(1,3)
while keep_looping:
    if random_number == 1:
        user_guess = str(input("What word rhymes with mango?\n-> "))
        if user_guess == "tango" or user_guess == "Tango" and attempt == 1:
            print("Wow! You got that first try! Great job!")
            keep_looping = False
        elif attempt == 3 and user_guess is not ["tango", "Tango"]:
            print("Hint: The word is a ballroom dance.\n-> ")
            attempt += 1
        elif user_guess in ["tango", "Tango"]:     
            print(f"Good job! You got that in {attempt} rounds.")
            keep_looping = False
        elif user_guess not in ["tango", "Tango"]:
            print("That was the wrong answer. Try again")
            attempt += 1
    if random_number == 2:
        user_guess = str(input("What word rhymes with chair?\n-> "))
        if user_guess == "bear" or user_guess == "Bear" and attempt == 1: 
            print("Wow! You got that first try! Great job!")
            keep_looping = False
        elif attempt == 3 and user_guess is not ["bear", "Bear"]:
            print("Hint: The word is a furry animal known to be big and have 8 species in the entire world.\n-> ")
            attempt += 1
        elif user_guess in ["bear", "Bear"]:     
            print(f"Good job! You got that in {attempt} rounds.")
            keep_looping = False
        elif user_guess not in ["bear", "Bear"]:
            print("That was the wrong answer. Try again")
            attempt += 1
    if random_number == 3:
        user_guess = str(input("what word rhymes with care?\n-> "))
        if user_guess == "dare" or user_guess == "Dare" and attempt == 1:
            print("Wow! You got that first try! Great job!")
            keep_looping = False
        elif attempt == 3 and user_guess is not ["dare", "Dare"]:
            print("Hint: The word is a physical challenge given to someone.\n-> ")
            attempt += 1
        elif user_guess in ["dare", "Dare"]:     
            print(f"Good job! You got that in {attempt} rounds.")
            keep_looping = False
        elif user_guess not in ["dare", "Dare"]:
            print("That was the wrong answer. Try again")
            attempt += 1
        