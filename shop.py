import random

class Item:
    def __init__(self, name:str, price:int, statName:str, statBonus:int, itemType:str):
        self.__itemName:str = name
        self.__price:int = price
        self.__statUpgraded:str = statName
        self.__bonus:int = statBonus
        self.__itemType:str = itemType
    # Constructor for every item, statUpgraded dictates which stat gets a bonus and itemType
    # dictates which inventory slot it will go in

    def __str__(self):
        return f"   {self.__itemName} | {self.__price} gold | +{self.__bonus} {self.__statUpgraded} | {self.__itemType}"
    # When called with print(ItemName), will print the message above with all stats.
    # Will be used in shop "interface"

    