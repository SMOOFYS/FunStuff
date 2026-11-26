from random import randint
welcome = """
Welcome to the Random Username Generator!
Answer the prompts to generate your random
username.
"""
print(welcome)

name_1 = input("First name: ").capitalize()
name_2 = input("Last name: ").capitalize()
pet = input("Favorite pet: ").capitalize()
food = input("Favorite food: ").capitalize()

three_digit = int(randint(100, 999))
random_number = int(randint(1, 3))

if random_number == 1:
    print(f"Your band name is: {name_1}_{name_2}_{three_digit}")
elif random_number == 2:
    print(f"Your band name is: {three_digit}-{pet}")
elif random_number == 3:
    print(f"Your band name is: {pet}+{food}")

