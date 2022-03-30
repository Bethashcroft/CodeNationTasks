import random

# print(random.random())

# print(random.uniform(1, 1000)) #Gives a random number between a range

# print(random.randint(1, 10)) #Random whole number between a range


print("   |    |   ")           
print("   |    |   ")
print("   |    |   ")
print("------------")
print("   |    |   ")    
print("   |    |   ")   
print("   |    |   ")    
print("------------")
print("   |    |   ")    
print("   |    |   ")    
print("   |    |   ") 

print("HELLO".lower()) # lower() turns words into all lower case
print("codingisfun".upper())# upper() turns words into all upper case
print("testing the capitalize method".capitalize()) 
# capitalize() turns the first character in a string into a capital letter - rest is lower
points = [1, 2 , 3, 3, 3 , 3 , 3 , 4 , 5 , 6]
print(points.count(3))# count() returns the amount of times a specified value is given

string = "Hello, welcome to coding"

print(string.find("to"))
#find() returns the index of the value given


# .replace() Takes two parameters - replaces the first parameter with the second parameter.
print("Hello World".replace("H","Y"))

# .strip() Removes characters from the beginning and/or end of a string. Specify a parameter or use no parameters and this will remove spaces.
print("*****Hello******".strip("*"))

# backslash ignores the subsequent character in a string 
name = "Ann"
fav_drink = "coffee"
print(f'{name}\'s favourite drinks is {fav_drink}')