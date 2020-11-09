import pandas as pd


unames = ['user_id', 'gender', 'age', 'occupation', 'zip'] #creating the users data bank
users = pd.read_table('users.dat', sep='::', engine='python', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp'] #creating the ratings data bank
ratings = pd.read_table('ratings.dat', sep='::', engine='python', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres'] #creating the movies data bank
movies = pd.read_table('movies.dat', sep='::', engine='python', header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies) #creating the combined data bank

mean_ratings = data.pivot_table('rating', index = 'title', aggfunc='mean') #creating table of mean values

ratings_by_title = data.groupby('title').size() 
active_titles = ratings_by_title.index[ratings_by_title >= 250] #only include users with 250 ratings

mean_ratings = mean_ratings.loc[active_titles] 
#max_ratings = mean_ratings.sort_values(by='rating') #finding the list of max ratings

#print(max_ratings.sort_index(by='rating'))
#print(max_ratings[::-1][:5]) #printing the list of max ratings to see the highest

max_rating = mean_ratings.nlargest(1, 'rating')
highest_rated_title = str(max_rating.index) #defining the max rated movie


     



print('\nThis is the first 5 rows of user data')
print(users[:5])
print('\nThis is the first 5 rows of ratings data')
print(ratings[:5])
print('\nThis is the first 5 rows of movie data')
print(movies[:5])
print('\nThis is the highest rated movie')
print(highest_rated_title[8:75])
print('\nThis is the first 5 rows of the combined data set')
print(data[:5])
print('\nThis is the number of records in the user data')
print(len(users.index))
print('\nThis is the number of records in the ratings data')
print(len(ratings.index))
print('\nThis is the number of records in the movie data')
print(len(movies.index))
print('\nThis is the number of records in the combined data')
print(len(data.index))