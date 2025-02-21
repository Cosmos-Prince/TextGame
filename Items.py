
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

Helmet1 = Helmet("Crâne reluisant", 40, 4)
Helmet2 = Helmet("Yankee with no brim", 30, 3)
Helmet3 = Helmet("Fallen king's crown", 20, 2)
Helmet4 = Helmet("Perruque de Remilli", 10, 1)
Helmet5 = Helmet("Une tuque aek dla broche", 50, 5)

###############    Chestplates    ###############

Chest1 = Chest("Hoodie rouge à Émile", 50, 5)
Chest2 = Chest("Diamond chestplate", 40, 4)
Chest3 = Chest("Un beater blanc", 10, 1)
Chest4 = Chest("Power Armor", 30, 3)
Chest5 = Chest("")

###############    Arms    ###############

Arms1 = Arms("Ein ti braclet d'amitié", 10, 1)
Arms2 = Arms("")
Arms3 = Arms()
Arms4 = Arms()
Arms5 = Arms()

###############    Pants    ###############

Pants1 = Pants("Les pants a Super Fancy Pants Adventure", 30, 3)
Pants2 = Pants("Joggings gris", 10, 1)
Pants3 = Pants("")
Pants4 = Pants()
Pants5 = Pants()

###############    Feet    ###############

Feet1 = Feet("Gougounnes", 10, 1)
Feet2 = Feet("Timbs", 20, 2)
Feet3 = Feet("")
Feet4 = Feet()
Feet5 = Feet()

###############    Misc~    ###############

Misc1 = Misc("Skibidiamand", 20, "Damage", 2)
Misc2 = Misc("Pierres aux reins dans un p'tit pot d'pillules", 40, "Damage", 4)
Misc3 = Misc("Mené artéfact famillial Tassé", 20, "Defense", 2)
Misc4 = Misc("Une garnotte", 10, "Damage", 1)
Misc5 = Misc("Une roche", 20, "Damage", 2)
Misc6 = Misc("Un pick de guit à Purok", 10, "Damage", 1)
Misc7 = Misc("Steve", 20, "Damage", 2)
Misc8 = Misc("J'ai des lunettes tu peux pas mfesser", 20, "Defense", 2)
Misc9 = Misc("Une monster blanche", 30, "Damage", 3)
Misc10 = Misc("Un des kids à Le Sau ?", 30, "Damage", 3)
Misc11 = Misc()
Misc12 = Misc()
Misc13 = Misc()
Misc14 = Misc()
Misc15 = Misc()

###############    Weapons    ###############

Weapon1 = Weapon("Épée des cramptés", 60, 6)
Weapon2 = Weapon("Quoicoupelle", 70, 7)
Weapon3 = Weapon("Le boulet à Boulet", 50, 5)
Weapon4 = Weapon("Objet phallique mauve en sillicone", 10, 1)
Weapon5 = Weapon("Cool stick you found", 20, 2)
Weapon6 = Weapon("Crowbar", 30, 3)
Weapon7 = Weapon("La guit à Purok", 40, 4)
