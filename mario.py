import pyxel
class Mario:
    # METHODS

    def __init__(self):
        self.__posX = 24 #Mario's position on the X axis
        self.__posY = 225 #Mario's position on the Y axis
        self.__lives = 3 #Mario's lives counter
        self.__dead = False #Turns True when mario.lives = 0
        self.__onplat = False #Checks whether Mario is standing on a platform
        self.__onladder = False #Checks whether Mario is standing on/over a ladder
        self.__falling = False #Turns True when Mario is neither onplat, onladder nor jumping
        self.__direct = 'R' #Stores the way Mario is facing (Right/Left)
        self.__jumpMoving = False  # Whether or not the player is jumping while moving
        self.__jumping = False #Whether or not Mario is jumping
        self.__gravity = 0 #This attribute was used to create more realistic jumps
        self.__score = 0 #Stores Mario's Score
        self.__dying = False #This attribute was used to trigger Mario's death animation
        self.__condition = False #Necessary for Mario's death animation
        self.__win = False #Stops the game and triggers the winning sequence
        self.__inRange = False #This attriute was used to draw the "+ 100" everytime Mario jumps over a barrel


    def fall(self): #This function replicates gravity. The name is self-explanatory
        self.__falling = True
        if self.__gravity != 0:
            self.__posY += self.__gravity
            self.__gravity = min(self.__gravity + 0.5, 4)
        else:
            self.__posY = min(self.__posY + 2, pyxel.height - 8)
        if self.__jumpMoving:
            if self.__direct == 'L' and self.__posY < 200:
                self.__posX = max(self.__posX - 1, 1)
            elif self.__direct == 'L' and self.__posY > 200:
                self.__posX = max(self.__posX - 1, 10)
            elif self.__direct == 'R':
                self.__posX = min(self.__posX + 1, pyxel.width - 15)

    def platMove(self): #Allows Mario to move sideways only while onPlat
        if self.__posY > 200:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_AXIS_LEFTX):
                self.__posX = max(self.__posX - 1, 10)
                self.__direct = 'L'
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_AXIS_RIGHTX):
                self.__posX = min(self.__posX + 1, pyxel.width - 15)
                self.__direct = 'R'
        elif self.__posY < 100:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_AXIS_LEFTX):
                self.__posX = max(self.__posX - 1, 46)
                self.__direct = 'L'
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_AXIS_RIGHTX):
                self.__posX = min(self.__posX + 1, pyxel.width - 15)
                self.__direct = 'R'
        else:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_AXIS_LEFTX):
                self.__posX = max(self.__posX - 1, 0)
                self.__direct = 'L'
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_AXIS_RIGHTX):
                self.__posX = min(self.__posX + 1, pyxel.width - 16)
                self.__direct = 'R'
    
    """
    This function was our first approach to Mario's onladder movement, but later
    on we decided that it would be easier to handle if we split it into ladderUp
    (Mario climbing upwards) and ladderDown (going downwards)
    def ladderMove(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.__posY = min(self.__posY - 2, pyxel.height)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.__posY = min(self.__posY + 2, pyxel.height)
    
    """
    
    def ladderUp(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.__posY = self.__posY - 1

    def ladderDown(self):
        if pyxel.btn(pyxel.KEY_DOWN):
            self.__posY = self.__posY + 2

    def jump(self): #This function is divided in 3 parts, 2 for Mario jumping while moving and 1 for static jump
        if pyxel.btn(pyxel.KEY_SPACE) and pyxel.btn(pyxel.KEY_RIGHT):
            self.__posX += 2
            self.__posY -= 5
            self.__gravity = -4
            self.__jumpMoving = True
            self.__jumping = True

        elif pyxel.btn(pyxel.KEY_SPACE) and pyxel.btn(pyxel.KEY_LEFT):
            self.__posX -= 2
            self.__posY -= 5
            self.__gravity = -4
            self.__jumpMoving = True
            self.__jumping = True


        elif pyxel.btn(pyxel.KEY_SPACE):
            self.__posY -= 5
            self.__gravity = -4
            self.__jumpMoving = False
            self.__jumping = True

    def Death(self): #This function is executed everytime Mario collides with a barrel
        self.__lives -= 1
        self.__posX = 24
        self.__posY = 225
        self.__jumping = False
        self.__dying = False
        for i in range(2):
            if self.__score > 0:
                self.__score -= 100

        if self.__lives == 0:
            self.__dead = True

    def Reset(self): #This function resets Mario when R is pressed on the keyboard
        self.__lives = 3
        self.__posX = 24
        self.__posY = 225
        self.__dead = False
        self.__onplat = False
        self.__direct = 'R'
        self.__score = 0
        self.__win = False

    # GETTERS
    @property
    def lives(self):
        return self.__lives

    @property
    def inRange(self):
        return self.__inRange

    @property
    def score(self):
        return self.__score

    @property
    def posX(self):
        return self.__posX

    @property
    def posY(self):
        return self.__posY

    @property
    def dying(self):
        return self.__dying

    @property
    def dead(self):
        return self.__dead

    @property
    def jumping(self):
        return self.__jumping

    @property
    def onplat(self):
        return self.__onplat

    @property
    def onladder(self):
        return self.__onladder

    @property
    def falling(self):
        return self.__falling

    @property
    def direct(self):
        return self.__direct

    @property
    def condition(self):
        return self.__condition

    @property
    def win(self):
        return self.__win

    # SETTERS
    @condition.setter
    def condition(self, value):
        self.__condition = value

    @posX.setter
    def posX(self, value):
        self.__posX = value

    @inRange.setter
    def inRange(self, value):
        self.__inRange = value

    @posY.setter
    def posY(self, value):
        self.__posY = value

    @lives.setter
    def lives(self, value):
        self.__lives = value

    @dying.setter
    def dying(self, value):
        self.__dying = value

    @dead.setter
    def dead(self, value):
        self.__dead = value

    @onplat.setter
    def onplat(self, value):
        self.__onplat = value

    @onladder.setter
    def onladder(self, value):
        self.__onladder = value

    @falling.setter
    def falling(self, value):
        self.__falling = value

    @jumping.setter
    def jumping(self, value):
        self.__jumping = value

    @direct.setter
    def direct(self, value):
        self.__direct = value

    @score.setter
    def score(self, value):
        self.__score = value

    @win.setter
    def win(self, value):
        self.__win = value

