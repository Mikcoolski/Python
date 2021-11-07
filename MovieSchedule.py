#List of movie showtimes
moviesTimes = { "Batman": "1:00PM",
                "Superman": "3:00PM",
                "Cat Woman": "5:00PM"}

#prompt the user the list of movies
print("We are currently have the following movies playing today:")
for movie in moviesTimes:
    print(movie)

#ask the user what movies they would like to see the times for
movieRequest = input("\nWhat movie would you like to see the times for?:")

#Display the movie time for the request given
print("The movie time(s) you requested for are:\n",moviesTimes.get(movieRequest))