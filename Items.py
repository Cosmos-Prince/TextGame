
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

### creation of classes
# super parent class is item
# child class Armor which is parent to all armor classes (helmet, chest, pants, boots, arms)
# Weapon and misc are still childs of Item since they dont have the same stats changed as Armor
class Armor(Item):
    def __init__(self, name:str, price:int, statBonus:int, itemType:str):
        super().__init__(name, price, "Defense", statBonus, itemType)

class Helmet(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Helmet")

class Chest(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Chestplate")

class Arms(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Bracers / Gloves")

class Pants(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Pants")

class Feet(Armor):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, statBonus, "Shoes / Boots")
        
class Misc(Item):
    def __init__(self, name:str, price:int, statName:str, statBonus:int):
        super().__init__(name, price, statName, statBonus, "Miscellaneous")

class Weapon(Item):
    def __init__(self, name:str, price:int, statBonus:int):
        super().__init__(name, price, "Damage", statBonus, "Weapon")

# Creates all different kinds of child items to fit them into the inventory of the player

###############   Helmets    ###############    

Helmet1 = Helmet()
Helmet2 = Helmet()
Helmet3 = Helmet()
Helmet4 = Helmet()
Helmet5 = Helmet()

###############    Chestplates    ###############

Chest1 = Chest()
Chest2 = Chest()
Chest3 = Chest()
Chest4 = Chest()
Chest5 = Chest()

###############    Arms    ###############

Arms1 = Arms()
Arms2 = Arms()
Arms3 = Arms()
Arms4 = Arms()
Arms5 = Arms()

###############    Pants    ###############

Pants1 = Pants()
Pants2 = Pants()
Pants3 = Pants()
Pants4 = Pants()
Pants5 = Pants()

###############    Feet    ###############

Feet1 = Feet()
Feet2 = Feet()
Feet3 = Feet()
Feet4 = Feet()
Feet5 = Feet()

###############    Misc~    ###############

Misc1 = Misc()
Misc2 = Misc()
Misc3 = Misc()
Misc4 = Misc()
Misc5 = Misc()
Misc6 = Misc()
Misc7 = Misc()
Misc8 = Misc()
Misc9 = Misc()
Misc10 = Misc()
Misc11 = Misc()
Misc12 = Misc()
Misc13 = Misc()
Misc14 = Misc()
Misc15 = Misc()

###############    Weapons    ###############

Weapon1 = Weapon()
Weapon2 = Weapon()
Weapon3 = Weapon()
Weapon4 = Weapon()
Weapon5 = Weapon()
Weapon6 = Weapon()
Weapon7 = Weapon()
