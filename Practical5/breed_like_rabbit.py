#rabbit generation
#creat two variables to store generation number and rabbit amount, initialse the numbers
ge=1 #ge means generation
n=2 #n means rabbit amount
#to test the generation with while loop, double every generation, store the generation number and amount
while n<=100:
 n=n*2
 ge=ge+1
#print conclusion
print ('The number of generations required to exceed 100 rabbits is '+ str(ge))
