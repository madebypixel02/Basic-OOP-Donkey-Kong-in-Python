#MAIN
from mario import Mario
from donkey import Donkey
import statics
import pyxel
import random
import math

class Game:
    
    def __init__(self):
        WIDTH = 192
        HEIGHT = 250
        CAPTION = "Mario Game Beta 5.0"
        
        self.mario = Mario()
        self.kong = Donkey()
        self.win_condition = False
        
        self.barrels = {}
        #######################
        self.platforms = {}
        for i in range(1,24):
            if i < 3:
                name = 'platform_' + str(i)
                x = 16 * (i-1)
                y = 242
                obj = statics.Platform(x,y)
                self.platforms[name] = obj
            elif i < 14:
                for j in range(2):
                    if j == 0:
                        name = 'platform_' + str(i) + '.' + str(j + 1)
                        x = 16 * (i-1)
                        y = 242 - (i-2)
                        obj = statics.Platform(x,y)
                        self.platforms[name] = obj
                    elif j == 1:
                        name = 'platform_' + str(i) + '.' + str(j + 1)
                        x = 16 * (i-1)
                        y = 140 - (i-2)
                        obj = statics.Platform(x,y)
                        self.platforms[name] = obj
            elif i > 13:
                if i == 16:
                    name = 'platform_' + str(i)
                    x = 16 * (i-15)
                    y = 180 + 1
                    obj = statics.Platform(x,y)
                    self.platforms[name] = obj
                else:
                    name = 'platform_' + str(i)
                    x = 16 * (i-15)
                    y = 180 + (i-15)
                    obj = statics.Platform(x,y)
                    self.platforms[name] = obj
        
        for i in range(10):
            if i < 3:
                name = 'platform' + str(100 + i)
                x = 16 * i
                y = 70
                obj = statics.Platform(x,y)
                self.platforms[name] = obj
            else:
                name = 'platform' + str(100 + i)
                x = 16*i
                y = 70 + (i - 2)
                obj = statics.Platform(x,y)
                self.platforms[name] = obj
        
        for i in range(6):
            name = 'platform' + str(200 + i)
            x = 100 + 16*i
            y = 40
            obj = statics.Platform(x,y)
            self.platforms[name] = obj
        ################
        self.invisiplats = {}
        name = 'inv_1'
        x = 145
        y = 188
        obj = statics.InvisiPlat(x, y)
        self.invisiplats[name] = obj
        name = 'inv_2'
        x = 160
        y = 77
        obj = statics.InvisiPlat(x, y)
        self.invisiplats[name] = obj
        name = 'inv_3'
        x = 32
        y = 139
        obj = statics.InvisiPlat(x, y)
        self.invisiplats[name] = obj
        ################
        self.ladders = {}
        
        name = 'ladder_1'
        x = 118
        yl = 229
        yh = 187
        obj = statics.Ladder(x, yh, yl)
        self.ladders[name] = obj
        
        name = 'ladder_2'
        x = 50
        yl = 176
        yh = 138
        obj = statics.Ladder(x, yh, yl)
        self.ladders[name] = obj
        
        
        name = 'ladder_3'
        x = 130
        yl = 126
        yh = 76
        obj = statics.Ladder(x, yh, yl)
        self.ladders[name] = obj
        
        name = 'ladder_4'
        x = 101
        yl = 67
        yh = 41
        obj = statics.Ladder(x, yh, yl)
        self.ladders[name] = obj
        
        ##################
        self.scores_path = 'highscores.txt'
        try:
            with open(self.scores_path, "r") as file:
                self.highscores = eval(file.readline())
            
        except:
            self.highscores =  []
            for i in range(5):
                self.highscores.append(0)
            
            with open(self.scores_path, "w") as file:
                file.write(str(self.highscores))
        ##################
        """
        We thought at first that ladders could be iterably generated, but soon
        changed our mind. 
        self.ladders = {}
        for i in range(1,9):
            name = 'ladder_' + str(i)
            x = 117
            y = 236-6*i
            obj = classes.Ladder(x,y)
            self.ladders[name] = obj
        """
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("opjects.pyxres")
        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)
        

    def update(self):
        if not self.mario.dead and not self.mario.win:
            self.win_condition = False
            self.mario.onplat = False
            self.mario.onladder = False
            self.mario.falling = False
            barrels_clear = False
            for j in self.barrels:
                self.barrels[j].onPlat = False
                self.barrels[j].ladder = False

            del_barrel = False

            b = random.randint(1, 3)
            if pyxel.frame_count % (30 * b) == 0:
                if len(self.barrels) < 10:
                    self.kong.throwing = True
                    self.kong.waiting = False
                    self.kong.grabbing_barrel = False
                    l = self.kong.throwBarrel()
                    self.barrels[l[0]] = l[1]

            #Mario WALK ON NON-HORIZONTAL platforms
            if self.mario.posY > 45:
                for i in self.platforms:
                    if self.mario.posY < 100:
                        if self.mario.posX + 5 == self.platforms[i].posX and self.mario.posY + 16 == self.platforms[i].posY: #fixes a bug when climbing the 3rd ladder
                            self.mario.posY -= 1
                    if self.mario.posY > 200 or (self.mario.posY < 160 and self.mario.posY > 100):

                        if self.mario.posX + 12 == self.platforms[i].posX and self.mario.posY + 15 == self.platforms[i].posY and self.mario.direct == 'R':
                            self.mario.posY -= 1
                            self.mario.posX += 1

                        if self.mario.posX + 12 == self.platforms[i].posX and self.mario.posY + 16 == self.platforms[i].posY and self.mario.direct == 'L':
                            self.mario.posY += 1
                            self.mario.posX -= 1

                        if self.mario.posX + 13 == self.platforms[i].posX and self.mario.posY + 16 == self.platforms[i].posY and self.mario.direct == 'L' and i!=1:
                            self.mario.posY += 1
                            self.mario.posX -= 1
                    #BUG FIX
                    if (self.mario.posX + 6 == self.platforms[i].posX) and (self.mario.posY + 16 or self.mario.posY + 17) == self.platforms[i].posY:
                        self.mario.posY -= 1

                    #BUG FIX
                    if  (self.mario.posX + 6 == self.platforms[i].posX) and self.mario.posY + 14 == self.platforms[i].posY:
                        self.mario.posY -= 1

                    #BUG FIX
                    if (self.mario.posX + 2 == self.platforms[i].posX or self.mario.posX + 1 == self.platforms[i].posX or self.mario.posX == self.platforms[i].posX or self.mario.posX - 1 == self.platforms[i].posX) and (self.mario.posY + 17 == self.platforms[i].posY or self.mario.posY + 18 == self.platforms[i].posY or self.mario.posY + 19 == self.platforms[i].posY) and self.mario.onladder == False:
                        self.mario.posY += 1


                    if (self.mario.posY < 200 and self.mario.posY > 160) or (self.mario.posY < 100 and self.mario.posY > 0):
                        if self.mario.posX + 3 == self.platforms[i].posX and self.mario.posY + 16 == self.platforms[i].posY and self.mario.direct == 'L':
                            self.mario.posY -= 1
                            self.mario.posX -= 1
                        if self.mario.posX + 3 == self.platforms[i].posX and self.mario.posY + 16 == self.platforms[i].posY and self.mario.direct == 'L':
                            self.mario.posY -= 1
                            self.mario.posX -= 1
                        if self.mario.posX + 4 == self.platforms[i].posX and self.mario.posY + 17 == self.platforms[i].posY and self.mario.direct == 'R':
                            self.mario.posY += 1
                            self.mario.posX += 1


            else:
                #BUG FIX
                for i in self.platforms:
                    if (self.mario.posX + 6 == self.platforms[i].posX) and (self.mario.posY + 17 == self.platforms[i].posY):
                        self.mario.posY += 1
                
            #BARRELS ROLLING DOWN THE self.platforms
            for i in self.platforms:
                for j in self.barrels:
                    if self.platforms[i].posY - self.barrels[j].posY < 12 and self.platforms[i].posY - self.barrels[j].posY > 9 and abs(self.barrels[j].posX - self.platforms[i].posX) < 16:
                        self.barrels[j].onPlat = True
                        self.barrels[j].falling = False
                if self.platforms[i].posY - self.mario.posY < 18 and self.platforms[i].posY - self.mario.posY > 15 and abs(self.mario.posX - self.platforms[i].posX) < 18 :
                    self.mario.onplat = True
                    self.mario.jumping = False

                    if not self.mario.dying:
                        self.mario.platMove()
                        self.mario.jump()
                        for l in self.invisiplats:
                            if 0 < self.invisiplats[l].posX - self.mario.posX < 17 and 15 < self.invisiplats[l].posY - self.mario.posY < 18 and ((self.mario.posY < 200 and self.mario.posY > 160) or (self.mario.posY < 100 and self.mario.posY > 50)):
                                self.mario.platMove()
                            else:
                                if -16 < self.mario.posX - self.invisiplats[l].posX < 6 and 15 < self.invisiplats[l].posY - self.mario.posY < 18:
                                    self.mario.platMove()
                    
                #PREVENTS self.mario FROM SLOWING DOWN AFTER JUMPING
                if self.platforms[i].posY - self.mario.posY < 20 and self.platforms[i].posY - self.mario.posY > 17 and abs(self.mario.posX - self.platforms[i].posX) < 18 :
                    if not self.mario.dying:
                        self.mario.platMove()
                        self.mario.jump()

            for j in self.barrels:
                for k in self.ladders:
                    if self.barrels[j].posX + 4 - self.ladders[k].posX < 3 and self.barrels[j].posX + 4 - self.ladders[k].posX > -5 and self.barrels[j].posY + 8 < self.ladders[k].posYlow and self.barrels[j].posY >= self.ladders[k].posYhigh - 17:
                        a = random.randint(1,4)
                        if a == 1:
                            self.barrels[j].ladder = True
                            self.barrels[j].onplat = False



            #self.mario ON LADDER DETECTION
            for i in self.ladders:
                if self.mario.posX + 2 - self.ladders[i].posX < 4 and self.mario.posX + 2 - self.ladders[i].posX > -4 and self.mario.posY + 8 < self.ladders[i].posYlow and self.mario.posY >= self.ladders[i].posYhigh - 17:
                    self.mario.onladder = True

            #self.mario ON LADDER MOVEMENT
            for i in self.ladders:
                if self.mario.onladder:
                    self.mario.jumping = False
                    if (self.mario.posY + 10 > self.ladders[i].posYlow or self.mario.posY + 8 < self.ladders[i].posYlow):
                        if not self.mario.dying:
                            self.mario.ladderUp()
                    if self.mario.posY > self.ladders[i].posYhigh - 18 and self.mario.posY + 10 < self.ladders[i].posYlow:
                        if not self.mario.dying:
                            self.mario.ladderDown()


            if self.mario.onplat == False and self.mario.onladder == False:
                self.mario.fall()

            for j in self.barrels:
                if self.barrels[j].ladder == True:
                    self.barrels[j].ladderMove()
                    self.barrels[j].ladderMove()
                    self.barrels[j].falling = True

                elif self.barrels[j].onPlat == False:
                    self.barrels[j].fall()
                else:
                    self.barrels[j].platMove()

            # print(self.mario.jumping)
            for j in self.barrels:
                if math.sqrt((self.mario.posX - self.barrels[j].posX)**2 + (self.mario.posY - self.barrels[j].posY)**2) < 15:
                    self.mario.dying = True

                if  self.barrels[j].posX == 0 and self.barrels[j].posY > 200:
                    barrel_n = j
                    del_barrel = True
                if -20 < self.mario.posX - self.barrels[j].posX < 20 and 15 < (self.barrels[j].posY - self.mario.posY) < 40:
                    if self.mario.jumping or self.mario.falling:
                        if self.barrels[j].scoreable:
                            self.mario.inRange = True
                            self.mario.score += 100
                            self.barrels[j].scoreable = False


            if del_barrel == True:
                del(self.barrels[barrel_n])
                del_barrel = False

            if barrels_clear or self.mario.dying:
                self.kong.grabbing_barrel = False
                self.kong.throwing = False
                self.barrels.clear()

            if self.mario.posX > 130 and self.mario.posY < 30:
                self.barrels.clear()
                self.mario.win = True


        else:
            if self.mario.score != 0:
                self.highscores.append(self.mario.score)
                self.bubbleSort(self.highscores)
                self.mario.score = 0
                self.highscores.pop()

        if pyxel.btnp(pyxel.KEY_Q):
            with open(self.scores_path, "w") as file:
                file.write(str(self.highscores))
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            with open(self.scores_path, "w") as file:
                file.write(str(self.highscores))
            self.reset()

    def draw(self):
        if not self.mario.dead and not self.mario.win:
            pyxel.cls(0)
            # draw PAULINE
            if self.mario.dying:
                if self.mario.lives == 1:
                    pyxel.blt(150, 19, 2, 122, 196, 16, 12, colkey=0) # Broken heart
                    pyxel.blt(170, 18, 0, 0, 49, 16, 22, colkey=0)
                else:
                    if (pyxel.frame_count//3) % 2 == 0:
                        pyxel.blt(170, 18, 0, 16, 49, 16, 22, colkey=0)
                        pyxel.blt(145, 19, 2, 2, 198, 22, 7, colkey=0)  # HELP!
                    else:
                        pyxel.blt(170, 18, 0, 0, 49, 16, 22, colkey=0)
                        pyxel.blt(145, 19, 2, 34, 198, 22, 7, colkey=0)  # HELP!
            else:
                pyxel.blt(170, 18, 0, 0, 49, 16, 22, colkey=0)

            #draw platforms
            for i in self.platforms:
                pyxel.blt(self.platforms[i].posX, self.platforms[i].posY, 0, 0, 180, 16, 8, colkey=0)


            #draw ladders
            for i in range(1,9):
                x = 118
                y = 236-6*i
                pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey = 0)
            for i in range(1,9):
                x = 50
                y = 183-6*i
                pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey = 0)
            for i in range(1,10):
                x = 130
                y = 133 -6*i
                pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey = 0)
            for i in range(1,7):
                x = 101
                y = 74 -6*i
                pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey = 0)

            pyxel.blt(116, 230, 2, 0, 16, 1, 1, colkey = 0)

            # draw donkey
            pyxel.blt(0, 60, 0, 2, 3, 12, 10, colkey=0) # Side barrel
            if self.kong.throwing:
                change = pyxel.frame_count % 7
                pyxel.blt(self.kong.posX, self.kong.posY, 0, 40, 98, 42, 32, colkey=0)
                if change == 6:
                    self.kong.throwing = False
                    self.kong.grabbing_barrel = True

            elif self.kong.grabbing_barrel:
                change = pyxel.frame_count % 15
                pyxel.blt(self.kong.posX, self.kong.posY, 0, 84, 98, 42, 32, colkey=0)
                if change == 0:
                    self.kong.grabbing_barrel = False
                    self.kong.waiting = True

            elif self.kong.waiting:
                pyxel.blt(self.kong.posX, self.kong.posY, 0, 0, 146, 38, 32, colkey=0)

            else:
                pyxel.blt(self.kong.posX, self.kong.posY, 0, 0, 98, 38, 32, colkey=0)
                
            #draw mario

            if self.mario.dying:
                pyxel.text(self.mario.posX + 10, self.mario.posY - 7, "-200", 8)
                change = (pyxel.frame_count // 6) % 7
                if change == 0 or self.mario.condition:
                    self.mario.condition = True
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 16 * change, 48, 16, 16, colkey=0)
                    if change > 5:
                        self.mario.condition = False
                        self.barrels.clear()
                        self.mario.Death()
                else:
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 0, 48, 16, 16, colkey=0)


            elif self.mario.onladder:
                change = (pyxel.frame_count // 5) % 2
                if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_UP):

                    for i in range(2):
                        pyxel.blt(self.mario.posX, self.mario.posY, 1, 16 * change, 32, 16, 16, colkey=0)
                else:
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 32, 32, 16, 16, colkey=0)

            elif self.mario.direct == 'R':
                if self.mario.jumping or self.mario.falling:
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 31, 0, 16, 16, colkey=0)
                elif pyxel.btn(pyxel.KEY_RIGHT):
                    change = (pyxel.frame_count // 5) % 2
                    for i in range(2):
                        pyxel.blt(self.mario.posX,self.mario.posY, 1, 16 * change, 0, 15, 16, colkey = 0)
                else:
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 0, 0, 16, 16, colkey=0)

            elif self.mario.direct == 'L':
                if self.mario.jumping or self.mario.falling:
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 48, 16, 17, 16, colkey=0)
                elif pyxel.btn(pyxel.KEY_LEFT):
                    change = (pyxel.frame_count // 5) % 2
                    for i in range(2):
                        pyxel.blt(self.mario.posX, self.mario.posY, 1, 16 * change, 16, 16, 16, colkey=0)
                else:
                    pyxel.blt(self.mario.posX, self.mario.posY, 1, 0, 16, 16, 16, colkey=0)

            if self.mario.inRange:
                pyxel.text(self.mario.posX + 10, self.mario.posY - 7, "+100", 11)
                if self.mario.onplat or self.mario.dying or self.mario.onladder:
                    self.mario.inRange = False


            #draw barrel

            for j in self.barrels:
                if self.barrels[j].ladder or self.barrels[j].falling:
                    change2 = (pyxel.frame_count // 2) % 2
                    for i in range(2):
                        pyxel.blt(self.barrels[j].posX, self.barrels[j].posY, 0, 16 * change2, 16, 16, 16, colkey=0)
                else:
                    change2 = (pyxel.frame_count // 3) % 4
                    if self.barrels[j].direct == "R":
                        for i in range(4):
                            pyxel.blt(self.barrels[j].posX, self.barrels[j].posY, 0, 16 * change2, 3, 16, 10, colkey=0)
                    elif self.barrels[j].direct == "L":
                        for i in range(4):
                            pyxel.blt(self.barrels[j].posX, self.barrels[j].posY, 0, 16 * change2, 131, 16, 10, colkey=0)


            # Draw Lives
            for i in range(self.mario.lives):
                pyxel.blt(i*10, 0, 1, 52, 36, 8, 8, colkey=0)

            # Draw Score
            color = 7
            if self.mario.dying:
                color = 8
            pyxel.text(60, 0, "Score: %i" % self.mario.score, color)

            # Draw Christmas Tree
            color_change = pyxel.frame_count//15 % 3
            for i in range(3):
                pyxel.blt(0, 214, 0, color_change * 24, 195, 21, 28, colkey=0)
            if self.mario.inRange:
                pyxel.text(self.mario.posX + 10, self.mario.posY - 7, "+100", 11)
                if self.mario.onplat or self.mario.dying or self.mario.onladder:
                    self.mario.inRange = False


        elif self.mario.win:
            timer = pyxel.frame_count // 30 % 8
            if timer == 0 or self.win_condition:
                self.win_condition = True
                if timer <= 2:
                    self.draw_win()
                else:
                    self.draw_death()
                    if timer == 7:
                        self.win_condition = False
            else:
                self.draw_win()



        else:
            self.draw_death()

    def draw_win(self):
        change2 = (pyxel.frame_count // 3) % 15
        pyxel.cls(change2)
        # draw self.platforms
        for i in self.platforms:
            pyxel.blt(self.platforms[i].posX, self.platforms[i].posY, 0, 0, 180, 16, 8, colkey=0)

        # draw self.ladders
        for i in range(1, 9):
            x = 118
            y = 236 - 6 * i
            pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey=0)
        for i in range(1, 9):
            x = 50
            y = 183 - 6 * i
            pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey=0)
        for i in range(1, 10):
            x = 130
            y = 133 - 6 * i
            pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey=0)
        for i in range(1, 7):
            x = 101
            y = 74 - 6 * i
            pyxel.blt(x, y, 0, 80, 0, 8, 6, colkey=0)
        pyxel.blt(116, 230, 2, 0, 16, 1, 1, colkey=0)

        # draw donkey

        pyxel.blt(self.kong.posX, self.kong.posY, 0, 0, 98, 38, 32, colkey=0)

        # draw mario

        pyxel.blt(self.mario.posX, self.mario.posY, 1, 0, 0, 16, 16, colkey=0)


        # draw PAULINE

        pyxel.blt(170, 18, 0, 0, 49, 16, 22, colkey=0)

        # Draw Heart

        pyxel.blt(150, 19, 2, 99, 196, 16, 12, colkey=0)

        # Draw Christmas Tree

        color_change = pyxel.frame_count // 15 % 3
        for i in range(3):
            pyxel.blt(0, 214, 0, color_change * 24, 195, 21, 28, colkey=0)




    def draw_death(self):
        pyxel.cls(0)
        pyxel.text(pyxel.width//2 - 30, pyxel.height//2 - 8, "RESET? PRESS R", 11)
        pyxel.text(pyxel.width//2 - 28, pyxel.height//2 + 10 - 8, "QUIT? PRESS Q", 8)
        change2 = (pyxel.frame_count//2) % 2
        y=pyxel.frame_count % (pyxel.height)
        for i in range(2):
            pyxel.blt(pyxel.width//2 - 60, y,0, 16 * change2, 16, 16, 16)
            pyxel.blt(pyxel.width//2 + 40, y,0, 16 * change2, 16, 16, 16)
        change2 = (pyxel.frame_count // 3) % 15
        if change2 != 0:
            pyxel.text(pyxel.width//2 - 23, 55, "HIGHSCORES:", change2)
        else:
            pyxel.text(pyxel.width//2 - 23, 55, "HIGHSCORES:", 15)
        for i in range(len(self.highscores)):
            if i == 0:
                pyxel.text(80, 65 + 7 * i, str(i + 1) + '.' + '%i'%(self.highscores[i]), 10)
            elif i == 1:
                pyxel.text(80, 65 + 7 * i, str(i + 1) + '.' + '%i' % (self.highscores[i]), 6)
            elif i == 2:
                pyxel.text(80, 65 + 7 * i, str(i + 1) + '.' + '%i' % (self.highscores[i]), 4)
            else:
                pyxel.text(80, 65 + 7 * i, str(i + 1) + '.' + '%i' % (self.highscores[i]), 7)


    def reset(self):
        self.mario.Reset()
        self.barrels.clear()
            
    def bubbleSort(self, aList):
        
        swapping = True
        num = len(aList) - 1
        
        while num > 0 and swapping:
            swapping = False
            for i in range(num):
                if aList[i] < aList[i + 1]:
                    swapping = True
                    aux = aList[i]
                    aList[i] = aList[i + 1]
                    aList[i + 1] = aux
            num -= 1

# main
Game()
