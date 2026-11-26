def view_all_items():
    if len(wishlist) == 0:
        print("You don't have any items in your wishlist.")
        return
    for items, cost in wishlist.items():
        print(f"{items} = ${cost}")
    return

def view_item():
    item_view = input("What item would you like to view from your wishlist?\n")
    if item_view in wishlist:
        print(f"{item_view} costs ${wishlist[item_view]}")
    elif item_view not in wishlist:
        print("That item is not in your wishlist.")
    return

def add_item():
    item_add = input("What item would you like to add to your wishlist?\n")
    if item_add in wishlist:
        print("You already have that item in your wishlist.")
        return
    if item_add not in wishlist:
        item_cost = input("Enter the cost of the item: ")
        wishlist[item_add] = item_cost
        print(f"{item_add} has been added to your wishlist.")
    return


def delete_item():
    item_gone = input("What item do you want to delete from your wishlist?\n")
    if item_gone not in wishlist:
        print("You don't have that item in your wishlist yet.")
        return
    if item_gone in wishlist:
        wishlist.pop(item_gone)
        print(f"{item_gone} has been removed from your wishlist.")
    return

wishlist = {
    "Comic Book": 15,
    "Backpack": 35,
    "T-shirt": 20,
    "Cap": 7
}

options = """
    (1) View Wish List (2) View Item (3) Add Item
    (4) Delete Item (5) Exit
"""


while True:
    choice = int(input(options))

    if choice == 1:
        view_all_items()
    elif choice == 2:
        view_item()
    elif choice == 3:
        add_item()
    elif choice == 4:
        delete_item()
    elif choice == 5:
        break
    else:
        print(f"{choice} is not a valid option")
