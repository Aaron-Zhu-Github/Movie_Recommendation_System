#!/usr/bin/env python
# coding: utf-8

# In[3]:


# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    
    
    lines = []
    movie_ratings_dict  = defaultdict(list)
    
    with open (f, "r") as file:
        lines = file.readlines()
    file.close()
    
    for i in range(len(lines)):
        word = lines[i].strip('\n').split('|')
        movie_ratings_dict[word[0]].append(word[1])

    return movie_ratings_dict 

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    # { "Toy Story (1995)" : "Adventure", "Golden Eye (1995)" : "Action" }
    
    
    lines = []
    movie_genre_dict  = {}
    
    with open (f, "r") as file:
        lines = file.readlines()
    file.close()
    
    for i in range(len(lines)):
        word = lines[i].strip('\n').split('|')
        movie_genre_dict[word[2]] = word[0]

    return movie_genre_dict



# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    # { genre1: [ m1, m2, m3], genre2: [m6, m7] }
    
    genre_to_movie =  defaultdict(list)

    for key, value in d.items():
            
            genre_to_movie[value].append(key);

    return genre_to_movie


    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    # {"Spider-Man (2002)": [3,2,4,5]}  ==>   {"Spider-Man (2002)": 3.5}
    
    rating_avg = {}

    for key in d.keys():
            avg = sum(d[key])/len(d[key])
            rating_avg[key] = avg

    return rating_avg

    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    popular = {}
    for key, value in sorted(d.items(), key=lambda item: item[1], reverse = True)[:n]:
        popular[key] = value

    return popular

    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    thres = {}
    for key, value in d.items():
        if value >= thres_rating:
            thres[key] = value
    return thres
    

    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    genre_list = []
    for key, value in genre_to_movies.items():
        if key == genre:
            genre_list = value
     
    match_rating = {}
    for i in genre_list:
        for key, value in movie_to_average_rating.items():
            if i == key:
                match_rating[key] = value
        
    genre_popular = dict(sorted(match_rating.items(), key=lambda item: item[1], reverse = True)[:n])

            
    return genre_popular

    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    genre_list = []
    for key, value in genre_to_movies.items():
        if key == genre:
            genre_list = value
            
    match_rating = {}
    for i in genre_list:
        for key, value in movie_to_average_rating.items():
            if i == key:
                match_rating[key] = value
     
    total = 0
    for value in match_rating.values():
        total += value
    
    avg = total/len(match_rating)
           

    return avg
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    gener_pop = {}
    
    
    for key, value in genre_to_movies.items():    
        match_rating = {}
        for i in value:
            for k, v in movie_to_average_rating.items():
                if i == k:
                    match_rating[k] = v
     
        total = 0
        for val in match_rating.values():
            total += val
    
        avg = total/len(match_rating)
        gener_pop[key] = avg
           
    gener_pop = dict(sorted(gener_pop.items(), key=lambda item: item[1], reverse = True)[:n])
    return gener_pop

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    # WRITE YOUR CODE BELOW
    lines = []
    user_ratings  = defaultdict(list)
    
    with open (f, "r") as file:
        lines = file.readlines()
    file.close()
    
    for i in range(len(lines)):
        word = lines[i].strip('\n').split('|')
        user_ratings[word[2]].append((word[0] ,float(word[1])))

    return user_ratings

    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    movie_list = []
    for key, value in user_to_movies.items():
        if user_id == key:
            movie_list = value
            
    genre_top  = defaultdict(list)
    for i in range(len(movie_list)):
        for k, v in movie_to_genre.items():
            if movie_list[i][0] == k:
                genre_top[v].append(movie_list[i])
                
    genre_rating = {}
    
    for k1, v1 in genre_top.items():
        total = 0
        for i in range(len(v1)):
            total += v1[i][1]
        avg = total / len(v1)
        genre_rating[k1] = avg
           
    user_genre = sorted(genre_rating.items(), key=lambda item: item[1], reverse = True)[:1][0][0]
    return user_genre
            

    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    movie_list = []
    for key, value in user_to_movies.items():
        if user_id == key:
            movie_list = value
            
    genre_top  = defaultdict(list)
    for i in range(len(movie_list)):
        for k, v in movie_to_genre.items():
            if movie_list[i][0] == k:
                genre_top[v].append(movie_list[i])
                
    genre_rating = {}
    
    for k1, v1 in genre_top.items():
        total = 0
        for i in range(len(v1)):
            total += v1[i][1]
        avg = total / len(v1)
        genre_rating[k1] = avg
           
    user_genre = sorted(genre_rating.items(), key=lambda item: item[1], reverse = True)[:1][0][0]
    
    mylist = []
    for i in range(len(movie_list)):
        mylist.append(movie_list[i][0])
    
    recommend_range = {}
    for k2, v2 in movie_to_average_rating.items():
        for k3, v3 in movie_to_genre.items():
            if k3 == k2 and v3 == user_genre:
                recommend_range[k2] =v2
    
    recommend_list = {}
    for k4, v4 in recommend_range.items():
        if k4 not in mylist:
            recommend_list[k4] = v4
            
    recommend_top3 = dict(sorted(recommend_list.items(), key=lambda item: item[1], reverse = True)[:3])
        
    return recommend_top3
    


# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading

    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions

    
# program will start at the following main() function call
# when you execute hw1.py
    main()

    


# In[ ]:




