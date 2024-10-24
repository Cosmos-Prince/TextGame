import random

def diceRoll(numberOfDices:int , diceSize:int, modifier:int) -> int:
    roll:int = 0 
    for i in range(0,numberOfDices):
        roll += random.randint(1, diceSize)
    roll += modifier
    return roll
# creates a dice roll function, which calculates the total of the dice roll depending on the number and max value of the dice

print(diceRoll(1, 10, 0))