from character import *
from functions import diceRoll, askInput
from Items import *
import math


class Player(Character):
    def __init__(self):
        super().__init__()
        # calls back the parent constructor
        self.__pots:int = 3
        self.__xp:int = 0
        self.__gold:int = 10
        self.__level:int = 1
        self.__invHead:Helmet = baseHelmet
        self.__invChest:Chest = baseChest
        self.__invArms:Arms = baseArms
        self.__invPants:Pants = basePants
        self.__invFeet:Feet = baseFeet
        self.__invMisc1:Misc = baseMisc
        self.__invMisc2:Misc = baseMisc
        self.__invMisc3:Misc = baseMisc
        self.__invMisc4:Misc = baseMisc
        self.__invWeapon:Weapon = baseWeapon
    # creates player class, adding onto the character class giving it pots, xp, and gold
    # adds inventory slots for items

    def getInventory(self):
        inventory:list = [self.__invHead.describeItem(), self.__invChest.describeItem(), self.__invArms.describeItem(), 
                          self.__invPants.describeItem(), self.__invFeet.describeItem(), self.__invMisc1.describeItem(), 
                          self.__invMisc2.describeItem(), self.__invMisc3.describeItem(), self.__invMisc4.describeItem(), self.__invWeapon.describeItem()]    
        return inventory
    # allows to see what items the player currently has, stored in a list that can be used to 
    # be compared later on

    def setItems(self, itemToEquip:Item, itemSlot:int = None):
        type:str = itemToEquip.getItemType()
        previousItem:Item = None
        if itemSlot != None:
            match itemSlot:
                case 1: self.__invMisc1 = itemToEquip
                case 2: self.__invMisc2 = itemToEquip
                case 3: self.__invMisc3 = itemToEquip
                case 4: self.__invMisc4 = itemToEquip
            return
        elif type == "Miscellaneous":
            print("Which item do you wish to replace?")
            choice:int = askInput([self.__invMisc1.describeItem(), self.__invMisc2.describeItem(), self.__invMisc3.describeItem(), self.__invMisc4.describeItem()])
            match choice:
                case 1:
                    previousItem = self.__invMisc1
                    self.__invMisc1 = itemToEquip
                case 2:
                    previousItem = self.__invMisc2
                    self.__invMisc2 = itemToEquip
                case 3:
                    previousItem = self.__invMisc3
                    self.__invMisc3 = itemToEquip
                case 4:
                    previousItem = self.__invMisc4
                    self.__invMisc4 = itemToEquip
            return [previousItem, choice]
        elif type == "Weapon":
            previousItem = self.__invWeapon
            self.__invWeapon = itemToEquip
        elif type == "Helmet":
            previousItem = self.__invHead
            self.__invHead = itemToEquip
        elif type == "Chestplate":
            previousItem = self.__invChest
            self.__invChest = itemToEquip
        elif type == "Bracers / Gloves":
            previousItem = self.__invArms
            self.__invArms = itemToEquip
        elif type == "Pants":
            previousItem = self.__invPants
            self.__invPants = itemToEquip
        elif type == "Shoes / Boots":
            previousItem = self.__invFeet
            self.__invFeet = itemToEquip
        else:
            print("I fucked up")
        return previousItem
        # changes the item based on where it should go in the 
        # player's inventory. Also returns previously equipped item for undo purpose


    def getPots(self):
        return self.__pots
    # allows to see the number of potions left in the inventory
    
    def getLvl(self):
        return self.__level
    # getter for player's level

    def getGold(self):
        return self.__gold
    # getter for player's gold
    
    def potsAdd(self, number:int):
        self.__pots += number
    # adds a number of potions to the player's inventory.

    def potionDrinking(self):
        if self.__pots <= 0:
            print("You don't have any remaining potions, you can buy some more next time you visit a shop")
            return
        self.__pots -= 1
        self.heal(diceRoll(1, 6, 2))
    # function to make drinking potions, heals by 1d4 + 2 and removes 1 potion from player inventory
    
    def changeGold(self, ammount:int, add:bool):
        if add == True:
            self.__gold += ammount
        elif add == False:
            self.__gold -= ammount
        else:
            print("how the fuck...")
        print(f"You now have {self.__gold} gold (beaucoup de bidous ca mon homme)")    
    # changes the gold of the player, depending on if needed to add or substract

    def killRewards(self):
        self.__xp += diceRoll(4, 10, 5) 
        self.changeGold(diceRoll(2, 10, 5), True)
        self.lvlup()
    # gives the player gold and xp per enemy kill and checks if the player can lvl up
    
    def xpToLvlUp(self):
        return round(math.log(self.__lvl, 1.5)*100, None)
    # function to calculate the the xp needed to lvl up

    def lvlUp(self):
        if self.__xp >= self.xpToLvlUp():
            self.__level += 1
            self.__xp -= self.xpToLvlUp()
            self.__atk += 2
            self.__hp += 10
            self.__defense += 1
            print(f"Congrats! You are now level {self.getLvl()} and have increased your stats! ")
        else:
            return
        
    # function to calculate lvl up and gives stats, resets xp back to xp - xp needed to lvl up
    