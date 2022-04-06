from secrets import choice
import time
import random
from xmlrpc.client import boolean

def startart():
        ShowText('''

██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      
                                                                                        
                                                                                        
███████ ███████  ██████  █████  ██████  ███████     ███████ ██   ██ ██ ██████           
██      ██      ██      ██   ██ ██   ██ ██          ██      ██   ██ ██ ██   ██          
█████   ███████ ██      ███████ ██████  █████       ███████ ███████ ██ ██████           
██           ██ ██      ██   ██ ██      ██               ██ ██   ██ ██ ██               
███████ ███████  ██████ ██   ██ ██      ███████     ███████ ██   ██ ██ ██      


                                                                                        
                                                                                  
        _    _                      _    _                         _    _
     __|_|__|_|__                __|_|__|_|__                   __|_|__|_|__
   _|____________|__           _|____________|__              _|____________|__
  |o o o o o o o o /          |o o o o o o o o /             |o o o o o o o o / 
~'`~'`~'`~'`~'`~'`~'`~       ~'`~'`~'`~'`~'`~'`~'`~         ~'`~'`~'`~'`~'`~'`~'`~

''')



name = ""
messageDelay = 1

health = 5
keys = 0
BananaEaten = False
MilkDrank = False
SnakeDodge = False
KeyFound = False
KeyFound2 = False
KeyFound3 = False


# Functions - Utilities
def SetName(desiredName):
    global name
    name = desiredName

def StartGame():
    global health
    global keys
    startart()
    print("Welcome! This is an escape room")
    time.sleep(messageDelay)
    print()
    desiredName = input("What is your name?")
    if desiredName == "Austin Powers":
        easter_egg()
    else:
        print(desiredName, "is a great name! Now try to escape!")
    SetName(desiredName)

    health = 5
    keys = 0

    MainRoom()

def easter_egg():
        print("""        YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY555555555555555555555555555555555555PPPPPP55P5555555555555555555555555555555555555555555555555555555555555555
        JYYYYYYYYYYYYJJJJJJJJJJJYYYYYYYYYYYYYYJYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5555YYJJ?77!!!77??JYYY55555555555555555YYYYYYYYYYYYY555555555555YYYYYYYYYYYYY555YY
        YYYYYYYYYYYYYJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?7!^::::...........:::^~!7JY55555555555YYYYYYYYYYY5555555555555555555YYYYYYY55555Y
        JJJJJJYJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJJ7~^:............................:~7?Y5555Y5YYYYYYYYYY55555555555555555555555YYYY55555Y
        JJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?!^::...................................:^!?Y55YYYYYYYYYYY555555555555555555555555YY55555Y
        JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYYYYYJJJJJJJYYYYYYYYJYY?!^.:::::......................................:~7JYYYYYYYYYY5555555555555555555555555Y555555
        JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYJ?^:::::::::.....................................::..:~7YYYYYYYYYY555555555555555555555YYYYYYY5Y
        JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYY?~^::::::::..........................................:::.:!?YYYYYYYY555555555555555555YYYYYYYYYYY
        JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYJ!^^^^::::..::...........................................:::::~?YYYYYY55555555555Y5555YYYYYYYYYYYYY
        ?JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYJ7~~^^^:::::..:::............................................:::::~JYYYY5555555YYYYYYYYYYYYYYYYYYYYYY
        JJJJJJJJJJJJJ?????????JJJJJJJJJJJJJJJJJJJJJJJJYJ?~~~^^^^::::...:::..............................................:::.:7YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        ??JJJJJJJJ????JJ??????????JJJJJJJJJJJJJJJJJJJY?!~~~~~^^:::::....::........................................::.....:::::!5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        ????J??????JJ??????????JJJJJJJJJJJJJJJJJJJJJJ!~!~~~~^^^::::::...:.................................::::.:::::.....:::^^:!5YYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        ????????????????????????JJJ?????JJJJJJJJJJJ?~!!~~~~~^^^^:::::.:::....................................::::::::......::^^:!5YYYYYYYYYYYYYYYYYYYYYYYYYYYY
        ??????????????????????JJJJJ???J??????JJJJJ?~~!~~^~~~^^^^^::::.::::............................::::::::::::::::::::::::^^^75YYYYYYYYYYYYYYYYYYYYYYYYYYY
        ????????????????????????JJJJJJJJ?????JJJJ?~~!!~~~~~~~^^^^:::::::::::::........................:::::::::::::::::::::::::^~^J5YYYYYYYYYYYYYYYYYYYYYYYYYY
        ?????????????????????????????????????JJJ?7!!!!~^^^^~~~^^^::::::.::::::.:..:::::::.......::::^^^^^^:::::::::^::::::^^^^:^~^~YYYYYYYYYYYYYYYYYYYYYYYYYYY
        ???????????????????????????????????????J?!!7!!~^^^^^^^^^^:::^^:.......::..:::........::::::.:::::::::::::^^::^^^:^^^^~^^^~:?5YYYYYYYYYYYYYYYYYYYYYYYYY
        ???????????????????????????????????????J?777!!~~^^^^^^^^::::^^::::::::::......::::::::....:::.......::::^^^^^^^^^^^^^^^:^~^~JYYYYYYYYYYYYYYYYYYYYYYYYY
        ???????????????????????????????????????JJ??7!!~^^^^^^^^::::::::::::::::.....::::.........::::::^~!~~~^:::^^^^^^^^^^::^^:^^^^!YJYYYYYYYYYYYYJJJJJYYYYYY
        ??????????????????????????????????????JJJ?777~^^^^^^^^^::::::::.:...:::::...::.........:::^~!!7?J??JJ7!~^^^^^^^:^:::^^::^^~~^?YYJJJYYYYYJJJJJJJJYYYYYY
        ???????????????????????????????????????YJJ??7!^^:^^^^^^^^::::::.:...::::::::::......:::^~!7?J???!~~!7JJ?!~~~~^^^^^^^^^::^^~~^!YYJJJJYYYYJJJJJJJJJJYYYY
        ???????????????????????????????????????YJJ??7~^^^^^^:^:::::::::::...::::::::::::::~~~777!?JJ7~:::::^^^~77~^~~^^^^^^^^^^^^^~~~!YYJJYJYYJYJJJJJJJJJJJYYY
        ???????????????????????????????????????YJJ??7??J?7777!!~^^^^:^^^:::~:::^^^::^::^~!!!7??JJ7~^::::::^^^:^^~~^~~^^^^^^^^^^^^~~~~7YYYYYJJJJJJJJJJJJJJJJJYJ
        7??????????????????????????????????????YJ?JJJYJ55JYYJ??7?7~!~~~~^:~!^^^^^^^^^^~!!!!77??7!^::^:^:::::::::^!~~^^^^^^^^^^~^~~^^~?YYJJJJJJJJJJJJJJJJJJJJJJ
        77??????????????????7777???????????????JY?YY??????JYY555YY?7???7!?J~^^^^^~~~~!!!777??7!~~~~~~~^^^::::::^^~~^^^^^^^^^~~~~~~^~!?YYYJJJJJJJJJJJJJJJJJJJJJ
        777????????????????777777?????????????7?YY5YJ?77??JY5PPBGP5555Y?7??!!~~~~~!!!!7?JJ??7777!7!!!!777!!!~^^^^~~^~^^^^^^~~~~~^~~!:!J77JYYJJJJJJJJJJJJJJJJYY
        7777???????77777??77777777?????????????JYY55YYY?77!~!!!?JY5PPGP5YJ7!~~~^^~~~!7?J??77???J77JJ!!!~!777!!~~^^~~~^^~~^~~~~~~~!~^^:::???JJJJJJYJJJJYYYYYYYY
        77777?????77777777777777777????????????JYYYYPYJ7!!!!77777!?JY555PP?~^::::::^~77!!!???JJ?5PB5GPPJJ7!!~!~^^^~~^^^~^^~~~~~~!^:^^:~?GJ!YYJJJYYYYYYYYYYYYYY
        77777777777777777777777777??????????????YJJJ5JJ5PYY5PGGB&BGP555JJ5?^:::::::^~~^^^~7JY?^~JYB5GYJ?JJ7~^::::^^:::^^^~^~~~~~~~^^^~?7JY!JJJJJYYYYYYYYYYYYYY
        7777777777777777777777777???????????????YJ??J?5PGGPP55Y??7!!!!?!!?!:::..:::^^^^:::~!!!7!77!!~!!!!!~^::::^^:::^^^~~~~~!~^^~~~!7!^~?!JYJJJJYYYYYYYYYYYYY
        7777777777777777777777777???????????????YJJ?7~!?Y5Y?77!!!~~!!~~~7?^::...:::^^^:::^~7??777777777!!~::::::^^::^^^^~~~~~~~^^~~!YY!~!!~YYYJYYYYYYYYYYYYYYY
        7777777777777777777777777???????????????JY?!77~~~7??J????7!~~^^~?!......::^^~^^^^:^^~!!!77777!~^:::::::^::::^^^^~~~~~~^^^~^^JJ!~!~~YYJYYYYYYYYYYYYYYYY
        77777777?77777777777777777?????????????7JY!!7!~:::::^^^::^^:::^7?^:.....:^~^^~^^^^:::::::::::::...::::::::::^^^~^~^^~~^^^~^::~^^^^^YYYYYYYYYYYYYYYYYYY
        !77777777777777777777777777?????????????YJ~7!~~^:::::::::::::^!J!::....::^~~~~~^^^^::::::::::.....:::::::::^^^~~~~~^^~^^^~^:^^^^:~^JYYYYYYYYYYYYYYYYYY
        !!7777777777777777777777777?????????????Y?!?!~~^^^:::::::::::~7?^:....:::^~~~^^~^^^^::::::......:::::::::::^^^~~~~~~~^^^~~^:^^^~^^:?YYYYYYYYYYYYYYYYYY
        !!!!!7777777777777777777777????????????7J???!!!~~^^^::::::::^!?~::.....::^~~~^^^^^^^^^::........:::::::::^^^~~~~~~~~~^~^~~~^~~^~~^:?5YYYYYYYYYYYYYYYYY
        ~~~~!!!!!777777777777777777?????????????P77J7!!!!~^^:::::::^!77^:......::^~~^^^^^^^^^^::......:::::::^^:^^^^~~~~~~~~~~~^~~~^:~^~~^~YYYYYYYYYYYYYYYYYYY
        ^^^^~~~~~!!!!!!!777777???????????????77?PJ^J??77!~~^^:::::^~!7!~^:.....::^^^^:^^^^^~~^^::::.:::::::^^^^^^^~~~~!~~~~~~~~~~~~::^~^7!7YYYYYYYYYYYYYYYYYYY
        ^^^^^^^^^^~~~~~~!!!!!!7777777?????????7J5577J???77!~^:^:^^^~!J?~^::::::^^~!~^^^^~^:^~^^^:::::::^:^^^^^^^^~~~~!~~~~~~~~^~~~?^:^~~7!JYYYYYYYYYYYYYYYYYYY
        ::::::::^^^^^^^^~~~~~~~!!!!7777???????7Y55Y~?J???77!~^^^^^~~!55?!~~^^^~!!!7?JJ?7!:::^~^^^^::^^^^^^^^^^^^^~~~!!~~^^^~^^^~^~P!:^~!~?5YYYYYYYYYYYYYYYYYYY
        ::::::::::::::::^^^^^^^^~~~~!!!!!777777Y5557!JJJJ?77!~^^^^~!?PGP5J?777??JYPPYJ?7~:::::^^^^^^^^^^^^^^^^~~~~~~~~~^^^^^^~~~~!P!^^~!!YYYYYYYYYYYYYYYYYYYYY
        :::::::::::::::::::::^^^^^^^^^~~~~~~~!~?PPPY!?????7777!^^~!7J55PP5PPPPPGPJ7!^:^::::::::^^^^^^^^^^^^^^^~^~~~~~~~~~^^^^~~~^7P?!!!!JYYYYYYYYYYYYYYYYYYYYY
        :::::::::::::::::::::::::::::^^^^^^^^^^~7JY5Y77?7??7!!!!~~!7JY55555P5YJ7~^::::::::::::::^^^~~~~^^^^^~^^~~~~~~~~^^^^^~^~~~?GP5YJJ?77??JJJYY55YYYYYYYYY5
        :::::::::::::::::::::::::::::::::::::::::::J57?J7??7!77!!7~~!7?JJ?7!~~^::::::::::::^^^^^^^~!!~~~^^^^^^~~~~~~~~^^^^~~^~~~~7BGP5YJ?7!!!!!7777???JJJJYYYY
        :::::::::::::::::::::::::::::::::::::::.:::?5Y!J?7??!7777!!!^~~~~!~::::^^:::::::^^^^~~^~~^^~!~^^^^^^^~~~~~~~~~^^~^^~~~!~!J#BGP5Y?777!!!!!!!!!!!!!!!777
        ::::::::::::::::::::::::::::::::::::^~7??J55Y5!7?77?7?7?777!^^^^^!~^^^::^^:^::^^^~~~~~^^~~~^^^~~^^^~~~~~~~~^~~~~~~~~~!!!?5##BBGY?777777777777777777777
        ::::::::::::::::::::::::^^^^^^^~~7?JY55PPPPP5Y?7J7??7??J77?777?JJJY?!!!!77!!!!!!!!~~!~~~~~~~~^^~^^~~~~~~~~~^~~~~~~~~!!?YJJB#&#G5JJJJJ??777777777777777
        :::::::::^^^~~~!!!77777????JJJJYYYY5555PPPPG5Y?!J??J???YY5PGG5?!~^75GP5PGGGGP5YYYJYYJJJJ?77!~~^~^~~!~~~~~~~~~~~~~!!!7JYJ??JJYBBG5YJJJ???77777777777777
        ::^^~~!!!!7777777777777777???JJJYYYY5555PPGPG5Y??J?YJ?7JYY7~^:::^^~7GP5YYJJ?!!!7?J?777!~~~~~~~~~!77!!~~~~~~!!!!!!7!?Y5?77???7YBG5JJJJJ??77777777777777
        !!7!!!!!!!!!!!!!!!!!!!!777777???JJJYY55PPGGGBB5YJJYJY?!^:...::^^~!?J?!!7!7!!!7?YYYJ?!!!~~~~^~~!!?7!!~~~~~!!!!!!777J55YJ?7?7!77GG5YJJJJ?????7777777777!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!777????JYY55PP5YJP#B5J!~::...:::^~!7?5PYJJJJYYYY5P55YJ7!~~~~~~~~~!!!7!~~~~~~!!!!777??7YP55J77!?7!!?GG5YYYJJ?????777777777!!
        !!!!!!!!!!!!!!!!!!~~~~~~!!!!!777???JJJ7^:.:!5J~::.....::~!7?J55PPPGGBBBBBGP5J7!~~~~~~~~~~~~!!77!~~~~~!!!777???!?5P5J7!!!!?!7!?PP5YYJJJJJJ??7777!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!~~~~!!!!!!!77?7~:  ^?!!~...:::::^~!7?JYYYYYY5P5J?7!~^:::::^^^^^~^^^~~!!77!~~~~!!!!7????7J5P5J7!77!!77!!!JGPYYJJJJJ??77!!!!!77!!!!
        ~~~~~~!!!!!!!!!!!!!!~~~~~!~~!!!!!!7^:.  ^?:^::.:^~~!!!JY55YYJ??J?777!~^:^::^::^^^^^^^^^~~!7777~~~~!!!!7??JY5PPY?7!!777!!?!!!75P5JYJJJ??777777777777!!!
        ~~~~~~~~~!!!!!!!!!!~~~~~~~~~~!!!!!7?77~:^!::!~^^^~!?PGGPPPP5YJJ?!!!7!~~~~~~~^^^~~~~~~~!!7???7!~!!!!77JY5PPP5YJ?!!!!!!77!?!!7J5YJJJ??777!!7777777!!!!!!
        ~~~~~~~~~~~~!!!!!!!!~~~~~~~~~!!~^~~~~~~^~?77J?!!77!7?Y5PP55PPP5YJ?7!7!!!!!!!!!!!!!!77?JYJ?77!!!!77?YPGPP5YJJ7!!!!!!!!!77J??J5YYJ??7777!!!!7!!!!!~!!!!!
        ~~~~~~~~~~~~~~!!!!!!!~~~~~~!!~^:::.   ..::7YJ7!!!:.   ..:::^^^^~!7YYJJJ????JJYYYJYY55YYJ???777?JYPGGPP5YJJ?7!!!7!!!7777?JYYYJJ???7777777!!!!!!~~~!!!!!
        ~~~~~~~~~~~~~~!!!!!!~~!!~~!!^^..  ....::^^^~JJ!^........::::^^..::!PBGGPPPPPPPGGPP55YJJJJJYY5PGGGG55YYJ?77!!!!!!!!!777?JJYJ???????7777!!!!!~~~~~!~!!!!
        ~~~~~~~~~~~~~~~~~~!!!!~~!!7~:......:::::^^^^^~^::..:...::^^^^~:.:^^7&##BBBGGGPP555555PPPGGGBBGGP5YYJJ?77!!!!!!!!!!77??JJ?????777777!!!!!!~!!~~~~!~!!!!
        ~~~~~~~~~~~~~~~~~!~!!!!!77~.......:::::^~~~^:^J!~~~:....::^^~^..:^^J#B####BBBBBBBBBBBBBBBBGPP5YYYJJ?7777!!!!!!!!77?JJJ??77777777!!~~~~~~~~!!!!!!!~!!!!
        ~~~~~~~~~~~~~~~~~!!~~!7?7^.......::::^~!7!~^^~55JJ~......:::~:..:^^7G##B#######&BGGGGGPP55YYYYYJ??77!!!!!!!!77???????77!!!!!!!!~~~~~~~~~~~!!!!!!!!!!!!
        ~~~~~!!!~~~~~~~~~~!~!7?!:.......:::^!7?J?777?Y5G#?.........^^...:^~:~5&######BBBYYYYYYYYYYYJJ??7777!!!!!77777??77!!!!!!~~!!~~~~~~~~~~~~!!!!!!!!~!!!!!!
        ~~~~~~!!!~~~~~~~~~!7?7: ........::^~7Y5YY555GGGBG~:......:^~:..::^~:^^G#BBGGG5PBJJJJJJ?????77!!!!!!!77777777!!!~~~~~~!!!~!!~~~~~~~~~~~!!!!!!!!!!!!!!!!
        ~~~~~!!!!!~~~~~~!7?7^..........::^~!JJYPPPP5PB#&Y::.....::~:::::^~:.:^J7~~~!555#J??7777777!!777777777!!!!!!!~~~~~~~~~!!!!!!~~~~~~~~~~!!!!!!!!!!!!!!!!!
        ~~~~~!!!!!~~~~~!?7~...........::^~!?YY??JJJY5B#B?^:::::^^~:.:^^^~~..^7!^^^^^J5YBY7?7777???JJJ???77!!!~~~!!!~~~~~~~~~!!!!!!!~~~~~~~~~~!!!!!!!!!!!!!!!!!
        !~~~!!!!!!!!~!7?7^..........:::^~~?Y?~~^^^~!7JP?:::.:^^^~:..:^^~!:..^?~~^^~!Y5JY5?JJJJJYJYJJ?777!!!!!!!!!!!!~~~~~~~~!!!!!!~!~~~~~~~~~!!!!!~!!!!!!!!!!!
        ~~~~!!!!!!!!!77!^:........:::::^~!??~::::::^~7!^::::^^!7^.::^^~!^.::^7~~~~7?Y5555JJJYYJJJJJ?77!!!!!!!!!!!!!!!~~~~~~~!!!!!!!!!!~~~~~~~~!!~~~!!!!!!!7!!!
        ~~~~!!!!!!!77!~^.........:::::^~!??~:::::::^~7~::^^~~??^:::~~77~::::^~!!!7?!!?JJJJJJJJJJJ?777!!!!~~~~!!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~~~~~!!!!!!!7!!!!
        ~~~~!!!!!!7?!^:.........:::::^~~7?!:..::::^!7~:^^~!7P5^^::^~?5!^^^^^^!!!!77~!Y?JJJJJ?JJJ??77!!!!!~~~~!!!!!!!!!~~~~~~~!!!!!!!!!!~~~~~~~~~!!!!!!!!!7!!!!
        ~~!!!!!!!??7^::........:::::^~~!?7~..::::^~??^^^^!?P#5!~^~~!BG!^^^:^~77777!~:!????J???????7!!!!~!!~~~!!!!!!!!!!~~~~~~~~!!!!!!!!!~~~~~~~~!!!!!!!!!7!!!!""")
        time.sleep(2)
        print("OH BEHAVE")
        time.sleep(2)
        easter_egg = False
    


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
        x = input().strip().capitalize()

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
    elif (choice == "Floor"):
        LookAtFloor()
    elif (choice == "Trunk"):
        LookInTrunk()
    else:
        print("Input not recognised")
        MainRoom


def LookAtWall():
    EnterRoom("Wall")
    ShowText("There are items on the wall")
    ShowText ("Which item will you inspect?")

    choice = PresentChoicesDynamic(["Shelf", "Picture Frame", "Map of the Ship", "Go Back"])

    if (choice == "Shelf"):
        LookAtShelf()
    elif (choice == "Picture Frame"):
        LookAtPicture()
    elif (choice == "Map of the Ship"):
        LookAtShipMap()
    elif (choice == "Go Back"):
        MainRoom()
    else: 
        print("Input not recognised")
        LookAtWall ()


def LookAtShelf():
    EnterRoom("Shelf")
    ShowText("Unlucky! You search through piles of junk, this shelf is a real dumping ground! What a waste of time!")
    ChangeHealth(-1)
    ShowText("No key was found. You lose one of your lives.")
    LookAtWall()
    
def LookAtPicture(): #! currently broken
    EnterRoom("Picture Frame")
    ShowText("You pull at the painting and it drops on your foot! Ouch! You wasted a lot of time recovering from that one.")
    ChangeHealth(-1)
    ShowText("Unlucky! No key was found. You lose one of your lives.")
    LookAtWall()

map1 = False

def LookAtShipMap(): #! currently broken 
    global KeyFound2
    EnterRoom("Ship Map")
    if (KeyFound2):
        ShowText("You already took the key don't be greedy")
        LookAtFloor()
        return
    ShowText("Congratulations! You found a key.")
    ShowText("Great work! Now maybe this map could help you escape...")
    ShowText ("Would you like to keep the map?")
    if ("yes"):
        map1 == True 
    elif ("no"):
        map1 == False 
            

    KeyFound2 = True 
    Changekeys(1)
    LookAtWall()


#?Scenario 2 

def LookAtFloor():
    EnterRoom("Floor")
    ShowText("You look at the floor")
    ShowText("There is a Snack, Rug and Shoe")

    choice = PresentChoicesDynamic(["Snack", "Rug", "Shoe", "Go back"])

    if (choice == "Snack"):
        LookAtSnack()
    elif (choice == "Rug"):
        LookAtRug()
    elif (choice == "Shoe"):
        LookAtShoe()
    elif (choice == "Go back"):
        MainRoom()
    else: 
        print("Input not recognised")
        LookAtFloor

def LookAtSnack():
    EnterRoom("Snack")
    ShowText("You find a banana, Do you want to eat it(Yes or No)")
    choice = PresentChoicesDynamic(["Yes", "No"])
    if choice == "Yes":
        EatBanana()
    elif choice == "No":
        ShowText("You drop the banana and go back to looking at the floor")
        LookAtFloor()
    else: 
        print("Input not recognised")
        LookAtSnack ()


def EatBanana():
    global BananaEaten
    coinflip = random.randint(0,1)

    if (BananaEaten):
        ShowText("There is a banana peel here, you already ate the banana")
        LookAtFloor()
        return

    elif coinflip == 0:
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

shoes1 = False

def LookAtShoe():
    global KeyFound
    global shoes1
    EnterRoom("Shoe")
    if (KeyFound):
        ShowText("You already took the key don't be greedy")
        LookAtFloor()
        return
    ShowText("Congratulations!, You have found a key")
    ShowText("Great work! These shoes look a lot better than your current ones this could help you escape...")
    ShowText ("Would you like to take the shoes?")
    choice = PresentChoicesDynamic(["Yes", "No"])
    if choice == "Yes": 
        shoes1 == True 
        ShowText("Shoes Taken")
    elif choice == "no":
        shoes1 == False 
            
    KeyFound = True 
    Changekeys(1)
    LookAtFloor()
    
#?SCENARIO 3 -

def LookInTrunk():
    EnterRoom("Trunk")
    print("SNAKE!!!!!")
    InsideTrunk()
    ShowText("You see other things in the trunk.")

    choice = PresentChoicesDynamic(["Diary", "Drink", "Shirt", "Go back"])

    if choice == "Diary":
        LookAtDiary()
    elif choice == "Drink":
        LookAtDrink()
    elif choice == "Shirt":
        LookAtShirt()
    elif choice == "Go back":
        MainRoom()
    else:
        print("Input not recognised")
        LookInTrunk()

    
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
    global KeyFound3
    EnterRoom("Diary")
    if (KeyFound3):
        ShowText("You already took the key don't be greedy")
        LookAtFloor()
        return
    ShowText("Congratulations! You found a key.")
    ShowText("Great work! Now you're just looking at a bunch of blank pages")
    KeyFound3 = True 
    Changekeys(1)
    LookAtDiary()
# currently takes back to main screen if diary is done first 

def LookAtDrink():
    EnterRoom("Drink")
    ShowText("You find a carton of milk, Do you want to drink it(Yes or No)")
    choice = PresentChoicesDynamic(["Yes", "No"])
    if choice == "Yes":
        DrinkMilk()
    elif choice == "No":
        ShowText("You leave the milk and go back to looking in the trunk again")
        LookInTrunk()
    else: 
        print("Input not recognised")
        LookAtDrink ()

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

#?keys check

def keys_Lastcheck():
    global keys
    if keys == 3:
        print("you have all the keys!")
        good_ending_keys()
    elif keys == 2:
        print ("missing a key!")
        bad_ending_keys()
    elif keys == 1:
        print ("missing 2 keys!")
        bad_ending_keys()
    elif keys == 0:
        print ("No keys were collected!")
        bad_ending_keys()

def good_ending_keys():
    print("You’ve found all of the keys! You rush over to the door and quickly unlock it and run out into the corridor...")
    time.sleep(1)    
    print("You proceed to the escape!")
    time.sleep(1)
    print("Your actions will now be judged")

def bad_ending_keys():
    print("You’ve wasted too much time and didnt find the keys, the water has risen too high, you’re sleeping  with the fishies tonight!")
    time.sleep(2)
    print("Better luck next time!")
    time.sleep(2)
    play_again = input("would you like to play again? [Y/N] ")
    if play_again.upper() == "Y" or play_again.upper() == "YES":
        StartGame()
    elif play_again.upper() == "N" or play_again.upper() == "NO":
        print("Farewell.")
        time.sleep(1)
        print("GAME HAS ENDED")
    else: 
        print("Input not recognised please try again")
        bad_ending_lives()

#?lives check

def health_last():
    global health
    if health == 7 > 8:
        good_ending_lives3()

    elif health == 4 < 6:
        good_ending_lives2()

    elif health == 1 < 3:
        good_ending_lives1()

    elif health == 0:
        bad_ending_lives()    

def Death ():
    print ('''

              ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

''')

def the_end():
    print ('''


████████ ██   ██ ███████     ███████ ███    ██ ██████  
   ██    ██   ██ ██          ██      ████   ██ ██   ██ 
   ██    ███████ █████       █████   ██ ██  ██ ██   ██ 
   ██    ██   ██ ██          ██      ██  ██ ██ ██   ██ 
   ██    ██   ██ ███████     ███████ ██   ████ ██████  
                                                       
   ''')       

def bad_ending_lives():
    print("You’ve wasted too much time and the water has risen too high, you’re sleeping  with the fishies tonight!")
    Death ()
    time.sleep(2)
    print("Better luck next time!")
    the_end ()
    time.sleep(2)
    play_again = input("would you like to play again? [Y/N] ")
    if play_again.upper() == "Y" or play_again.upper() == "YES":
        StartGame()
    elif play_again.upper() == "N" or play_again.upper() == "NO":
        print("Farewell.")
        print 
    else: 
        print("Input not recognised please try again")
        bad_ending_lives()

def good_ending_lives3():
    print("you are healthy and have survived the ship, but now lets see if you can escape it!")
    time.sleep(2)
    map_and_shoes1()

def good_ending_lives2():
    print("you have hurt yourself a bit but managed to survived the ship, but now lets see if you can escape it!")
    time.sleep(2)
    map_and_shoes1()

def good_ending_lives1():
    print("you have really hurt yourself while in the ship but surpisingly you are still standing, now lets see if you can escape it!")
    time.sleep(2)
    map_and_shoes1()




#!exits check

def map_and_shoes1():
    if map1 and shoes1 == True:
        trainer_map_t()
    elif map1 == False and shoes1 == True:
        trainer_t_map_f()
    elif map1 == True and shoes1 == False:
        trainer_f_map_t()
    elif map1 == False and shoes1 == False:
        trainer_f_map_f()

def Helicopter (): 
    print ('''
`--------------------------`()'--------------------------'
                            ||
                         __ ||                                        __
                         ] """"---...._                             .' /
                   _,-"""==============`--.                       .'/)/
                 ,' ) ,--. .-----.         `.___________________.' ///_
               .'  / /___| |_____|  e c      G-DMG       _______  ()  _>
              /   / /____| |__|__|             ,----"""""       `//  |
            .<`=='===========================.'                 (/`.  |
           (  `.----------------------------/                       `._|
            `-._\_                ____...--'
                  """--ii--'"""77"
                 .____//______//___,
                 `-----------------'

''')

def trainer_map_t():
    print("“With your trusty map and shoes you speed through the decks with alarming speed. You're first to the rescue helicopter so get to choose the best seat!”")
    Helicopter ()

def trainer_t_map_f():
    print("You are wearing snazzy shoes but don’t have a map, you run around lost for a while and eventually find your way to the deck. Just in time to grab the last seat  on the rescue helicopter!")
    Helicopter ()

def trainer_f_map_t():
    print("You have the map and know your way around but you are still wearing crappy shoes.  You rush as fast as you can to the deck and just barely manage to grab the last seat on the rescue helicopter")
    Helicopter ()
    
def trainer_f_map_f():
    print("You don’t have a map or the right shoes so you get lost and move slowly. By the time you get to the deck the helicopter has left without you!")
    Death ()


StartGame()




