#a is distance to Edinburgh
a=-3.19
#b is distance to Los Angeles
b=-118.24
#c is distance to Haining
c=116.39
#d is LA to E
d=a-b
#e is H to E
e=c-a
#comparison
if d<e:
 print ('The distance between LA and Edinburgh is shorter than distance between Haining and Edinburgh')
elif d>e:
 print ('The distance between LA and Edinburgh is longer than distance between Haining and Edinburgh')
else: 
 print ('The distance is same.')
#Booleans
X=True
Y=False
W=X and Y
Z=X or Y
print ('W is',W,'and Z is',Z)

