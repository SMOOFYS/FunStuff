from random import randint

welcome = """
Welcome to the Band name Generator!
Answer the queries to create your random
band name.
"""
print(welcome)

singer = input("Lead singer's first name: ").capitalize()
adjective = input("Adjective describing the music: ").capitalize()
plural_noun = input("A plural noun: ").capitalize()
month = input("A month of the year: ").capitalize()
verbing = input("A verb ending in `ing`: ").capitalize()
plural_animal = input("A plural animal: ").capitalize()
color = input("A color: ").capitalize()
body = input("A body part: ")

band_name = [
    singer,
    adjective,
    plural_noun,
    month,
    verbing,
    plural_animal,
    color,
    body,
]


random_number = int(randint(0, 4))

if random_number == 0:
    print(f"'{singer} and the {plural_noun}'.")
elif random_number == 1:
    print(f"The '{adjective} {plural_noun}'.")
elif random_number == 2:
    print(f"The {month} {plural_noun}.")
elif random_number == 3:
    print(f"The {color} {body}.")
elif random_number == 4:
    print(f"The '{verbing} {plural_animal}'")


# Use for random picking
