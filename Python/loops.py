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

# Activity(1): 
# Create a for loop that prints "hello world" 13 times. Now, convert this into a while loop that does the same job. 

for i in range(13):
    print("hello world")
i = 0
while i < 13:
    print("hello world")
    i += 1


# Activity(2): 
# Create a variable, use a loop to generate a random number between 1 and 30 six times. 
# For each random number generated, check if this number of divisible by 7 or not.

import random
for i in range(6):
    num = random.randint(1, 30)
    if num % 7 == 0:
        print(num, "IS divisible by 7.")
    else:
        print(num, "is NOT divisible by 7.")
        
# Activity(3):
# Create a while loop to randomly cycle through a list of card suits until a given suit is reached.sum
# Create a variable called current_card and use a list method to randomly give it a value from the list every time the loop runs. Then compare this to the suit you want to find to stop the while loop.
import random
cards = ["Diamond", "Spade", "Club", "Heart"]
current_card = random.choice(cards)
my_card = "Heart"
while my_card != current_card:
    print(current_card)
    current_card = random.choice(cards)
print(f"You found {my_card}!")