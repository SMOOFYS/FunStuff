welcome_banner = """
                Welcome to the List Workout!
    In this app, you'll need to create lists based off of
    the prompts below and display the correct item from 
    each list to answer the prompt.
"""

print(welcome_banner)

def view_planets():
    num_planets = len(planets)
    print(f"There are {num_planets} in our solar system.")
    print(planets)

    
    
    
# Create a list of the 8 planets in our solar system (in order from closest to the
# sun to farthest from the sun)
planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]

# Display the list of planets
# Display "There are 8 planets in our solar system". Use the function that
# tells you how many items are in a list to do this.
view_planets()

# For the next set of challenges, you'll need to use the correct index
# number of each planet as you display information about them.
print("Let's practice indexing our list of planets.")


# Display "We live on planet Earth".
print(f"We live on planet {planets[2]}")

# Display "The closest planet to the sun is Mercury".
print(f"The closest planet to the sun is {planets[0]}")

# Display "The farthest planet from the sun is Neptune".
print(f"The farthest planet from the sun is {planets[7]}")

# Display "The great red spot is on Jupiter".
print(f"The great red spot is on {planets[4]}")

print("Is Pluto in our planets list?")


# Add a conditional statement that displays
# "Pluto is in our planets list" if Pluto is in the list of planets
# It should display "Pluto is NOT in our planets list" otherwise.

if "Pluto" in planets:
    print("Pluto is in our planets list.")
elif "Pluto" not in planets:
    print("Pluto is NOT in our planets list.")

print("Let's add Pluto to our list of planets (even though it technically isn't).")


# Add Pluto to the end of the planets list.
planets.append("Pluto")

# Add a conditional statement that displays
# "Pluto has been added to the planets list" if Pluto is in the list of planets
# It should display "Pluto has not been added to the planets list" otherwise.

if "Pluto" in planets:
    print("Pluto has been added to the planets list.")
elif "Pluto" not in planets:
    print("Pluto has not been added to the planets list.")
    
print("Nevermind, let's remove Pluto from the list of planets.")

# Remove Pluto from the planets list

planets.pop(-1)

# Add a conditional statement that displays
# "Pluto has been removed from the planets list" if Pluto is not in the list of planets
# It should display "Pluto is still in the planets list" otherwise.

if "Pluto" in planets:
    print("Pluto is still in the planets list.")
elif "Pluto" not in planets:
    print("Pluto has been removed from the planets list.")




