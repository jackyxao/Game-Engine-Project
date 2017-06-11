import pygame

from pygame.locals import*

from lib.map import Map
from lib.character import Character
from lib.objectsLayer import Objects

class engine:
    # Author: Jacky Xao, 2016-05-10
    # This is essentially the game engine that will run everything
    # Very prototype. Will change a lot
    # Parameters:
        # inputFilename: atm, it's just a map name (that has a corrisponding obj file)
        # (x,y): Initial coordinates for the map
    # Fields:
        # screen: the screen
        # char: the character
        # map: the current map
        # objL: the objects for the current map
        # x,y: top left pixel coords of the map on the screen
    # Methods:
        # draw: draws map, then objects, then character* (order might change)
        # travelTest: prototype for travelling to a different map
        # calcCC: calculate character pixel coords
        # check_movement: check if the arrow keys were pressed and move
        # run: temporary mainloop, (just a shitty infinite loop)
    def __init__(self,inputFilename,x,y):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((0, 0, 0))
        pygame.key.set_repeat(10,200)
        
        self.map = Map(inputFilename+".map")
        self.objL = Objects(self.map,inputFilename+".obl")
        self.x = x
        self.y = y
        self.char = Character(self.screen,"name.chr",(2,2),self.map)
        self.char.initImages()
        self.draw()

    def draw(self):
        self.map.draw(self.screen,self.x,self.y)
        self.objL.draw(self.screen,self.x,self.y)
        self.char.draw(self.x,self.y)
        pygame.display.flip()
        
    def travelTest(self):
        if self.objL.grid[self.char.coord[0]][self.char.coord[1]] != None:
            if self.objL.grid[self.char.coord[0]][self.char.coord[1]].type == 'p':
                if self.objL.grid[self.char.coord[0]][self.char.coord[1]].condition == 1:
                    print ("CAN TRAVEL")
                    door = self.objL.grid[self.char.coord[0]][self.char.coord[1]]
                    newMap = door.path
                    self.map = Map(newMap)
                    newmap = newMap[:newMap.index('.')]
                    self.objL = Objects(self.map,newmap+".obl")
                    self.char.layout = self.map
                    self.char.coord = [2,2]
                    self.x = 0
                    self.y = 0
                    self.screen.fill((0, 0, 0))
                    self.draw()
                    print ("New MAP!")

    def calcCC(self,n):
        if n == 0:
            c = self.char.coord[0] * 25 + self.x
        else:
            c = self.char.coord[1] * 25 + self.y
        print (self.char.coord[1])
        return c
    
    def check_movement(self, event):
        if event.key==K_UP:
            # if self.char.coord[1] > 10 and self.char.coord[1] < (self.map.size[1] - 10):
            #     if self.char.canMove(0):
            #         self.y += 25
            #         self.char.moveMap(0,self.x,self.y)
            # else:
            #     self.char.moveChar(0,self.x,self.y)
            self.char.moveChar(0,self.x,self.y)
        elif event.key==K_RIGHT:
            # if self.char.canMove(1):
            #     self.x -= 25
            #     self.char.moveMap(1,self.x,self.y)
            self.char.moveChar(1,self.x,self.y)
        elif event.key==K_DOWN:
            # if self.char.coord[1] < (self.map.size[1] - 10) and self.char.coord[1] > 10:
            #     if self.char.canMove(2):
            #         self.y -= 25
            #         self.char.moveMap(2,self.x,self.y)
            # else:
            #     self.char.moveChar(2,self.x,self.y)
            self.char.moveChar(2,self.x,self.y)
        elif event.key==K_LEFT:
            # if self.x <= 30:
            #     if self.char.canMove(3):
            #         self.x += 25
            #         self.char.moveMap(3,self.x,self.y)
            # else:
            #     self.char.moveChar(3,self.x,self.y)
            self.char.moveChar(3,self.x,self.y)
        pygame.display.flip()

    def run(self):
        run = True
        self.map.playMusic()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.check_movement(event)
                    self.travelTest()
                elif event.type == pygame.QUIT:
                    run = False
        pygame.quit()
        
        
X = engine("testMap",10,10)
X.run()
