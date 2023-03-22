#Distance comparision
#create variables to store the distances
#a is distance to Edinburgh
a=-3.19
#b is distance to Los Angeles
b=-118.24
#c is distance to Haining
c=116.39
#d is distance from LA to Edinburgh
d=a-b
#e is distace from Haining to Edinburgh
e=c-a
#comparision, if d<e, then print 'The distance between LA and Edinburgh is shorter than distance between Haining and Edinburgh', and vice versa except for same distance situation.
if d<e:
 print ('The distance between LA and Edinburgh is shorter than distance between Haining and Edinburgh')
elif d>e:
 print ('The distance between LA and Edinburgh is further than distance between Haining and Edinburgh')
else: 
 print ('The distance is same.')
#Booleans
#set up the origin variables, X is True, Y is False
X=True
Y=False
#define W and Z, W is X and Y, Z is X or Y.
W=X and Y
Z=X or Y
#print the result
print ('W is',W,'and Z is',Z)

