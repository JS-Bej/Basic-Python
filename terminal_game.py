import random

print ("--------------Terminal Game--------------")
print ("You are alone in the dark, you dont see anything...")
print ("Suddenly you wake up. It appears that you are fighting a monster and something hit you so hard you forgot your name.")
user=input("What is your new name? ")
print (f"\n{user}: Oh, yeah...")
print ("You see a monster in front of you, it is very ugly and scary. He's impatiently telling you that is your turn, he can't move.")
userhp=50
enemyhp=100
while enemyhp > 0 and userhp > 0:
 print (f"\nHP: {userhp}         Enemy HP: {enemyhp}")
 action=int(input("What do you want to do?\n1. Attack\n2. Defend\n3. Heal\n"))
 if action == 1:
  print ("You attack the monster!")
  damage=random.randint(12,20)
  enemyhp-=damage
  print (f"You did {damage} damage to the monster.")
  if enemyhp <= 0:
    print ("\nYou defeated the monster!")
    print ("Now you feel alone... Play again?")
    break
 elif action == 2:
  print ("You defend yourself!")
 elif action == 3:
    print ("You heal yourself!")
    heal=random.randint(10,14)
    userhp+=heal
    print (f"You healed {heal} HP.")
    if(userhp > 50):
        userhp = 50
 else:
    print ("Invalid action.")
    continue
 print ("The monster attacks you!")
 damage=random.randint(5,15)
 if action == 2:
    damage-=4
    print (f"You defended yourself and took {damage} damage.")
    userhp-=damage
 else:
   print (f"You took {damage} damage.")
   userhp-=damage

 if userhp <= 0:
    print ("\nYou died. Game over.")
print (f"Thanks for playing, {user}.")
print ("------------------------------------------")