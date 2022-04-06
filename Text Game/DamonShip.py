from secrets import choice
import time
import random
from xmlrpc.client import boolean


name = ""
messageDelay = 1

health = 5
keys = 0
BananaEaten = False
MilkDrank = False
SnakeDodge = False
KeyFound = False


# Functions - Utilities
def SetName(desiredName):
    global name
    name = desiredName

def StartGame():
    global health
    global keys
    print("Welcome! This is an escape room")
    time.sleep(messageDelay)
    print()
    desiredName = input("What is your name?")
    SetName(desiredName)
    print(desiredName, "is a great name! Now try to escape!")

    health = 5
    keys = 0

    MainRoom()

def ExitGame():
    ShowText("We hope you had fun playing")
    ShowText("Would you like to try again?")
    
    choice = PresentChoicesDynamic(["Retry", "Exit"])

    if choice == "Retry":
        StartGame()
    if choice == "Exit":
        exit()

def ShowPlayerStats():
    global name
    global health
    global keys
    characterString = "< --- Character - " + name + " --- >"
    ShowText(characterString)
    print("You have", health, "Health and", keys, "keys.")

# Creates a set of options from a list of strings (options)
# "Choices" - a list of strings
# Outputstring - "You can choose: Eggs, Banana, Milk"
# Main Functions
def PresentChoicesDynamic(choices):
    x = ""
    choices = (choices)
    while x not in choices:
        outputstring = "You can choose: "
        for choice in choices:
            outputstring += choice + ", "
        ShowText(outputstring)
        x = input().strip()

    return x


def EnterRoom(roomName):
    entranceText = "< ==== " + roomName + " ==== >"
    ShowText(entranceText)
    ShowPlayerStats()

def ShowText(text):
    time.sleep(messageDelay)
    print()
    print(text)

def Changekeys(change):
    global keys
    keys += change
    
    
    if change <= 0:
        print("You have lost", change, "keys")
        MainRoom()
    else:
        print("You have gained", change, "keys")
        MainRoom()
   


def ChangeHealth(change):
    global health
    health += change
    if change <= 0:
        print("You have lost", change, "health")
    else:
        print("You have gained", change, "health")
    if health <= 0:
        ExitGame()

# PresentChoiceDynamic uses a list of strings to present choices []
# SCENARIO 1 -
def MainRoom():
    EnterRoom("Main Room")
    ShowText("There is a wall, floor and trunk.")

    choice = PresentChoicesDynamic(["Wall", "Floor", "Trunk"])

    if (choice == "Wall"):
        LookAtWall()
    if (choice == "Floor"):
        LookAtFloor()
    if (choice == "Trunk"):
        LookInTrunk()

def LookAtWall():
    EnterRoom("Wall")
    ShowText("There are items on the wall")
    ShowText("The picture frame is slightly ajar")

    choice = PresentChoicesDynamic(["Shelf", "Picture Frame", "Map of the Ship", "Go Back"])

    if (choice == "Shelf"):
        LookAtShelf()
    if (choice == "Picture Frame"):
        LookAtPicture()
    if (choice == "Map of the Ship"):
        LookAtShipMap()
    if (choice == "Go Back"):
        MainRoom()

def LookAtFloor():
    EnterRoom("Floor")
    ShowText("You look at the floor")
    ShowText("There is a Snack, Rug and Shoe")

    choice = PresentChoicesDynamic(["Snack", "Rug", "Shoe", "Go back"])

    if (choice == "Snack"):
        LookAtSnack()
    if (choice == "Rug"):
        LookAtRug()
    if (choice == "Shoe"):
        LookAtShoe()
    if (choice == "Go back"):
        MainRoom()

def LookAtSnack():
    EnterRoom("Snack")
    ShowText("You find a banana, Do you want to eat it(Yes or No)")
    choice = PresentChoicesDynamic(["Yes", "No"])
    if choice == "Yes":
        EatBanana()
    if choice == "No":
        ShowText("You drop the banana and go back to looking at the floor")
        LookAtFloor()


def EatBanana():
    global BananaEaten
    coinflip = random.randint(0,1)

    if (BananaEaten):
        ShowText("There is a banana peel here, you already ate the banana")
        LookAtFloor()
        return

    if coinflip == 0:
        print("Luckily for you, The banana was fresh. ")
        ChangeHealth(1)
    else:
        print("You took one bite of the banana, it was rotten")
        ChangeHealth(-2)

    BananaEaten = True    
    LookAtFloor()

def LookAtRug():
    EnterRoom("Rug")
    ShowText("Oh no! You slipped on the rug")
    ChangeHealth(-1)
    ShowText("You were incorrect, Try again")
    LookAtFloor()


def LookAtShoe():
    global KeyFound
    EnterRoom("Shoe")
    if (KeyFound):
        ShowText("You already took the key don't be greedy")
        LookAtFloor()
        return
    ShowText("Congratulations!, You have found a key")
    KeyFound = True 
    Changekeys(1)
    LookAtFloor()
    
#SCENARIO 2 -

def LookInTrunk():
    EnterRoom("Trunk")
    print("SNAKE!!!!!")
    InsideTrunk()
    ShowText("You see other things in the trunk.")

    choice = PresentChoicesDynamic(["Diary", "Drink", "T-shirt", "Go back"])

    if (choice == "Diary"):
        LookAtDiary()
    if (choice == "Drink"):
        LookAtDrink()
    if (choice == "Shirt"):
        LookAtShirt()
    if (choice == "Go back"):
        MainRoom()

    
def InsideTrunk():
    global SnakeDodge
    coinflip = random.randint(0,1)
    if (SnakeDodge):
        ShowText("JK JK, no more snakes don't worry your phobia is kept safe with me")
        InsideTrunk
        return
    if coinflip == 0:
        print("Amazing! You dodged the snake")
        ChangeHealth(1)
    else:
        print("Yikes! Looks like you was bitten by the snake ")
        ChangeHealth(-1)
    SnakeDodge = True 

    
def LookAtDiary():
    EnterRoom("Diary")
    ShowText("Just blank pages...")
    LookInTrunk()

def LookAtDrink():
    EnterRoom("Drink")
    ShowText("You find a carton of milk, Do you want to drink it(Yes or No)")
    choice = PresentChoicesDynamic(["Yes", "No"])
    if choice == "Yes":
        DrinkMilk()
    if choice == "No":
        ShowText("You leave the milk and go back to looking in the trunk again")
        LookInTrunk()

def DrinkMilk():
    global MilkDrank
    coinflip = random.randint(0,1)
    
    if (MilkDrank):
        ShowText("You left it from before...tut tut")
        LookInTrunk()
        return

    if coinflip == 0:
        print("Luckily for you, The milk was fresh. ")
        ChangeHealth(1)
    else:
        print("You drank expired milk, good job")
        ChangeHealth(-2)
    MilkDrank = True
    ShowText("You go back to looking in the trunk")    
    LookInTrunk()


def LookAtShirt():
    EnterRoom("Shirt")
    ShowText("The smell of shirt, burns your nose")
    ChangeHealth(-1)
    ShowText("You were incorrect, Try again")
    LookInTrunk()


#Scenario 3 
def LookAtShelf():
    EnterRoom("Shelf")

def LookAtPicture():
    EnterRoom("Picture Frame")

def LookAtShipMap():
    EnterRoom("Ship Map")

StartGame()