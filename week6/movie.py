
############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like


friend1_movies = []
friend2_movies = []

# Ask the first friend for movies they like and save them in a list
print("Friend 1, please enter the movies you like (separated by commas):")
friend1_movies = input().split(',')

common_movies = []  # To store common movies
common_movie_count = 0  # Count of common movies

# Ask the second friend for movies they like and save them in a list
print("Friend 2, please enter the movies you like (separated by commas):")
friend2_movies = input().split(',')

# Compare the two lists of movies to find common ones
for movie1 in friend1_movies:
    for movie2 in friend2_movies:
        if movie1.strip() == movie2.strip():
            common_movies.append(movie1)
            common_movie_count += 1
            if common_movie_count >= 3:
                break
    if common_movie_count >= 3:
        break

# Print the common movies
if common_movies:
    print("You both like the following movies:")
    for movie in common_movies:
        print(movie.strip())
else:
    print("You don't have any common movie preferences.")
