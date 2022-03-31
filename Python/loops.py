# for i in range(10):
#     print(i)
# #Range with 1 parameter - do a job x number of times
# #If printing nums - stop before you reach this num

# for i in range(1, 11):
#     print(i)
# #range with 2 paramaters - first value is start, second value stop (not including)
# #Use when you don't want to start from 0/the beginning of your object

# for i in range(0, 1001, 50):
#     print(i)
#Third parameter - default is +1, manually increment your loop index with a different value

# Activity(1):
# Create a list of 4 favourite films
# Use a for loop to show each film in the list
# Create a function called film_check() that checks if the 3rd film in the list is Ghostbusters.
# If it is, it should print "yey it's ghostbusters". If it isn't, it should print "booo, we want ghostbusters"

favourite_films = ["About Time", "Baby Driver", "Titanic", "Finding Nemo"]

for film in favourite_films:
    print(film)
    
def film_check():
    if favourite_films[2] == "Ghostbusters":
        print("yey it's Ghostbusters!")
    else:
        print("Boooo, we want Ghostbusters!")
        
film_check()


#  Activity(2):
# If you can create a for loop to print 0-9 on the terminal, how can you create one to count backwards from 9-0?
# Consider the different ways we've used range and give it a go. Research if necessary!

for i in range(10):
    print(i)
    
for i in range(9, -1, -1):
    print(i)
    
#range(start, stop, step)

import random

rand_num = random.randint(0,50)

my_num = 50

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,50)
    
print("You've found {}!".format(my_num))