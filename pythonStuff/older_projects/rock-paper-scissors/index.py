from random import choice
########################## BEGIN FUNCTION DEFINITIONS ######################
def display_choices(player_choice, computer_choice):
    print(f"{username} chose {options[player_choice]}!")
    print(f"Computer chose {options[computer_choice]}!")

def round_win(player_choice, computer_choice):
    global options
    if (
        player_choice == "rock" and computer_choice == "scissors" or
        player_choice == "paper" and computer_choice == "rock" or 
        player_choice == "scissors" and computer_choice == "paper"

    ):
        return "Player"
    elif player_choice == computer_choice:
        return 
    elif (
        computer_choice == "rock" and player_choice == "scissors" or
        computer_choice == "paper" and player_choice == "rock" or 
        computer_choice == "scissors" and player_choice == "paper"
    ):
        return "The Computer"
    elif player_choice not in options:
        return "Try again."
    
def add_win():
    global match_winner
    global player_wins
    global pc_wins
    if match_winner == "Player":
        player_wins += 1
    elif match_winner == "The Computer":
        pc_wins += 1

def display_game_winner():
    global player_wins
    global pc_wins
    if player_wins > pc_wins:
        print(f"{username} won the series!")
    elif pc_wins > player_wins:
        print("The Computer has won the series!")
    else:
        print("It was a tie! Nobody won the series!")
  
def display_scoreboard(plyr_wins, comp_wins, NUMBER_TIES, GAMES_PLAYED):
    return f"""
    PLAYER_WINS: {plyr_wins}
    C0MPUTER_WINS: {comp_wins}
    NUM_TIES: {NUMBER_TIES}
    NUM_GAMES_PLAYED: {GAMES_PLAYED}
    """
    
        
########################## END FUNCTION DEFINITIONS ################
welcome = """
Welcome to Rock, paper, scissors.

How to play:
Choose one of the three options, rock, paper, and scissors.

Rock beats scissors,
scissors beats paper,
and paper beats rock.

Choose one and if your choice beats the robot's choice, you win!
"""

options = {
    "rock": "🤘🏻",
    "paper": "📝",
    "scissors": "✂️"
}

print(welcome + "\n")
username = input("Enter your name: ")
print("Choose:")
for valid_choice, emoji in options.items():
    print(valid_choice + emoji)
    

game_loop = True
player_wins = 0
pc_wins = 0
NUM_TIES = 0
Num_rounds = 0
Player_acssi = fr"""
 {username} wins the round!
        
   .------\ /------.
   |       -       |
   |               |
   |               |
   |               |
_______________________
===========.===========
  / ~~~~~     ~~~~~ \
 /|     |     |\
 W   ---  / \  ---   W
 \.      |o o|      ./
  |                 |
  \    #########    /
   \  ## ----- ##  /
    \##         ##/
     \_____v_____/
        """
pc_acssi = r"""
The computer wins the round!             
    
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \                             | 
|     /  %%%%%%%%%%%%%%  \                            | 
|     ^^^^^^^^^^^^^^^^^^^^                            | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        """
while game_loop:
    Num_rounds += 1
    plyr_choice = input("\n").lower().strip()
    pc_choice = choice(options.keys())
    display_choices(plyr_choice, pc_choice)
    match_winner = round_win(plyr_choice, pc_choice)
    
    if match_winner == 'Player':
        if plyr_choice == "rock":
            print("Rock crushes scissors!")
        elif plyr_choice == "paper":
            print("Paper covers rock!")
        elif plyr_choice == "scissors":
            print("Scissors cut paper!")
        print(Player_acssi)
    elif match_winner == 'The Computer':
        print(pc_acssi)
    elif match_winner == "Try again.":
        print("That was an invalid choice. Try again!")
    else:
        print("It's a Tie!")
        NUM_TIES += 1
        
    add_win()
    
    print(display_scoreboard(player_wins, pc_wins, NUM_TIES, Num_rounds))
    
    keep_playing = input("Keep playing? (y/n)")
    if keep_playing not in ["y", "Y", "Yes", "yes"]:
        game_loop = False
        
display_game_winner()