#Activity1

password = "password123"
if len(password) < 8:
    print("password is too short")
else:
    print(password)


#Activity 2 
num = 30

if num  % 3 == 0 and num % 5 == 0:
    print("This number is divisble by 3 and 5")
else: 
    print("This number is not divisible by 3 and 5")
    
    
#Activity 3

num = 231

if num % 3 == 0 and num % 7 == 0:
    print("fizz buzz")
elif num % 7 == 0:
    print("buzz")
elif num % 3 == 0:
    print("buzz")
else:
    print(num)
    
    
#Activity 4

word = "seasons"

if word[0] == word[-1]:
    print("True")
else:
    print("False")
    
#Activity5

time = 7
place_of_work = "office"
town_of_home = "wigan"

if time == 7:
    print(f"I am in {town_of_home}")
elif time == 8:
    print("I am commuting")
elif time == 9:
    print(f"I am at the {place_of_work}")
    
#Activity6

num1 = 10
num2 = 12
sum = num1 + num2

if sum % 2 == 0:
    print("True")
else:
    print("False")