from Rooms import create_room
import random


def show_player_stats():
    print_bar()
    print(
        f"""
        {name["Player_name"]}:
        Health: {Player_stats["Health"]}
        Potions: {Player_stats["Potions"]}
        Gold: {Player_stats["Gold"]}
        """
    )


def getInput():
    print("Actions")
    print_bar()
    for choicy in choices:
        print(choicy)
    player_choice = input("What would you like to do? ")
    return player_choice


def search():
    luck = random.randint(0, 5)
    if luck == 0:
        print("You got caught in a trap! You took 10 damage.")
        Player_stats["Health"] -= 10
    elif luck == 1:
        get_loot()
    elif luck == 2:
        print("You found a healing potion.")
        Player_stats["Potions"] += 1
    elif luck == 3 or luck == 4:
        print("You were attacked!")
        start_combat()
    else:
        print("Tough luck, you didn't find anything!")


def get_loot():
    global loot
    loot = random.randint(100, 1001)
    print(f"You found {loot} gold!")
    Player_stats["Gold"] += loot


def heal():
    if Player_stats["Potions"] > 0:
        Player_stats["Potions"] -= 1
        Player_stats["Health"] += 10
    else:
        print("You don't have any potions to use!")


def print_bar():
    print("===============")


def start_combat():
    enemies = ["orc", "troll", "cave spider", "zombie", "dweller"]
    enemy = random.choice(enemies)
    print(f"A {enemy} jumped out from a hidden alcove!")
    enemy_health = random.randint(1, 3)
    while enemy_health > 0:
        attack = random.randint(0, 3)
        if attack == 0:
            print(f"You missed...\nYou took 15 damage from the {enemy}.")
            Player_stats["Health"] -= 15
            if Player_stats["Health"] <= 0:
                print("You passed out from your injuries!")
                break
        else:
            print(f"You struck the {enemy} for {attack} damage.")
            enemy_health -= attack
        battle_status(enemy, enemy_health)
    print("You've won the battle!")
    get_loot()
    return
    


def battle_status(enemy_name, enemy_health):
    print(
        f"""
        {enemy_name}:{enemy_health}
        {name["Player_name"]}:{Player_stats["Health"]}
        """
    )


print(
    """┏┓┏┓┏┓╋╋╋╋╋╋╋╋╋╋╋┏┓┏━━━┓╋╋╋╋╋╋╋╋┏┓
┃┃┃┃┃┃╋╋╋╋╋╋╋╋╋╋╋┃┃┃┏━┓┃╋╋╋╋╋╋╋┏┛┗┓
┃┃┃┃┃┣┳━━━┳━━┳━┳━┛┃┃┃╋┃┣┓┏┳━━┳━┻┓┏┛
┃┗┛┗┛┣╋━━┃┃┏┓┃┏┫┏┓┃┃┃╋┃┃┃┃┃┃━┫━━┫┃
┗┓┏┓┏┫┃┃━━┫┏┓┃┃┃┗┛┃┃┗━┛┃┗┛┃┃━╋━━┃┗┓
╋┗┛┗┛┗┻━━━┻┛┗┻┛┗━━┛┗━━┓┣━━┻━━┻━━┻━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛"""
)


Player_stats = {
    "Health": 100,
    "Potions": 0,
    "Gold": 0,
}
name = {"Player_name": input("What is your name, Wizard? ")}
print("May good luck be on your side, " + name["Player_name"])
choices = ["Move on (1)", "Search (2)", "Heal (3)", "Quit (4)"]

room = create_room()
while True:
    print(room)
    show_player_stats()
    action = getInput()
    if action == "4":
        break
    elif action == "1":
        print("You move on to the next room...")
        room = create_room()
    elif action == "2":
        print("You searched the room")
        search()
    elif action == "3":
        heal()

    input("\nPress enter to continue")

print("Game over")
