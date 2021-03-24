import pyxel
class Barrel:
    def __init__(self):
        self.__posX = 53 #Barrel's position in the X axis
        self.__posY = 45 #Barrels's position in the Y axis
        self.__onPlat = False #Checks whether 
        self.__direct = 'R' #Stores the direction the barrel is rolling towards
        self.__scoreable = True #Checks whether Mario has jumped over a barrel (you will score once per barrel)
        self.__ladder = False #Checks if a barrel is rolling over a ladder
        self.__falling = False #Turns True when a barrel is neither onplat, onladder nor jumping
        
    """
    This function was used in early versions of the game when we didn't have a throwBarrel function for Donkey Kong,
    so barrels would reset everytime they reached the end of the course. In the final version of the game, the object
    is removed from the dictionary using its key name.
    def Reset(self):
        self.__posX = 53
        self.__posY = 45
        self.__direct = None
    """
    
    def platMove(self): #Very similar to Mario's platMove.
        self.__falling = False
        if (self.__posY > 150 and self.__posY < 200) or (self.__posY < 100 and self.__posY > 0):
            self.__posX = max(self.__posX + 2.5, 0)
            self.__direct = 'R'
        elif self.__posY > 200 or (self.__posY > 100 and self.__posY < 150):
            self.__posX = max(self.__posX - 2.5, 0)
            self.__direct = 'L'

    def ladderMove(self): #Runs when a barrel is randomly selected to fall down a ladder
        self.__falling = True
        self.__direct = None
        self.__posY = self.__posY + 1.5

    def fall(self): #This function replicates gravity. The name is self-explanatory
        self.__posY = min(self.__posY + 2.8, pyxel.height - 8)
        if self.__direct == 'R':
            self.__posX = max(self.__posX + 1, 0)
        elif self.__direct == 'L':
            self.__posX = max(self.__posX - 1, 0)
            
    #Getters
    @property
    def posX(self):
        return self.__posX

    @property
    def falling(self):
        return self.__falling

    @property
    def posY(self):
        return self.__posY

    @property
    def idn(self):
        return self.__idn

    @property
    def onPlat(self):
        return self.__onPlat

    @property
    def scoreable(self):
        return self.__scoreable

    @property
    def ladder(self):
        return self.__ladder

    @property
    def direct(self):
        return self.__direct

    # Setters
    @onPlat.setter
    def onPlat(self, value):
        self.__onPlat = value

    @scoreable.setter
    def scoreable(self, value):
        self.__scoreable = value

    @ladder.setter
    def ladder(self, value):
        self.__ladder = value

    @falling.setter
    def falling(self, value):
        self.__falling = value
