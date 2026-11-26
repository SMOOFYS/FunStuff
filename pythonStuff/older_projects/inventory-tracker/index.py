def display_options():
    options = "(1) View Inventory (2) Add Item (3) Drop Item (4) Exit "
    selected_option = int(input(options))
    return selected_option

def view_inventory():
    num_items = len(inventory)
    print(f"""
    ----------------------
    {inventory}
    ----------------------
    {num_items} Items in Inventory
    ----------------------
    """)
 
def add_item():
    item = input("What item would you like to add to your inventory? ")
    if item in [inventory]:
        print(f"You already have a(n) {item}!")
    else:
        inventory.append(item)
        print(f"{item} has been added to your inventory!")


def drop_item():
    view_inventory()
    index = input("What is the index of the item that you want to remove? (First item in list is 0, and so on)\n")
    dropped_item = inventory.pop(index)
    print(f"Removed {dropped_item} from inventory")
    
    

inventory = [
    "Cloak",
    "Wooden Stick",
    "Ragged Cloth",
    "Worn-out Shield"
]

while True:
    selected_option = display_options()
    if selected_option == 1:
        view_inventory()
    elif selected_option == 2:
        add_item()
    elif selected_option == 3:
        drop_item()
    elif selected_option == 4:
        print("Goodbye!")
        break
