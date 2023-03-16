# What does this piece of code do?
# Answer: Run a [1,100)-random-integer-fetch process 10 times and print the biggest random integer.
# Import libraries
#  randint allows drawing a random number,
#  e.g. randint(1,5) draws a number between 1 and 5
from random import randint
#  ceil takes the ceiling of a number, i.e. the next higher integer.
#  e.g. ceil(4.2)=5
#  useless in this program, as randint is already fetching integer :(
from math import ceil
# setting variables to store the run-number and biggest random integer
progress=0
stored_random_number=0
# progress+=1 means progress=progress+1, to store the time you run this while loop
while progress<10:
	progress+=1
# get a random integer in the [1,100) interval
	n = randint(1,100)
# fetch the biggest one
	if n > stored_random_number:
		stored_random_number = n
#print the biggest number
print(stored_random_number)
