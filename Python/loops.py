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

# favourite_films = ["About Time", "Baby Driver", "Titanic", "Finding Nemo"]

# for film in favourite_films:
#     print(film)
    
# def film_check():
#     if favourite_films[2] == "Ghostbusters":
#         print("yey it's Ghostbusters!")
#     else:
#         print("Boooo, we want Ghostbusters!")
        
# film_check()


#  Activity(2):
# If you can create a for loop to print 0-9 on the terminal, how can you create one to count backwards from 9-0?
# Consider the different ways we've used range and give it a go. Research if necessary!

# for i in range(10):
#     print(i)
    
# for i in range(9, -1, -1):
#     print(i)
    
#range(start, stop, step)

# import random

# rand_num = random.randint(0,50)

# my_num = 50

# while rand_num != my_num:
#     print(rand_num)
#     rand_num = random.randint(0,50)
    
# print("You've found {}!".format(my_num))

# Activity(1): 
# Create a for loop that prints "hello world" 13 times. Now, convert this into a while loop that does the same job. 

# for i in range(13):
#     print("hello world")
# i = 0
# while i < 13:
#     print("hello world")
#     i += 1


# Activity(2): 
# Create a variable, use a loop to generate a random number between 1 and 30 six times. 
# For each random number generated, check if this number of divisible by 7 or not.

# import random
# for i in range(6):
#     num = random.randint(1, 30)
#     if num % 7 == 0:
#         print(num, "IS divisible by 7.")
#     else:
#         print(num, "is NOT divisible by 7.")
        
# Activity(3):
# Create a while loop to randomly cycle through a list of card suits until a given suit is reached.sum
# Create a variable called current_card and use a list method to randomly give it a value from the list every time the loop runs. Then compare this to the suit you want to find to stop the while loop.
# import random
# cards = ["Diamond", "Spade", "Club", "Heart"]
# current_card = random.choice(cards)
# my_card = "Heart"
# while my_card != current_card:
#     print(current_card)
#     current_card = random.choice(cards)
# print(f"You found {my_card}!")


# extra challenges

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

# add up all the numbers in the list 
sum_of_num = 0

for i in my_list:
    sum_of_num += i 
    
print(sum_of_num)

# sum up all the even numbers

even_numbers = []

for i in my_list:
    if i % 2 == 0:
        even_numbers.append(i) 
        
sum_even_numbers = 0

for i in even_numbers:
    sum_even_numbers += i 
    
print(sum_even_numbers)

# count the number of even numbers in the list

count = 0
# for loop checks the length of the list
# then modulus goes through every number and checks the remainder
# if the remainder is 0, then it adds it to the count
# print count to get the answer
for i in range(len(my_list)):
    if my_list[i]%2==0:
        count +=1
print(count)


#looping through a dictionary 
my_dict = {"apple": 2.50, "orange": 4.99, "banana": 0.59}

# accessing keys - aka the strings in this case
for i in my_dict.keys():
    print(i)
    

# accessing values - aka the intergers in this case

for i in my_dict.values():
    print(i)
    
# accessing both values and keys together
# use .items to access both
# use j as i has been used for keys
# format the print so we know which is which 
for i,j in my_dict.items():
    print('Key: ', i)
    print(f'Value: {j}')
