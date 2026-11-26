"""
################ HINTS #####################################

Print the welcome message whenever you create it.

You should ask the user:
    - How many Marvel comics they want
    - How many DC comics they want
    - Don't forget to convert the response to the correct data type

You should calculate and display:
    - The total cost of the Marvel comics
    - The total cost of the DC comics
    - The total cost of the order

Use a conditional statement to:
    - Print a win message and the comic_movie_prize if the order total is $35
    - Print a lose message otherwise

############################################################
"""


welcome_message = """
    Welcome to the comic store! Find anything that interests you and purchase it! If you manage to get $35 exactly in your price, you can win a guest role in an upcoming movie version of one of the franchise's comics!
"""

# Find ASCII art at https://www.asciiart.eu/
comic_movie_prize = r"""

"""
# The art wasn't working for some reason, it would only work with words so i had to remove it for the Comic store to work.


cost_marvel = 2
cost_dc = 3

num_marvel = int(input("How many marvel comics do you want?\n-> "))
marvel_total = num_marvel*cost_marvel
print(f"You spent ${marvel_total} on marvel comics.")

print()

num_dc = int(input("How many DC comics do you want?\n-> "))
dc_total = num_dc*cost_dc
print(f"You spent ${dc_total} on dc comics.")

print()

order_total = dc_total+marvel_total

print()

if order_total == 35:
    print("You won the free guest role!")
    print(comic_movie_prize)
else:
    print("Not quite $35, try again and maybe you can win a guest role!") 


























