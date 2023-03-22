# This is the Movie genre task.
# import matplotlib
import matplotlib.pyplot as plt
# create dictionary and input datas, print
my_dict = {}
Movie_genres = {'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-Fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
print('Movie genres dictionary', Movie_genres)
# Draw piechart from dictionary, set up as equal, percent number, show the piechart
plt.pie(Movie_genres.values(),labels=Movie_genres.keys(),autopct='%1.1f%%')
plt.axis('equal')
plt.show()
#test input, the variable name is GenrQ, and use 'Comedy' as example for practical task
# fetch the value by key, and print it
GenrQ=Movie_genres['Comedy']
print('Comedy favorite students number:', GenrQ)
# another way to show dictionary's function by user's input
# reach for the input, let a variable equal to it, fetch the key and search for value in dictionary, print
Genr1=input('Movie genre you wanna know:')
h=Movie_genres.get(Genr1, 'Genre not found')
print(h)
