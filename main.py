import random
import os
import sys
import time


def write(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Variables
miles = 0
health = 10
energy = 10
randy = random.randint(1,10) # FIXED
bigrandy = random.randint(1,20)
crew = 25 + random.randint(0,6)
food = 150 + random.randint(0,20)
oxygen = 10 + random.randint(0,6)
fuel = 50 + random.randint(0,3)
attack = 3
standing = 10
morale = 10
armor = 15
day = 0
done = False

write("Select your ship class!")
shipclass = int(input("1. Explorer, 2. Ambassador, 3. Destroyer"))

if shipclass == 1:
    oxygen = oxygen + 10
    food = food + 75
    fuel = fuel + 40
    crew = crew - 10
if shipclass == 2:
    morale = morale + 5
    standing = standing + 10
    armor = armor + 3
    attack = attack - 1
    crew = crew + 5
if shipclass == 3:
    morale = morale-1
    attack= attack+4
    armor = armor+5
    standing = standing-2

write("""
====================================
    Welcome to the Ship Game!
====================================
You’ve taken a camel to journey across the vast Sahara desert.
The locals are pursuing you to reclaim their camel.
Endure your desert adventure and stay ahead of the natives.

Instructions:
- Choose actions each turn to manage thirst, camel tiredness, and distance.
- Reach 200 miles to win. If the natives catch you, you lose!
- Find oases for a boost. Good luck!
====================================
""", 0.01)




while crew>0:
    randy = random.randint(1, 10)
    print("Day", day)
    print( "ship status" )
    print ("crew", crew)
    print("food", food)
    print("oxygen", oxygen)
    print ("fuel", fuel)
    print ("attack", attack)
    print ("standing", standing)
    print ("morale", morale)
    print ("armor", armor)
    
    





