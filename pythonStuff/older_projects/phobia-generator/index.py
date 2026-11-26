animals = []

phobias = []

times_looped = 0

def User_animals():
    global times_looped
    for num in range(1,5):
        times_looped += 1
        animal = input(f"Enter animal {times_looped}: ")
        animals.append(animal)
    print()    

def List_of_animals():
    print("Here are all of the animals you gave me:\n")
    for x in animals:
        print(x)
    print()
        
def Animal_phobia_maker():
    for animal in animals:
        phobia = animal + "ophobia"
        phobias.append(phobia)
    
def List_of_animal_phobias():
    print("And here are the phobia names you have invented for those animals:\n")
    Animal_phobia_maker()
    for phobia in phobias:
        print(phobia)
        
User_animals()
List_of_animals()
List_of_animal_phobias()