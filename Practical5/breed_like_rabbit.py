#rabbit generation
#ge is generation number, n is the rabbit ammount
ge=1
n=2
#to test the generation with loop
while n<=100:
 n=n*2
 ge=ge+1
print ('The number of generations required to exceed 100 rabbits is '+ str(ge))
