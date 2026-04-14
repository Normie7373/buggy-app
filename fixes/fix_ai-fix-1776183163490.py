import random
from random import randint

def roll_dice(first, last):
    try:
        roll = randint(first, last)
        return roll
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

first = 1
last = 6
result = roll_dice(first, last)
print(f"You rolled a {result}")