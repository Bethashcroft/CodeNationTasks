# # import time

# # key1 = 1
# # key2 = 1
# # key3 = 1
   


# # Key_test = sum([ key1, key2, key3])

# # def keys():
# #     if Key_test == 3:
# #         print("you have all the keys!")
# #         good_ending_keys()
# #     elif Key_test == 2:
# #         print ("missingf a key!")
# #         bad_ending_keys()
# #     elif Key_test == 1:
# #         print (" missing 2 keys!")
# #         bad_ending_keys()
# #     elif Key_test == 0:
# #         print ("No keys were collected!")
# #         bad_ending_keys()

# # def good_ending_keys():
# #     print("You’ve found all of the keys! You rush over to the door and quickly unlock it and run out into the corridor...")
# #     time.sleep(1)    
# #     print("Proceed to escape ending depending on options chosen")

# # def bad_ending_keys():
# #     print("You’ve wasted too much time and didnt find the keys, the water has risen too high, you’re sleeping  with the fishies tonight!")
# #     time.sleep(2)
# #     print("Better luck next time!")
# #     time.sleep(2)
# #     play_again = input("would you like to play again? [Y/N] ")
# #     if play_again.upper() == "Y" or play_again.upper() == "YES":
# #         start_game()
# #     elif play_again.upper() == "N" or play_again.upper() == "NO":
# #         print("Farewell.")
# #         time.sleep(1)
# #         print("GAME HAS ENDED")
# #     else: 
# #         print("Input not recognised please try again")
# #         bad_ending_lives()

# # lives1 = 1
# # lives2 = 1
# # lives3 = 1
   


# # lives_test = sum([ lives1, lives2, lives3])

# # def lives():
# #     if lives_test == 3:
# #         lives_total =3
# #         good_ending_lives3()

# #     elif lives_test == 2:
# #         lives_total =2
# #         good_ending_lives2()

# #     elif lives_test == 1:
# #         lives_total =1
# #         good_ending_lives1()

# #     elif lives_test == 0:
# #         bad_ending_lives()    



# # def bad_ending_lives():
# #     print("You’ve wasted too much time and the water has risen too high, you’re sleeping  with the fishies tonight!")
# #     time.sleep(2)
# #     print("Better luck next time!")
# #     time.sleep(2)
# #     play_again = input("would you like to play again? [Y/N] ")
# #     if play_again.upper() == "Y" or play_again.upper() == "YES":
# #         start_game()
# #     elif play_again.upper() == "N" or play_again.upper() == "NO":
# #         print("Farewell.")
# #         time.sleep(1)
# #         print("GAME HAS ENDED")
# #     else: 
# #         print("Input not recognised please try again")
# #         bad_ending_lives()

# # def good_ending_lives3():
# #     print("you are healthy and have survived the ship, but now lets see if you can escape it!")
# #     time.sleep(2)
# #     map_and_trainers()

# # def good_ending_lives2():
# #     print("you habe hurt yourself a bit but managed to survived the ship, but now lets see if you can escape it!")
# #     time.sleep(2)
# #     map_and_trainers()

# # def good_ending_lives1():
# #     print("you have really hurt yourself while in the ship but surpisingly you are still standing, now lets see if you can escape it!")
# #     time.sleep(2)
# #     map_and_trainers()




# # map = True
# # trainers = True

# # def map_and_trainers():
# #     if map and trainers == True:
# #         map_trainer_t()
# #     elif map == False and trainers == True:
# #         trainer_t_map_f()
# #     elif map == True and trainers == False:
# #         trainer_f_map_t()
# #     elif map == False and trainers == False:
# #         trainer_f_map_f()



# # def map_trainer_t():
# #     print("“With your trusty map and trainers you speed through the decks with alarming speed. You're first to the rescue helicopter so get to choose the best seat!”")

# # def trainer_t_map_f():
# #     print("You are wearing snazzy trainers but don’t have a map, you run around lost for a while and eventually find your way to the deck. Just in time to grab the last seat  on the rescue helicopter!")

# # def trainer_f_map_t():
# #     print("You have the map but are still wearing crappy shoes, you rush as fast as you can to the deck and manage to grab the last seat on the rescue helicopter")

# # def trainer_f_map_f():
# #     print("You don’t have a map or the right shoes so you get lost and move slowly. By the time you get to the deck the helicopter has left without you!")









# # def name_check1():
# #     name = input("enter your name")
# #     if name == "Austin Powers":
# #         print("test1")
# #         easter_egg()
# #     else:
# #         print("all good")
    
# # def easter_egg():
# #         print("""YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY555555555555555555555555555555555555PPPPPP55P5555555555555555555555555555555555555555555555555555555555555555
# #         JYYYYYYYYYYYYJJJJJJJJJJJYYYYYYYYYYYYYYJYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5555YYJJ?77!!!77??JYYY55555555555555555YYYYYYYYYYYYY555555555555YYYYYYYYYYYYY555YY
# #         YYYYYYYYYYYYYJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?7!^::::...........:::^~!7JY55555555555YYYYYYYYYYY5555555555555555555YYYYYYY55555Y
# #         JJJJJJYJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJJ7~^:............................:~7?Y5555Y5YYYYYYYYYY55555555555555555555555YYYY55555Y
# #         JJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?!^::...................................:^!?Y55YYYYYYYYYYY555555555555555555555555YY55555Y
# #         JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYYYYYJJJJJJJYYYYYYYYJYY?!^.:::::......................................:~7JYYYYYYYYYY5555555555555555555555555Y555555
# #         JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYJ?^:::::::::.....................................::..:~7YYYYYYYYYY555555555555555555555YYYYYYY5Y
# #         JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYY?~^::::::::..........................................:::.:!?YYYYYYYY555555555555555555YYYYYYYYYYY
# #         JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYJ!^^^^::::..::...........................................:::::~?YYYYYY55555555555Y5555YYYYYYYYYYYYY
# #         ?JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYJ7~~^^^:::::..:::............................................:::::~JYYYY5555555YYYYYYYYYYYYYYYYYYYYYY
# #         JJJJJJJJJJJJJ?????????JJJJJJJJJJJJJJJJJJJJJJJJYJ?~~~^^^^::::...:::..............................................:::.:7YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ??JJJJJJJJ????JJ??????????JJJJJJJJJJJJJJJJJJJY?!~~~~~^^:::::....::........................................::.....:::::!5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ????J??????JJ??????????JJJJJJJJJJJJJJJJJJJJJJ!~!~~~~^^^::::::...:.................................::::.:::::.....:::^^:!5YYYYYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ????????????????????????JJJ?????JJJJJJJJJJJ?~!!~~~~~^^^^:::::.:::....................................::::::::......::^^:!5YYYYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ??????????????????????JJJJJ???J??????JJJJJ?~~!~~^~~~^^^^^::::.::::............................::::::::::::::::::::::::^^^75YYYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ????????????????????????JJJJJJJJ?????JJJJ?~~!!~~~~~~~^^^^:::::::::::::........................:::::::::::::::::::::::::^~^J5YYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ?????????????????????????????????????JJJ?7!!!!~^^^^~~~^^^::::::.::::::.:..:::::::.......::::^^^^^^:::::::::^::::::^^^^:^~^~YYYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ???????????????????????????????????????J?!!7!!~^^^^^^^^^^:::^^:.......::..:::........::::::.:::::::::::::^^::^^^:^^^^~^^^~:?5YYYYYYYYYYYYYYYYYYYYYYYYY
# #         ???????????????????????????????????????J?777!!~~^^^^^^^^::::^^::::::::::......::::::::....:::.......::::^^^^^^^^^^^^^^^:^~^~JYYYYYYYYYYYYYYYYYYYYYYYYY
# #         ???????????????????????????????????????JJ??7!!~^^^^^^^^::::::::::::::::.....::::.........::::::^~!~~~^:::^^^^^^^^^^::^^:^^^^!YJYYYYYYYYYYYYJJJJJYYYYYY
# #         ??????????????????????????????????????JJJ?777~^^^^^^^^^::::::::.:...:::::...::.........:::^~!!7?J??JJ7!~^^^^^^^:^:::^^::^^~~^?YYJJJYYYYYJJJJJJJJYYYYYY
# #         ???????????????????????????????????????YJJ??7!^^:^^^^^^^^::::::.:...::::::::::......:::^~!7?J???!~~!7JJ?!~~~~^^^^^^^^^::^^~~^!YYJJJJYYYYJJJJJJJJJJYYYY
# #         ???????????????????????????????????????YJJ??7~^^^^^^:^:::::::::::...::::::::::::::~~~777!?JJ7~:::::^^^~77~^~~^^^^^^^^^^^^^~~~!YYJJYJYYJYJJJJJJJJJJJYYY
# #         ???????????????????????????????????????YJJ??7??J?7777!!~^^^^:^^^:::~:::^^^::^::^~!!!7??JJ7~^::::::^^^:^^~~^~~^^^^^^^^^^^^~~~~7YYYYYJJJJJJJJJJJJJJJJJYJ
# #         7??????????????????????????????????????YJ?JJJYJ55JYYJ??7?7~!~~~~^:~!^^^^^^^^^^~!!!!77??7!^::^:^:::::::::^!~~^^^^^^^^^^~^~~^^~?YYJJJJJJJJJJJJJJJJJJJJJJ
# #         77??????????????????7777???????????????JY?YY??????JYY555YY?7???7!?J~^^^^^~~~~!!!777??7!~~~~~~~^^^::::::^^~~^^^^^^^^^~~~~~~^~!?YYYJJJJJJJJJJJJJJJJJJJJJ
# #         777????????????????777777?????????????7?YY5YJ?77??JY5PPBGP5555Y?7??!!~~~~~!!!!7?JJ??7777!7!!!!777!!!~^^^^~~^~^^^^^^~~~~~^~~!:!J77JYYJJJJJJJJJJJJJJJJYY
# #         7777???????77777??77777777?????????????JYY55YYY?77!~!!!?JY5PPGP5YJ7!~~~^^~~~!7?J??77???J77JJ!!!~!777!!~~^^~~~^^~~^~~~~~~~!~^^:::???JJJJJJYJJJJYYYYYYYY
# #         77777?????77777777777777777????????????JYYYYPYJ7!!!!77777!?JY555PP?~^::::::^~77!!!???JJ?5PB5GPPJJ7!!~!~^^^~~^^^~^^~~~~~~!^:^^:~?GJ!YYJJJYYYYYYYYYYYYYY
# #         77777777777777777777777777??????????????YJJJ5JJ5PYY5PGGB&BGP555JJ5?^:::::::^~~^^^~7JY?^~JYB5GYJ?JJ7~^::::^^:::^^^~^~~~~~~~^^^~?7JY!JJJJJYYYYYYYYYYYYYY
# #         7777777777777777777777777???????????????YJ??J?5PGGPP55Y??7!!!!?!!?!:::..:::^^^^:::~!!!7!77!!~!!!!!~^::::^^:::^^^~~~~~!~^^~~~!7!^~?!JYJJJJYYYYYYYYYYYYY
# #         7777777777777777777777777???????????????YJJ?7~!?Y5Y?77!!!~~!!~~~7?^::...:::^^^:::^~7??777777777!!~::::::^^::^^^^~~~~~~~^^~~!YY!~!!~YYYJYYYYYYYYYYYYYYY
# #         7777777777777777777777777???????????????JY?!77~~~7??J????7!~~^^~?!......::^^~^^^^:^^~!!!77777!~^:::::::^::::^^^^~~~~~~^^^~^^JJ!~!~~YYJYYYYYYYYYYYYYYYY
# #         77777777?77777777777777777?????????????7JY!!7!~:::::^^^::^^:::^7?^:.....:^~^^~^^^^:::::::::::::...::::::::::^^^~^~^^~~^^^~^::~^^^^^YYYYYYYYYYYYYYYYYYY
# #         !77777777777777777777777777?????????????YJ~7!~~^:::::::::::::^!J!::....::^~~~~~^^^^::::::::::.....:::::::::^^^~~~~~^^~^^^~^:^^^^:~^JYYYYYYYYYYYYYYYYYY
# #         !!7777777777777777777777777?????????????Y?!?!~~^^^:::::::::::~7?^:....:::^~~~^^~^^^^::::::......:::::::::::^^^~~~~~~~^^^~~^:^^^~^^:?YYYYYYYYYYYYYYYYYY
# #         !!!!!7777777777777777777777????????????7J???!!!~~^^^::::::::^!?~::.....::^~~~^^^^^^^^^::........:::::::::^^^~~~~~~~~~^~^~~~^~~^~~^:?5YYYYYYYYYYYYYYYYY
# #         ~~~~!!!!!777777777777777777?????????????P77J7!!!!~^^:::::::^!77^:......::^~~^^^^^^^^^^::......:::::::^^:^^^^~~~~~~~~~~~^~~~^:~^~~^~YYYYYYYYYYYYYYYYYYY
# #         ^^^^~~~~~!!!!!!!777777???????????????77?PJ^J??77!~~^^:::::^~!7!~^:.....::^^^^:^^^^^~~^^::::.:::::::^^^^^^^~~~~!~~~~~~~~~~~~::^~^7!7YYYYYYYYYYYYYYYYYYY
# #         ^^^^^^^^^^~~~~~~!!!!!!7777777?????????7J5577J???77!~^:^:^^^~!J?~^::::::^^~!~^^^^~^:^~^^^:::::::^:^^^^^^^^~~~~!~~~~~~~~^~~~?^:^~~7!JYYYYYYYYYYYYYYYYYYY
# #         ::::::::^^^^^^^^~~~~~~~!!!!7777???????7Y55Y~?J???77!~^^^^^~~!55?!~~^^^~!!!7?JJ?7!:::^~^^^^::^^^^^^^^^^^^^~~~!!~~^^^~^^^~^~P!:^~!~?5YYYYYYYYYYYYYYYYYYY
# #         ::::::::::::::::^^^^^^^^~~~~!!!!!777777Y5557!JJJJ?77!~^^^^~!?PGP5J?777??JYPPYJ?7~:::::^^^^^^^^^^^^^^^^~~~~~~~~~^^^^^^~~~~!P!^^~!!YYYYYYYYYYYYYYYYYYYYY
# #         :::::::::::::::::::::^^^^^^^^^~~~~~~~!~?PPPY!?????7777!^^~!7J55PP5PPPPPGPJ7!^:^::::::::^^^^^^^^^^^^^^^~^~~~~~~~~~^^^^~~~^7P?!!!!JYYYYYYYYYYYYYYYYYYYYY
# #         :::::::::::::::::::::::::::::^^^^^^^^^^~7JY5Y77?7??7!!!!~~!7JY55555P5YJ7~^::::::::::::::^^^~~~~^^^^^~^^~~~~~~~~^^^^^~^~~~?GP5YJJ?77??JJJYY55YYYYYYYYY5
# #         :::::::::::::::::::::::::::::::::::::::::::J57?J7??7!77!!7~~!7?JJ?7!~~^::::::::::::^^^^^^^~!!~~~^^^^^^~~~~~~~~^^^^~~^~~~~7BGP5YJ?7!!!!!7777???JJJJYYYY
# #         :::::::::::::::::::::::::::::::::::::::.:::?5Y!J?7??!7777!!!^~~~~!~::::^^:::::::^^^^~~^~~^^~!~^^^^^^^~~~~~~~~~^^~^^~~~!~!J#BGP5Y?777!!!!!!!!!!!!!!!777
# #         ::::::::::::::::::::::::::::::::::::^~7??J55Y5!7?77?7?7?777!^^^^^!~^^^::^^:^::^^^~~~~~^^~~~^^^~~^^^~~~~~~~~^~~~~~~~~~!!!?5##BBGY?777777777777777777777
# #         ::::::::::::::::::::::::^^^^^^^~~7?JY55PPPPP5Y?7J7??7??J77?777?JJJY?!!!!77!!!!!!!!~~!~~~~~~~~^^~^^~~~~~~~~~^~~~~~~~~!!?YJJB#&#G5JJJJJ??777777777777777
# #         :::::::::^^^~~~!!!77777????JJJJYYYY5555PPPPG5Y?!J??J???YY5PGG5?!~^75GP5PGGGGP5YYYJYYJJJJ?77!~~^~^~~!~~~~~~~~~~~~~!!!7JYJ??JJYBBG5YJJJ???77777777777777
# #         ::^^~~!!!!7777777777777777???JJJYYYY5555PPGPG5Y??J?YJ?7JYY7~^:::^^~7GP5YYJJ?!!!7?J?777!~~~~~~~~~!77!!~~~~~~!!!!!!7!?Y5?77???7YBG5JJJJJ??77777777777777
# #         !!7!!!!!!!!!!!!!!!!!!!!777777???JJJYY55PPGGGBB5YJJYJY?!^:...::^^~!?J?!!7!7!!!7?YYYJ?!!!~~~~^~~!!?7!!~~~~~!!!!!!777J55YJ?7?7!77GG5YJJJJ?????7777777777!
# #         !!!!!!!!!!!!!!!!!!!!!!!!!!!777????JYY55PP5YJP#B5J!~::...:::^~!7?5PYJJJJYYYY5P55YJ7!~~~~~~~~~!!!7!~~~~~~!!!!777??7YP55J77!?7!!?GG5YYYJJ?????777777777!!
# #         !!!!!!!!!!!!!!!!!!~~~~~~!!!!!777???JJJ7^:.:!5J~::.....::~!7?J55PPPGGBBBBBGP5J7!~~~~~~~~~~~~!!77!~~~~~!!!777???!?5P5J7!!!!?!7!?PP5YYJJJJJJ??7777!!!!!!!
# #         !!!!!!!!!!!!!!!!!!!!!~~~~!!!!!!!77?7~:  ^?!!~...:::::^~!7?JYYYYYY5P5J?7!~^:::::^^^^^~^^^~~!!77!~~~~!!!!7????7J5P5J7!77!!77!!!JGPYYJJJJJ??77!!!!!77!!!!
# #         ~~~~~~!!!!!!!!!!!!!!~~~~~!~~!!!!!!7^:.  ^?:^::.:^~~!!!JY55YYJ??J?777!~^:^::^::^^^^^^^^^~~!7777~~~~!!!!7??JY5PPY?7!!777!!?!!!75P5JYJJJ??777777777777!!!
# #         ~~~~~~~~~!!!!!!!!!!~~~~~~~~~~!!!!!7?77~:^!::!~^^^~!?PGGPPPP5YJJ?!!!7!~~~~~~~^^^~~~~~~~!!7???7!~!!!!77JY5PPP5YJ?!!!!!!77!?!!7J5YJJJ??777!!7777777!!!!!!
# #         ~~~~~~~~~~~~!!!!!!!!~~~~~~~~~!!~^~~~~~~^~?77J?!!77!7?Y5PP55PPP5YJ?7!7!!!!!!!!!!!!!!77?JYJ?77!!!!77?YPGPP5YJJ7!!!!!!!!!77J??J5YYJ??7777!!!!7!!!!!~!!!!!
# #         ~~~~~~~~~~~~~~!!!!!!!~~~~~~!!~^:::.   ..::7YJ7!!!:.   ..:::^^^^~!7YYJJJ????JJYYYJYY55YYJ???777?JYPGGPP5YJJ?7!!!7!!!7777?JYYYJJ???7777777!!!!!!~~~!!!!!
# #         ~~~~~~~~~~~~~~!!!!!!~~!!~~!!^^..  ....::^^^~JJ!^........::::^^..::!PBGGPPPPPPPGGPP55YJJJJJYY5PGGGG55YYJ?77!!!!!!!!!777?JJYJ???????7777!!!!!~~~~~!~!!!!
# #         ~~~~~~~~~~~~~~~~~~!!!!~~!!7~:......:::::^^^^^~^::..:...::^^^^~:.:^^7&##BBBGGGPP555555PPPGGGBBGGP5YYJJ?77!!!!!!!!!!77??JJ?????777777!!!!!!~!!~~~~!~!!!!
# #         ~~~~~~~~~~~~~~~~~!~!!!!!77~.......:::::^~~~^:^J!~~~:....::^^~^..:^^J#B####BBBBBBBBBBBBBBBBGPP5YYYJJ?7777!!!!!!!!77?JJJ??77777777!!~~~~~~~~!!!!!!!~!!!!
# #         ~~~~~~~~~~~~~~~~~!!~~!7?7^.......::::^~!7!~^^~55JJ~......:::~:..:^^7G##B#######&BGGGGGPP55YYYYYJ??77!!!!!!!!77???????77!!!!!!!!~~~~~~~~~~~!!!!!!!!!!!!
# #         ~~~~~!!!~~~~~~~~~~!~!7?!:.......:::^!7?J?777?Y5G#?.........^^...:^~:~5&######BBBYYYYYYYYYYYJJ??7777!!!!!77777??77!!!!!!~~!!~~~~~~~~~~~~!!!!!!!!~!!!!!!
# #         ~~~~~~!!!~~~~~~~~~!7?7: ........::^~7Y5YY555GGGBG~:......:^~:..::^~:^^G#BBGGG5PBJJJJJJ?????77!!!!!!!77777777!!!~~~~~~!!!~!!~~~~~~~~~~~!!!!!!!!!!!!!!!!
# #         ~~~~~!!!!!~~~~~~!7?7^..........::^~!JJYPPPP5PB#&Y::.....::~:::::^~:.:^J7~~~!555#J??7777777!!777777777!!!!!!!~~~~~~~~~!!!!!!~~~~~~~~~~!!!!!!!!!!!!!!!!!
# #         ~~~~~!!!!!~~~~~!?7~...........::^~!?YY??JJJY5B#B?^:::::^^~:.:^^^~~..^7!^^^^^J5YBY7?7777???JJJ???77!!!~~~!!!~~~~~~~~~!!!!!!!~~~~~~~~~~!!!!!!!!!!!!!!!!!
# #         !~~~!!!!!!!!~!7?7^..........:::^~~?Y?~~^^^~!7JP?:::.:^^^~:..:^^~!:..^?~~^^~!Y5JY5?JJJJJYJYJJ?777!!!!!!!!!!!!~~~~~~~~!!!!!!~!~~~~~~~~~!!!!!~!!!!!!!!!!!
# #         ~~~~!!!!!!!!!77!^:........:::::^~!??~::::::^~7!^::::^^!7^.::^^~!^.::^7~~~~7?Y5555JJJYYJJJJJ?77!!!!!!!!!!!!!!!~~~~~~~!!!!!!!!!!~~~~~~~~!!~~~!!!!!!!7!!!
# #         ~~~~!!!!!!!77!~^.........:::::^~!??~:::::::^~7~::^^~~??^:::~~77~::::^~!!!7?!!?JJJJJJJJJJJ?777!!!!~~~~!!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~~~~~!!!!!!!7!!!!
# #         ~~~~!!!!!!7?!^:.........:::::^~~7?!:..::::^!7~:^^~!7P5^^::^~?5!^^^^^^!!!!77~!Y?JJJJJ?JJJ??77!!!!!~~~~!!!!!!!!!~~~~~~~!!!!!!!!!!~~~~~~~~~!!!!!!!!!7!!!!
# #         ~~!!!!!!!??7^::........:::::^~~!?7~..::::^~??^^^^!?P#5!~^~~!BG!^^^:^~77777!~:!????J???????7!!!!~!!~~~!!!!!!!!!!~~~~~~~~!!!!!!!!!~~~~~~~~!!!!!!!!!7!!!!""")
# #         time.sleep(2)
# #         print("OH BEHAVE")
# #         time.sleep(2)
# #         easter_egg = False
# #         name_check1()


# # name_check1()





# #!keys

# def keys_Lastcheck():
#     global keys
#     if keys == 3:
#         print("you have all the keys!")
#         good_ending_keys()
#     elif keys == 2:
#         print ("missing a key!")
#         bad_ending_keys()
#     elif keys == 1:
#         print ("missing 2 keys!")
#         bad_ending_keys()
#     elif keys == 0:
#         print ("No keys were collected!")
#         bad_ending_keys()
