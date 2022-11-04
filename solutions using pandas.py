# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:49:32 2022

@author: Martin
"""

# inporting packages 
import numpy as np
import pandas as pd

# reading files
ratings = pd.read_csv('ratings.dat', 
                 sep="\::", 
                 
                 names=['userID', 'movieID','rating', 'timestamp'])


movies = pd.read_csv('movies.dat', 
                 sep="\::", 
                 
                 names=['movieID ', 'title','genres'])
# joining the two tables
movielens = pd.concat([ratings,movies], axis=1)
# finding number of rows and columns; can just print(movielens.shape)
number_of_rows = movielens.shape[0]
number_of_columns = movielens.shape[1]

# printing all the rating values and seeing no zeros
# for question 5, same idea - look at the count value next to the rating of "3"
movielens.rating.value_counts()
# above can be used to answer questions 10 and 11


# finding the number of different movies from the ratings.dat file
len(movielens.movieID.value_counts())

# It looks as though the movies.dat file has more unique movies than the ratings.dat file,
# so I am using this answer, accounting for the NaN value
uniqueMovies = pd.unique(movielens[['movieID', 'movieID ']].values.ravel('K'))
print(uniqueMovies.shape)  #substract 1 from the length to compensate for the 'NaN' value
answer6 = len(uniqueMovies)-1

# number of different users
answer7 = len(movielens.userID.value_counts())


# Going to look at each of the listed movies and how many ratings they have one by one.
namesList = ['Forrest Gump (1994)','Jurassic Park (1993)','Pulp Fiction (1994)','Shawshank Redemption, The (1994)','Speed 2: Cruise Control (1997)']
numberRating = np.zeros(5)


for i in range(len(namesList)):
    movieRatings = movielens.loc[movielens['title'] == namesList[i], 'movieID ']
    numberRating[i] = len(movielens.loc[movielens['movieID'] == movieRatings.values[0], 'rating'])
# answer9 contains the name of the movie with the highest number of ratings
answer9 = namesList[np.argmax(numberRating)]






