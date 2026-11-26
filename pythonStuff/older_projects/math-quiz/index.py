from random import randint

lives = 3

def display_welcome_banner():
    welcome_banner = """
            Welcome to the Math Quiz!

    You'll start with three lives. 
    Each round, you'll be asked to solve a math problem. 
    If you solve the problem correctly, you won't lose any lives.
    If you can't solve the problem, you lose a life.

    You can gain lives if you solve a problem correctly
    and your lives and level number have the same parity.
    Otherwise, your lives stay the same, even if you 
    solve the problem correctly.

    You can play until you're out of lives.
    """
    print(welcome_banner)

def get_operator():
    choice = randint(1, 4)
    if choice == 1:
        return "+"
    if choice == 2:
        return "-"
    if choice == 3:
        return "*"
    if choice == 4:
        return "/"
    
def get_expression(first_term, second_term, operator):
    if operator == "/":
        message = "(round the answer to the nearest whole number)"
    else:
        message = ""
    return f"What is {first_term}{operator}{second_term} {message}? "

def solve(num1, num2, operation):
    if operation == "/":
        return int(round(num1/num2))
    elif operation == "+":
        return int(num1+num2)
    elif operation == "-":
        return int(num1-num2)
    elif operation == "*":
        return int(num1*num2)
        
def check_lives(numLives, user_answer, expression_answer):
    global lives
    if user_answer != expression_answer:
        print("Wrong!")
        lives = numLives - 1
    if lives % 2 == 0 and user_answer % 2 == 0 and user_answer == expression_answer:
        lives = numLives + 1
        print("That is correct!")
    elif lives % 2 == 1 and user_answer % 2 == 1 and user_answer == expression_answer:
        print("That is correct!")
        lives = numLives + 1
    elif user_answer == expression_answer:
        print("That is correct!")

def out_of_lives(lives):
    if lives <= 0:
        return True
    else:
        return False
    
display_welcome_banner()

user_name = input("What is your name?\n")
still_playing = True
##lives = 3

while still_playing:
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    operator = get_operator()
    expression_answer = solve(num1, num2, operator)
    expression = get_expression(num1, num2, operator)    
    user_answer = input(expression)
    check_lives(lives, user_answer, expression_answer)
    out_of_lives(lives)
    if out_of_lives(lives):
        still_playing = False
    
    
        