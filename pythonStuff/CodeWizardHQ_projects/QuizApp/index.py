print("Video Game Quiz")
print()

correct_answers = 0
# Use \n to go to the next line
q1 = input("What is the world's most competitive game as of right now?\n-> ")

if q1 == "Fortnite" or q1 == "fornite":
    # Can also work as -> correct_answers = correct_answers + 1
    print()
    correct_answers += 1
    print("Correct!")
else:
    print()
    print("Incorrect... the answer is Fortnite.")
print()
q2 = input("Do playing action games train you to make right decisions faster? T/F\n-> ")
if q2 == "True" or q2 == "true" or q2 == "t" or q2 == "T":
    print()
    correct_answers += 1
    print("Correct!")
else:
    print()
    print("Incorrect... the answer is True.")
print()
q3 = input("What is the most best-selling console of all time?\n-> ")
if q3 == "playstation 2" or q3 == "Playstation 2":
    print()
    correct_answers += 1
    print("Correct!")
else:
    print()
    print("Incorrect... the answer is Plasystation 2")
print()
q4 = input("What is the most best-selling game?\n-> ")
if q4 == "minecraft" or q4 == "Minecraft":
    print()
    correct_answers += 1
    print("Correct!")
else:
    print()
    print("Incorrect... the answer is Minecraft")
print()
q5 = input("And lastly, how old was the youngest professional pro player?\n-> ")
if q5 == "11":
    print()
    print("Correct!")
    correct_answers += 1
else:
    print()
    print("Incorrect... the answer was 11")

if correct_answers == 5:
    print()
    print(f"You got a {correct_answers}/5, good job!")
else:
    print()
    print(f"You got a {correct_answers}/5, try again for a higher score!")
