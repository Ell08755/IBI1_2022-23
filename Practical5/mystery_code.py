# What does this piece of code do?
# Answer: Run a [1,100)-ceil-random-number-fetch process 10 times and print the biggest one.
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
#progress+=1 means progress=progress+1, to store the time you run this while loop
	n = randint(1,100)
#fetch the biggest one
	if n > stored_random_number:
		stored_random_number = n
#print the biggest number
print(stored_random_number)
