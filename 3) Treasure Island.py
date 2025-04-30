print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Caution: Type in capital letters only.")
Direction = input("Do you want to go to left or right? type L for left or R for right ")
if Direction == "L":
    swim_or_wait = input("There is a river, do you want to swim or wait? Type S to swim or W to wait ")
    if swim_or_wait == "W":
        choose_door = input("Which door you want to choose, red, blue or yellow? Type the first letter of the color ")
        if choose_door == 'R':
            print("You got burned like a witch in medieval times. Game over")
        elif choose_door == "B":
            print("You got eaten by beast you filthy human, Game over.")
        elif choose_door == "Y":
            print("You did good for a human being. You win.")
        else:
            print("Choose a correct door you insolent being.")


    else:
        print("You were attacked by trout, game over you loser.")
else:
    print("You fell into hole, game over. hahahaha")