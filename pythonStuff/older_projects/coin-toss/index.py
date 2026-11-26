from random import randint

coin_toss = True
count_loop = 0
min_streak = 2
max_streak = 5
while coin_toss:
    h_t = int(input("(1) Heads or (2) Tails?\n-> "))
    random_guess = randint(1,2)
    if h_t == random_guess:
        count_loop += 1
        print(f"Great job, you got it right! You are currently on a {count_loop}x winning streak!")           
    if h_t != random_guess and h_t in [1, 2]:
        print("Unfortunate... your answer is wrong.")
        count_loop == 0
        coin_toss = False
    if h_t > 2 or h_t < 1:
        print("That input is invalid. Please pick a number 1 or 2.")
if count_loop == min_streak:
    print(f"Congrats! You just won $50 for geting a streak of {count_loop}x!")
if count_loop >= max_streak:
    print(f"Congrats! You just won a grand total of $100 for getting a streak of {count_loop}x!")
if count_loop == max_streak - 1:
    print("Oh no! You were one win short of getting the grand total prize of $100! For getting so close, take a complimentary prize of $10 on top of your $50.")