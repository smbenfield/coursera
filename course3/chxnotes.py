# Methods = functions that are part of a dictionary
# Construct = create empty instance of object

breaker = '----------'

movies = list()
movie1 = dict()
movie1['Director'] = 'James Cameron'
movie1['Title'] = 'Avatar'
movie1['Release Date'] = '18 December 2009'
movie1['Running Time'] = '162 Minutes'
movie1['Rating'] = 'PG-13'
movies.append(movie1)
movie2 = dict()
movie2['Director'] = 'David Finscher'
movie2['Title'] = 'The Social Network'
movie2['Release Date'] = '01 October 2010'
movie2['Running Time'] = '120 Minutes'
movie2['Rating'] = 'PG-13'
movies.append(movie2)

print movies

keys = ['Title', 'Director', 'Rating', 'Running Time']
print breaker
print movies
print breaker
print keys
for item in movies:
    print breaker
    for key in keys:
        print key, ':', item[key]
print breaker
