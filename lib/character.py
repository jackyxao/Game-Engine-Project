import pygame

class Character(object):
    # Author: Dustin Hu, 2015-01-12;
    # Purpose: To create the character, and to draw it
    # ATTENTION: IN ORDER TO DRAW THE CHARACTER, YOU MUST FIRST RUN initImages()

    # Methods:
    # __init__: the initilization, creates the character, reading from a character file (.chr)
    #           .chr file outline:
    #           name = name
    #           imgNorth = imgNorth.png
    #           imgEast = imgEast.png
    #           imgSouth = imgSouth.png
    #           imgWest = imgWest.png

    # draw: blits the character to a surface
    # moveChar: Moves the character around on the surface
    # erase: Erases the character from the surface
    # initImages: Initializes the images
    # moveMap: move the map, keeping the character centred
    # write: Writes data fields to a save file with extension .chr

    # Data fields:
    # charFile: The file to read from
    # surface: The surface the character sholud be drawn to. The reason for having a surface variable
    #          is such that we can have a single surface for character objects for ease of tracking
    # images: The array of images holding the character
    # direction: The direction the character is facing, an integer from 0-3, where  NESW=0123
    # coord: The coordinates of the character in the current map, an array of [x,y], defaulted to (0, 0)

    # START COUNTING FROM 1 NOT 0 (SHOULD REALLLY FIX THIS)
    def __init__(self, surface = None, charFile = "name.chr", coord = (0, 0), layout = None):
        # Author: Dustin Hu, 2015-01-12;
        if not "data/char/" in charFile:
            charFile = "data/chr/" + charFile
        self.surface = surface
        self.images = []
        self.charFile = charFile
        try:
            inputData = open(self.charFile, 'r').read()
            nameInput = inputData.split("\n")

            self.name = nameInput[0]
            self.name = self.name[self.name.find("=")+1:].strip()

            self.coord = list(coord)
            self.direction = 0
            self.layout = layout

        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            pygame.quit()
            raise Exception
        except NameError as e:
            print "Name error:", e.strerror
            pygame.quit()
            raise Exception
    def draw(self, x, y):
        # Author: Dustin Hu, 2015-01-12; Jacky Xao, 2015-03-06;
        # Purpose: To draw the character to the predefined surface
        # x,y: initial x,y coords of the map/screen/thing

        self.surface.blit(self.images[self.direction], (self.coord[0] * 25 + x, self.coord[1] * 25 + y))

    def moveChar(self, direction, x, y):
        # Author: Dustin Hu, 2015-01-12; Jacky Xao, 2015-03-07;
        # Purpose: To move the character
        # direction: direction to move in, either 0, 1, 2, or 3, which will increment the coordinates by 25
        # x,y: initial coords

        self.direction = direction
        if self.canMove(direction):
            if (direction == 0):
                self.layout.map[self.coord[0]][self.coord[1]].draw(
                    self.surface, x + (self.coord[0] * 25), y + (self.coord[1] * 25))
                self.coord[1] = self.coord[1] - 1

            elif (direction == 1):

                self.layout.map[self.coord[0]][self.coord[1]].draw(
                    self.surface, x + (self.coord[0] * 25), y + (self.coord[1] * 25))
                self.coord[0] = self.coord[0] + 1

            elif (direction == 2):
                self.layout.map[self.coord[0]][self.coord[1]].draw(
                    self.surface, x + (self.coord[0] * 25), y + (self.coord[1] * 25))
                self.coord[1] = self.coord[1] + 1

            else:
                self.layout.map[self.coord[0]][self.coord[1]].draw(
                    self.surface, x + (self.coord[0] * 25), y + (self.coord[1] * 25))
                self.coord[0] = self.coord[0] - 1

        self.draw(x,y)

    def moveMap(self, direction, x, y):
        # Author: Jacky Xao, 2015-03-04;
        # Purpose: keeps the character centred and moves the map
        # direction: direction to move in, either 0, 1, 2, or 3, which will increment the coordinates by 25
        # x,y: initial x,y coords of the map/screen/thing

        self.direction = direction
        if self.canMove(direction):
            if (direction == 0):
                self.coord[1] = self.coord[1] - 1
                self.layout.draw(self.surface,x,y)

            elif (direction == 1):
                self.coord[0] = self.coord[0] + 1
                self.layout.draw(self.surface,x,y)

            elif (direction == 2):
                self.coord[1] = self.coord[1] + 1
                self.layout.draw(self.surface,x,y)

            else:
                self.coord[0] = self.coord[0] - 1
                self.layout.draw(self.surface,x,y)

        self.draw(x,y)

    def canMove(self, direction):
        # Author: Jacky Xao, 2015-03-07;
        # Purpose: checks if the character can move or not
        # direction, the direction they're heading
        # return: true is can move, false otherwise
        
        move = False
        if direction == 0:
            move = self.layout.map[self.coord[0]][self.coord[1] - 1].passable
        elif direction == 1:
            move = self.layout.map[self.coord[0] + 1][self.coord[1]].passable
        elif direction == 2:
            move = self.layout.map[self.coord[0]][self.coord[1] + 1].passable
        elif direction == 3:
            move = self.layout.map[self.coord[0] - 1][self.coord[1]].passable
        return move

    def moveCentredAnimated(self,direction):
        # Author: Jacky Xao, 2015-04-09;
        # Purpose: keeps the character centred and moves the map with animations
        # direction: direction to move in, either 0, 1, 2, or 3, which will increment the coordinates by 25
        # WIP
        
        self.direction = direction

        if (direction == 0):
            if self.layout.map[self.coord[0]][self.coord[1]-1].passable:
                self.coord[1] = self.coord[1] - 1
                self.y += 12
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()
                pygame.display.flip()
                self.y += 13
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()

        elif (direction == 1):
            if self.layout.map[self.coord[0]+1][self.coord[1]].passable:
                self.coord[0] = self.coord[0] + 1
                self.x -= 12
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()
                pygame.display.flip()
                self.x -= 13
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()

        elif (direction == 2):
            if self.layout.map[self.coord[0]][self.coord[1]+1].passable:
                self.coord[1] = self.coord[1] + 1
                self.y -= 12
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()
                pygame.display.flip()
                self.y -= 13
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()

        else:
            if self.layout.map[self.coord[0]-1][self.coord[1]].passable:
                self.coord[0] = self.coord[0] - 1
                self.x += 12
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()
                pygame.display.flip()
                self.x += 13
                self.layout.draw(self.surface,self.x,self.y)
                self.draw()

    def initImages(self):
        # Author: Dustin Hu, 2015-02-24; Jacky Xao, 2015-01-04;
        # Purpose: To initialize just the images of the character
        try:
            inputData = open(self.charFile, 'r').read()
            temp = inputData.split("\n")
            temp = temp[1:]
            for i in xrange(4):
                line = temp[i]
                filename = line[line.find("=") + 1:].strip()
                image = pygame.image.load("artwork/" + str(filename))
                self.images.append(image)
        except:
            print "error in initImages"
            pygame.quit()
            raise Exception

    def write(self):
        # Author: Jackie Xu, 2015-03-23
        # Purpose: To write the characteristics (data fields) of the the character to a .cht file

        output = open("name.chr", "w")
        output.write("name = " + str(self.charFile))
        output.write(self.surface)
        for i in self.images:
            output.write(i)
        output.write(str(self.direction))
        output.write(self.coord)
        output.close()

    def read(self):
        # Author: Jackie Xu, 2015-03-23
        # Purpose: To read the characteristics (data fields) from the a.cht character file

        file = open("name.chr", "r")

        list = []
        for line in file:
            list.append(line)
        self.charFile = str(list[0])
        self.surface = str(list[1])
        self.images = str(list[2])
        self.direction = str(list[3])
        self.coord = str(list[4])
        file.close()
