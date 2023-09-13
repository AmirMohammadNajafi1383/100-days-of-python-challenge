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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

user_input = (input("You're at a cross road.\nWhere do you want to go? Type \"left\" or \"right\"\n")).lower()
if user_input == "left":
      user_input = (input("You've come to a lake.\nThere is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")).lower()

      if user_input == "swim":
            print("You got attacked by an angry trout.\nGame Over.")
      elif user_input == "wait":
            user_input = (input("you arrive at the island unharmed.\nThere is a house with 3 doors.One red, one yellow and one blue.Which color do you choose?\n")).lower()
            if user_input == "yellow":
                  print("You found the treasure.\nYou win!")
            elif user_input == "red":
                  print("It's a room full of fire.\nGame Over.")
            elif user_input == "blue":
                  print("You enter a room of beats.\n Game Over.")
elif user_input == "right":
      print("You fell into a hole.\nGame Over.")