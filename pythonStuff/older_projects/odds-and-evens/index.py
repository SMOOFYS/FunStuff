from random import randint
welcome_banner = """
                Welcome to Odds and Evens!

    This game simulates a hand game between two 
    players. Each player holds up a hidden amount
    of fingers on one hand. One player chooses 
    whether the sum will be "odd" or "even". Then,
    each player shows their hand, and you take the
    total of the number of fingers and see who wins.

    For example, if player 1 chooses "odd" and the
    sum of the fingers is 4, player1 loses.
"""

print(welcome_banner)

player_name = input("Enter your name:  ")

while(True):
    num_player_fingers = int(input("Amount of fingers you want to hold up: "))
    num_computer_fingers = int(randint(1, 5))
    if num_player_fingers >= 1 and num_player_fingers <= 5:
        break
    if num_player_fingers < 1 or num_player_fingers > 5:
        print("That input is invalid. Please try again.")
        

player_choice = input("Odd or even?\n-> ")
   
if player_choice not in ["odd", "Odd"] and player_choice not in ["even", "Even"]:
    print("Invalid choice")
    player_choice = "odd"
    
sum_fingers = num_computer_fingers+num_player_fingers

print(f"Amount of fingers computer chose: {num_computer_fingers}\nThe total sum of fingers held up: {sum_fingers}")
if sum_fingers % 2 == 0 and player_choice == "even":
    print(f"{player_name} wins!")
elif sum_fingers % 2 != 0 and player_choice == "odd":
    print(f"{player_name} wins!")
else:
    print("The computer wins!")









