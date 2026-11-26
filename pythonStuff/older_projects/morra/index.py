from random import choice
########################## BEGIN FUNCTION DEFINITIONS ######################


########################## END FUNCTION DEFINITIONS ######################


game_rules = """
    Welcome to Morra! In this game, you'll decide how many fingers
    to hold up (from one hand) and then the computer will randomly
    do the same. You'll need to guess the total number of fingers
    to win the round, before seeing how many fingers the computer
    has decided to hold up!
"""
print(game_rules)

player_wins = 0
computer_wins = 0

number_of_fingers_held = [
    1,
    2,
    3,
    4,
    5
]

username = input("Enter your name: ")
rounds_to_play = input("How many rounds do you want to play for?\n-> ")
rounds_to_play += 1

for i in range(1, rounds_to_play):
    print(f"\nRound {i}\n")
    computer_fingers = choice(number_of_fingers_held)
    fingers_held = int(input("How many fingers do you want to hold up? (Up to 5)\n-> "))
    if fingers_held not in number_of_fingers_held:
        print(f"{fingers_held} is an invalid number of fingers! The computer gets a point!")
        computer_wins += 1
        continue
    total_fingers_held = fingers_held + computer_fingers
    user_finger_guess = input("Now guess how many fingers are there combined with the computer's!\n-> ")
    if user_finger_guess == total_fingers_held:
        print(f"That is correct! {total_fingers_held} were held up! {username} wins this round!")
        player_wins += 1
    elif user_finger_guess != total_fingers_held:
        print(f"That is incorrect, {total_fingers_held} fingers were held up. The computer wins this round!")
        computer_wins += 1
        
end_game = f"""
GAME END

{username}'s wins: {player_wins}
Computer's wins: {computer_wins}

"""
print(end_game)
if player_wins > computer_wins:
    print(f"{username} won the game!")
elif computer_wins > player_wins:
    print("The computer won the game!")
elif computer_wins == player_wins:
    print("Nobody won, it's a tie!")