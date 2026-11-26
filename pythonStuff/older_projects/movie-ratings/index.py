def view_all_movies():
    if len(movies) == 0:
        print("You don't have any movies reviewed yet!")
        return
    for name, rating in movies.items():
        print(f"{name}'s rating is {rating}")


def view_movie():
    movie_viewer = input("What movie do you want to view from your list?\n")
    if movie_viewer in movies:
        print(f"Rating: {movies[movie_viewer]}")
    elif movie_viewer not in movies:
        print("That movie is not in your list.")
        return

def add_movie():
    name = input("What is the name of the movie you are adding?\n")
    
    if name in movies:
        print("That Movie already exists in your movie list!")
        return
    
    rating = input("Enter the movie's rating: ")
    
    movies[name] = rating    
    print(f"{name} has been added to your movie list.")
    
    

def update_movie():
    movie_update = input("What movie do you want to update?\n")
    if movie_update in movies:
        movie_rating = input("Enter the movie rating: ")
        movies[movie_update] = movie_rating
        print(f"{movie_update}'s rating has updated.")
    elif movie_update not in movies:
        print("That movie is not in your list.")
    return


def remove_movie():
    movie_removal = input("What movie do you want to remove?\n")
    if movie_removal in movies:
        movies.pop(movie_removal)
        print(f"Removed '{movie_removal}' from your list.")
        return
    elif movie_removal not in movies:
        print("That movie is not in your list.")
        return

movies = {
    "The Godfather": 8.7,
    "Uncut Gem": 7,
    "Minions: Rise of Gru": 10,
    "Hard Kill": 0
}


options = """
    (1) View all watched movies (2) View movie rating 
    (3) Add movie               (4) Update movie rating 
    (5) Remove movie            (6) Exit
"""


while True:
    choice = int(input(options))

    if choice == 1:
        view_all_movies()
    elif choice == 2:
        view_movie()
    elif choice == 3:
        add_movie()
    elif choice == 4:
        update_movie()
    elif choice == 5:
        remove_movie()
    elif choice == 6:
        break
    else:
        print(f"{choice} is not a valid option")
