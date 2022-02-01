#IMPORTS
from platform import release
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#LIST
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

#DICTIONARY
#movie_dict = { 2011: 103, 2012: 101, 2013: 99, 2014: 100, 2015: 100, 2016: 95, 2017: 95, 2018: 96, 2019: 93, 2020: 90 }
#movie_dict = dict(zip(years, durations))
movie_dict = {'years': years, 'durations': durations}
print(movie_dict)

#DATAFRAME 
durations_df = pd.DataFrame(list(movie_dict.items()))
print(durations_df)

#CREATE LINE PLOT
plt.plot(years, durations)
plt.title("Netflix Movie Durations 2011-2020")
plt.show()

#READ CSV DATAFRAME
netflix_df = pd.read_csv("./netflix_data.csv")
netflix_df['duration'] = netflix_df['duration'].str.replace('min', '')

#SUBSETTING DATAFRAME FOR TYPE "MOVIE"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

#SELECTING COLUMNS OF INTEREST
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "listed_in", "release_year", "duration"]]
print(netflix_movies_col_subset[0:5])

#CREATING SCATTER PLOT:  RELEASE YEAR X DURATION
rlsy = pd.to_numeric(netflix_movies_col_subset["release_year"])
drtn = pd.to_numeric(netflix_movies_col_subset["duration"])

plt.scatter(rlsy, drtn)
plt.title("Movie Duration by Year of Release")
plt.show()

#CREATING SHORT_MOVIES DATAFRAME (< 60 MINUTES)
short_movies = netflix_movies_col_subset[drtn < 60]
print(short_movies)