# Import random function
# Roll the dice
# With a dictionary, print the dice

import random

def rollDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    
    print("Rolled: {} and {}".format(d1,d2))

    again = input("Again? Y/N ")
    if again == "Y" or again == "y":
        rollDice()
    else:
        print("Goodbye")

rollDice()