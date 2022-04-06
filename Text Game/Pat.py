# import time
# import random
# import sys

# name = ""
# Delay = 1

# health = 5
# keys = 0
# a = 2
# b = 0.2
# c = 0.08


# print()
# print()
# print("     ######################")
# print("     |                    |")
# print("     |       WIGAN TEAM   |")
# print("     |                    |")
# print("     ######################")
# print()
# print()
# time.sleep(a)
# print("Wha... Welcome! This is an escape room")
# time.sleep(a)
# print("It's too dark to see anything...")
# time.sleep(a)
# print()
# startGame = input("Would you like to start the game? (Y/N): ")
# if startGame == "n" or startGame == "N":
#     print("Maybe next time")
#     time.sleep(3)
# elif startGame == "y" or startGame == "Y":
#     intro()

# def intro():
#     print()
#     print("(EVERYTHING IS DARK)")
#     time.sleep(a)
#     print("You feel around, using your hands to see.")
#     time.sleep(a)
#     print("The ground is cold, damp, and covered in thick vines.")
#     time.sleep(a)
#     print("You feel a round rock that sinks into the floor when you press it.")
#     time.sleep(a)
#     print("The ground starts rumbling.")
#     time.sleep(a)
#     print("Light begins flooding in.")
#     time.sleep(a)
#     print()


# def StartGame():
#     global health
#     global keys
#     print("You begin walking down the mountain toward the bottom")
#     time.sleep(Delay)

#     anyName = input("What is your name")
#     SetName(anyName)
#     print(anyName, " good name! now try to escape!")

#     health = 3
#     keys = 0

#     Room()