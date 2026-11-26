print("Let's count from 1 to 10!")
for num in range(1, 11):
    print(num)
    
favorite_fruit = [
    "Watermelon",
    "Peache",
    "Strawberrie",
    "Banana"
]

plural_foods = []

user_foods = [] 

num_letters = 5

times_in_loop = 0

for fruit in favorite_fruit:
    plural_food = fruit + "s"
    plural_foods.append(plural_food)
    
print("\nThese are my favorite fruits that are longer than 5 letters:")
for fruit in plural_foods:
    if len(fruit) > num_letters:
        print(fruit)
print("What are your top 3 favorite foods?")
for food in range(1,4):
    times_in_loop += 1
    user_food_fav = input("Enter food number {}: ")
    user_foods.append(user_food_fav)
print(f"These are your favorite foods (In order):\n{user_foods}")
