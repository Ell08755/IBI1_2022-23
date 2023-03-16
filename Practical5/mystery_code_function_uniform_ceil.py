# What does this piece of code do?
# Answer: Run a [1,100)-ceil-random-number-fetch process 10 times and print the biggest one.
# Import libraries: from [function storage] import [specific function name], letting the program know what is [specific function name].
#  from the [random] storage fetch uniform function
#  uniform let you get a random rational number in a rational interval, e.g.uniform(9.2,19.8) 
from random import uniform
#  from the [math] storage fetch ceil function
#  ceil takes the ceiling of a number, i.e. the next higher integer.
#  e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
#progress+=1 means progress=progress+1, to store the time you run this while loop
	n = ceil(uniform(1,100))
#fetch the biggest one
	if n > stored_random_number:
		stored_random_number = n
#print the biggest number
print(stored_random_number)
