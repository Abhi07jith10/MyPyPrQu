# Movie Rating Analysis
# Find the average rating of each movie and display the movie with the highest average rating.
# movies = {
#  "Inception": {"ratings": [8, 9, 10, 9]},
#  "Interstellar": {"ratings": [10, 9, 9, 10]},
#  "Avatar": {"ratings": [7, 8, 9, 8]}
# }
# Expected output:
# Inception: 9.0
# Interstellar: 9.5
# Avatar: 8.0
# Highest Rated Movie: Interstellar

movies = {
  "Inception": {"ratings": [8, 9, 10, 9]},
  "Interstellar": {"ratings": [10, 9, 9, 10]},
  "Avatar": {"ratings": [7, 8, 9, 8]}
 }

high_rate=0
name=""
for i in movies:
    total=sum(movies[i]["ratings"])
    average=total/4
    
    print(f"{i}:{average}")

    if average>high_rate:
        high_rate=average
        name=i
print(f"highest rated movie is {name}")
    