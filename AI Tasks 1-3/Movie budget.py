movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

add_movies = input("Do you want to add more movies? (yes/no): ")
if add_movies.lower() == "yes":
    num_movies_to_add = int(input("How many movies do you want to add? "))
    for i in range(num_movies_to_add):
        movie_name = input("Enter movie name: ")
        movie_budget = int(input("Enter movie budget: "))
        movies.append((movie_name, movie_budget))

total_budget = 0
for movie in movies:
    total_budget += movie[1]

average_budget = total_budget / len(movies)

print("Movies with budget higher than average:")
count = 0
for movie in movies:
    if movie[1] > average_budget:
        print(f"{movie[0]} has a budget of {movie[1]}, which is {movie[1] - average_budget} higher than the average.")
        count += 1

print(f"{count} movies spent more than the average budget of {average_budget}.")