#IMPORTS
import numpy as np
import pandas as pd

#LIST
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

#DICTIONARY
#movie_dict = { 2011: 103, 2012: 101, 2013: 99, 2014: 100, 2015: 100, 2016: 95, 2017: 95, 2018: 96, 2019: 93, 2020: 90 }
movie_dict = dict(zip(years, durations))

print(movie_dict)

#DATAFRAME 
durations_df = pd.DataFrame(list(movie_dict.items()))

print(durations_df)