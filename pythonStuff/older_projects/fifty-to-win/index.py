from random import randint
###########FUNCTION_DEFINITIONS#############
def display_welcome_banner():
    welcome_banner = """
            Welcome to Fifty To Win!

This is a dice game between two players, the user
and a computer opponent. The game is played in rounds. 

In each round: 

- Each player rolls two dice.

- If the parity of the sum of the roll and the round
number is the same, the player gets the sum of the
roll added to their points. 

- The game continues until a player reaches 50 or more points. 

- If both players reach 50 or more points in the same round and
have the same score, then the game is a tie.

Note: Parity is whether a number is even or odd.
"""
    print(welcome_banner)
    
def roll_dice():
    return randint(2,12)

def is_even(number):    
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0
    
def has_parity_match(player_roll, round_number):
    if is_even(user_roll) and is_even(round_num):
        return True
    elif is_odd(user_roll) and is_odd(round_num):
        return True
    else:
        return False

def display_scoreboard(user_score, computer_score, round_num):
    print(f"""
    USER_SC0RE: {user_score}
    C0MPUTER_SCORE: {computer_score}
    R0UND_NUM: {round_num}
    """)
    
def display_round_stats(round_number, user_name, user_roll, computer_roll):
    return f"""
    Round {round_number}
    {user_name} rolled a {user_roll}.
    Computer rolled a {computer_roll}.
    
    """
    
def display_game_results(user_name, user_score, computer_score):
    if user_score >= 50:
        print(f"{user_name} wins the game!")
        keep_looping = input("Want to play again? (y/n)\n-> ")
        if keep_looping in ["y", "Y"]:
            return False
        else:
            return True
    if computer_score >= 50:
        print("Computer wins the game!")
        keep_looping = input("Want to play again? (y/n)\n-> ")
        if keep_looping in ["y", "Y"]:
            return False
        else:
            return True
###########################################
display_welcome_banner()
#################VARIABLES#################
user_score = 0
computer_score = 0
round_num = 0
keep_looping = True
still_playing = True
user_name = input("What is your name?\n")
###########################################

while True:
    input("Roll the dice (Press Enter): ")
    round_num += 1
    user_roll = roll_dice()
    computer_roll = roll_dice()
    
    display_round_stats(round_num, user_name, user_roll, computer_roll)
    
    if has_parity_match(user_roll,round_num):
        user_score += user_roll
        print(f"{user_name} gets {user_roll} added to their points!")
    if has_parity_match(computer_roll,round_num):
        computer_score += computer_roll
        print(f"Computer gets {computer_roll} added to their points!")
        
    display_scoreboard(user_score, computer_score, round_num)
        
    game_result = display_game_results(user_name, user_score, computer_score)
    if game_result:
        break

        
    
    
    
