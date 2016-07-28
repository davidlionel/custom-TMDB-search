import tmdbsimple as tmdb
# Add your TMDB API Key here
tmdb.API_KEY = '{YOURAPIKEY}'
import csv
import time
import pandas as pd

print("I would like to recommend some movies for you.")
movieId = input("Please insert a TMDB Movie ID here: ")
movie = tmdb.Movies(movieId)
credits = movie.credits()

# Open our CSV to store some of our info
searchData = open('search-data.csv', 'w')
infoGather = csv.writer(searchData, delimiter=',')
infoGather.writerow(["movie_id", "title", "count"])
maxCalls = 37

# Search by each keyword id and save results to csv
print("Processing Keyword matches...")
tagsRaw = movie.keywords()
tags = tagsRaw["keywords"]
for tag in tags[:maxCalls]:
    keywordSearch = tmdb.Keywords(tag["id"])
    keywordMovies = keywordSearch.movies()
    keywordMovies = keywordMovies["results"]
    for keyMovieResult in keywordMovies:
        row = keyMovieResult
        infoGather.writerow([row["id"],[row["title"]]])
        #print (keyMovieResult["title"])
print("Please wait while we pause to respect the TMDB API Request Limit...")
time.sleep(12)

# Search by each cast id, append and save results to csv
print("Processing Cast matches...")
cast = credits["cast"]
for singleKey in cast[:maxCalls]:
    singleMember = tmdb.People(singleKey["id"])
    alsoStarring = singleMember.movie_credits()
    alsoStarring = alsoStarring["cast"]
    for castMovie in alsoStarring:
        row = castMovie
        infoGather.writerow([row["id"],[row["title"]]])

print("Please wait while we pause to respect the TMDB API Request Limit...")
time.sleep(12)

# Search by each crew id, append and save results to csv
print("Processing Crew matches... Almost done!")
crew = credits["crew"]
for singleKey in crew[:maxCalls]:
    singleMember = tmdb.People(singleKey["id"])
    alsoWorked = singleMember.movie_credits()
    alsoWorked = alsoWorked["crew"]
    for crewMovie in alsoWorked:
        row = crewMovie
        infoGather.writerow([row["id"],[row["title"]]])

print("Process completed.")


# Show TMDB default "similar movie" results for comparison
similarMovies = movie.similar_movies()
similarMovies = similarMovies["results"]
print("Similar results as suggested by TMDB's current algorithm")
for similarMovie in similarMovies:
    print(similarMovie["title"])


#### RESULTS
# Count number of same occurences, group them by movie_id, display count and sort by count
searchDataFrame = pd.read_csv('search-data.csv')
searchDataFrame['count'] = searchDataFrame.groupby('title')['count'].transform(len)
searchDataFrame = searchDataFrame.sort_values("count", ascending=False)
searchDataFrame= searchDataFrame.drop_duplicates('title')
searchDataFrame = searchDataFrame.rename(columns={'count': 'score'})

pd.set_option('display.max_rows', len(searchDataFrame))
print(searchDataFrame)


