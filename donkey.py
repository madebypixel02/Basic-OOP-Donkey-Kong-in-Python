from barrel import Barrel
class Donkey:
    def __init__(self):
        self.__posX = 16 #Donkey's position in the X axis
        self.__posY = 38 #Donkey's position in the Y axis
        self.__counter = 1 #This attribute is used for naming the barrels Donkey throws
        self.__throwing = False #Triggers animation
        self.__grabbing_barrel = False #Triggers animation
        self.__waiting = False #Triggers animation

    def throwBarrel(self): #This function creates a barrel object, returning both the object and a name (that will be used as a key in the barrels dictionary)
        name = 'barrel_' + str(self.__counter)
        obj = Barrel()
        self.__counter += 1
        return name, obj

    #GETTERS
    @property
    def posX(self):
        return self.__posX

    @property
    def waiting(self):
        return self.__waiting

    @property
    def grabbing_barrel(self):
        return self.__grabbing_barrel

    @property
    def posY(self):
        return self.__posY

    @property
    def throwing(self):
        return self.__throwing

    #SETTERS
    @waiting.setter
    def waiting(self, value):
        self.__waiting = value

    @throwing.setter
    def throwing(self, value):
        self.__throwing = value

    @grabbing_barrel.setter
    def grabbing_barrel(self, value):
        self.__grabbing_barrel = value
