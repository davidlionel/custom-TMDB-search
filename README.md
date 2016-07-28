# custom-TMDB-search

Walkthrough Video: https://youtu.be/X27SMC4fyIQ

All movie information supplied by the great folks at TheMovieDB.org (TMDB)

# Why it exists
I am a bonified cult movie nerd with a pretty narrow taste. I almost never get good recommendations from Netflix, Amazon, or even Letterboxd. I assume this is because I am an outlier in my taste: I almost never enjoy the latest Hollywood movie, I almost never identify my "movie mood" by genre, so I needed a script that made finding the kind of movies I like simpler.

Instead of average user ratings or genres, I focus on keywords, crew, and cast. For me, I am usually looking for movies with the same "feel", regardless of era or genre, and that usually comes down to the people behind the making of the films.

# How to Use:
1. Navigate to the TMDB movie page that you would like to find similar recommendations for.
2. Copy the TMDB movie ID from your address bar.
3. Run the Custom-TMDB-Search.py script
4. Enter the TMDB movie ID and wait.
5. To look up a movie result from the returned list, copy the {movie_id} and paste it at the end of the tmdb movie link. 
EXAMPLE:
Result I want to look up...
```
       movie_id                        title
       128                             [u'Princess Mononoke']
```
So, I paste the "movie_id" (in this case, "128"), at the end of the TMDB `/movie/` link in my browser...
`https://www.themoviedb.org/movie/128`

That's it! Have fun!

# Caveats
If the search breaks the script just before returning your results, simply run the "Movie-Results.py" script and you should be able to see the results of your previous search.

There are API request limits imposed by TMDB, so the searches take longer than you are probably used to. This is not a processing issue, but just a few built-in time-outs to respect TMDB's rules.

Using tmdbsimple wrapper in script:
https://github.com/celiao/tmdbsimple

# Future plans
I may port this to a simple Django app, give it a pretty little front-end, and link the results back to the TMDB movie pages. As far as messing with the insanely simple search algorithm, I want to weight some things differently, add a few parameters and give it a slightly more sophisticated scoring system... Would love to get some feedback from other cult movie fans.
