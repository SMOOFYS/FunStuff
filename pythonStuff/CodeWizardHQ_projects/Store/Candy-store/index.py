welcome_message = """
    Welcome to Captain Beezob's Candy Store!

    If you spend exactly $50 on candy, you'll receive a pass to
    Captain Beezob's Candy Factory!

    Good luck!
"""

candy_factory_pass = r"""
    .----------------------------.
    |\  /\  /\  /\  /\  /\  /\  /|
    | )(  )(  )(  )(  )(  )(  )( |
    |(  )(  )(  )(  )(  )(  )(  )|
    | )(  )(  )(  )(  )(  )(  )( |
    |(  )(  )(  )(  )(  )(  )(  )|
    | )(  )(  )(  )(  )(  )(  )( |
    |(  )(  )(  )(  )(  )(  )(  )|
    | )(  )(  )(  )(  )(  )(  )( |
    |(  )(  )(  )(  )(  )(  )(  )|
    | )(  )(  )(  )(  )(  )(  )( |
    |/  \/  \/  \/  \/  \/  \/  \|
    '----------------------------'
"""

cost_lolipops = 3
cost_cookies = 5
cost_jellybeans = 2

print(welcome_message)


########################## WRITE YOUR CODE BELOW ###########################

num_lolipops = int(input("How many lolipops do you want?\n-> "))
lolipops_total = num_lolipops*cost_lolipops
print(f"You spent ${lolipops_total} on lolipops.")

print()

num_cookies = int(input("How many cookies do you want?\n-> "))
cookies_total = num_cookies*cost_cookies
print(f"You spent ${cookies_total} on cookies.")

num_jellybeans = int(input("How many jellybeans do you want?\n-> "))
jellybeans_total = num_jellybeans*cost_jellybeans
print(f"You spent ${jellybeans_total} on lolipops.")

print()

order_total = lolipops_total+cookies_total+jellybeans_total

print()
if order_total == 50:
    print("You won the Factory pass!")
    print(candy_factory_pass)
else:
    print("Not quite $50. Try again to get it!") 





















