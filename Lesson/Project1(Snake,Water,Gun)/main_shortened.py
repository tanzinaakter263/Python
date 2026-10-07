'''We all have played snake, water gun game in our childood.
If you don't google the rules of this game and 
write a python program capable of playing this game with the user.

1 for snake
-1 for water
0 for gun
'''

import random
computer=random.choice([-1,0,1])
youstr = input("Enter your choice: " )
youDict={"s":1,"w":-1,"g":0} 
reverseDict={ 1: "snake", -1: "water", 0: "gun" }
you=youDict[youstr]

#by now  we have 2 numbers (variables), you and computer

print(f"You choice {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer==you):
  print("It's a draw!")
else:
  if((computer - you)== -1 or (computer - you) == 2):
    print("You lose!")
  else:
    print("You win!")
