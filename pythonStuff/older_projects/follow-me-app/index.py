def display_options():
    choice = int(input(" | (1) View Friends (2) Follow Friend (3) Unfollow Friend (4) Exit | "))
    return choice

def view_friends():
    num_friends = len(friend_list)
    print(friend_list)
    print(f"You have {num_friends} friends.")
def follow_friend():
    added_friend = input("Who do you want to friend?\n")
    friend_list.append(added_friend)
    print(f"{added_friend} has been added to your friends list.")

def unfollow_friend():
    view_friends()
    index = int(input("What is the index of the friend that you want to unfollow? (First friend in list is 0, and so on)\n"))
    friend_list.pop(index)
    print("Friend has been removed.")
    
friend_list = [
    "Grovejuice",
    "supsMan2321",
    "Jailreck288",
    "IcyThe4st",
]
    
while True:
    option = display_options()
    if option == 1:
        view_friends()
    elif option == 2:
        follow_friend()
    elif option == 3:
        unfollow_friend()
    elif option == 4:
        print("Thank you for using the Follow Me app.")
        break
