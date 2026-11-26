import random


def create_room():
    room = random.choice(types)
    adj = random.choice(adjectives)
    feature = random.choice(features)
    adj_2 = random.choice(adjectives_2)
    description = f"""
    You find yourself in a {adj}, {adj_2} {room}. In the room you can see a {feature}.
    """
    return description


types = [
    "Barrack",
    "Playground",
    "Fisherman Hideout",
    "House",
    "Treehouse",
    "Warehouse",
    "Pond",
    "Parking Lot",
    "Grocery Isle",
    "Crypt",
]
features = [
    "treasure chest",
    "crumbling statue",
    "tilting tree",
    "piece of chewed-up gum",
    "mirror",
    "plethora of barrels",
    "lot of spiders",
    "rotten potato",
    "glass of water",
    "monke",
]
adjectives = [
    "Eerie",
    "Abandoned",
    "Lonely",
    "Ruined",
    "Foggy",
    "Spacious",
    "Dim",
    "Humid",
    "Unsettling",
    "Cramped",
]
adjectives_2 = [
    "gigantic",
    "small",
    "ancient-looking",
    "vivid",
    "shady",
    "fragrant",
    "tall",
    "little",
    "loud",
    "surreal",
]
