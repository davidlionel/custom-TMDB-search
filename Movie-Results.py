import pandas as pd
import tmdbsimple as tmdb
tmdb.API_KEY = 'cd0107a9d4d806541eb7237dce3d9757'

searchDataFrame = pd.read_csv('search-data.csv')


# Run this script to get results from existing CSV.

#### RESULTS ####
# Count number of same occurences, group them by movie_id, display count and sort by count
searchDataFrame['count'] = searchDataFrame.groupby('title')['count'].transform(len)
searchDataFrame['count'] = searchDataFrame['count']
searchDataFrame = searchDataFrame.sort_values("count", ascending=False)
searchDataFrame= searchDataFrame.drop_duplicates('title')
searchDataFrame = searchDataFrame.rename(columns={'count': 'score'})


pd.set_option('display.max_rows', len(searchDataFrame))
print(searchDataFrame)

