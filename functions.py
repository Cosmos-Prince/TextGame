import random

def diceRoll(numberOfDices:int , diceSize:int, modifier:int) -> int:
    roll:int = 0 
    for i in range(0,numberOfDices):
        roll += random.randint(1, diceSize)
    roll += modifier
    return roll
# creates a dice roll function, which calculates the total of the dice roll depending on the number and max value of the dice


def askInput(choices:list):
    # prints the choices for the user
    print("Please choose your next action...")
    for i in range(0, len(choices)):
        print(f"{i+1}-" + choices[i])
    while True:
        try:
            # tries to convert the input to an int, if succeed, return the int
            number:int = int(input())
            if number >=1 and number < len(choices) + 1:
                return number
            else:
                print(f"Please input a valid number (between 1 and {len(choices)})")
        except :
            print("please input a number, not whatever the fuck you put there lmao")

