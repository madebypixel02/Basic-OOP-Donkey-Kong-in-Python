class Platform: #Static element
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y

    @property
    def posX(self):
        return self.__posX

    @property
    def posY(self):
        return self.__posY


class InvisiPlat: #Static element
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y

    @property
    def posX(self):
        return self.__posX

    @property
    def posY(self):
        return self.__posY

class Ladder: 
    def __init__(self, x, y_high, y_low):
        self.__posX = x
        self.__posYhigh = y_high #Upper limit
        self.__posYlow = y_low #Lower limit

    @property
    def posX(self):
        return self.__posX

    @property
    def posYhigh(self):
        return self.__posYhigh

    @property
    def posYlow(self):
        return self.__posYlow

