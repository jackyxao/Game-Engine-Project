from tile import Tile
import pygame

class Map (object):

    # Author: Dustin Hu, 2014-12-08; Jacky Xao, 2015-05-10;
    # Purpose: create the map layer

    # Parameter:
        # fileName: The file name to read from
    # Fields:
        # map: 2D array of tiles. map[column][row]
        # template: The template in an array of chars
        # music: music for the map
        # size: tuple of (x,y). Deal with it.

    # == Template == #
    # the input file looks something like this, ignore the hashes.
    #
    #    [Map]
    #    13
    #    10
    #    |
    #    |
    #    |
    #    |$$$$$$$$$$$$
    #        \    *
    #        \    *
    #        \    *
    #        \    *
    #        \    *
    #    )))))))))))))
    #    [Key]
    #    | = Green.png[]
    #    $ = Pink.png
    #    \ = Blue.png
    #    * = Red.png
    #    ) = Purple.png
    #    [Music]
    #    song.mp3
    #

    # As you can see, the file starts off with [Map].
    # After [Map], the 2 integer represents the width and height of the map (x,y)
    # You do not need to accomindate for the safety borders.

    # After this is the map to turn into an array, and it will
    # continue reading the map into the array until it reaches [Key]. Preferably,
    # the entire space of the map should be filled with symbols, otherwise,
    # it will be filled with black, default, unpassable space tiles.

    # Forbidden characters for the map are '[', ']', and '=', as these are required for
    # reading of the file. Also, ' ' (a.k.a ascii 32) represents default, so don't overwrite it

    # [Key] section tells the computer which symbols mean which tile
    # [] at the end signifies that the tile is unpassable
    # The line after [Music] is the mp3 file for the map

    # Methods:
        # __str__: Prints the map in the template field as plaintext
        # draw: To draw the background
        # playMusic: plays the music
        # stopMusic: stops the music
        # mapOverride: it does something. Might wanna change the logic

    def __init__(self, fileName):
        # Author: Dustin Hu, 2014-12-08; Jacky Xao, 2015-04-02
        if not "data/map/" in fileName:
            fileName = "data/map/" + fileName
        try:
            inputData = open(fileName, 'r').read()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            pygame.quit()
            raise Exception

        inputData = open(fileName, 'r').read()
        temp = inputData.splitlines()

        self.template = []
        self.template = temp[3:temp.index("[Key]")]

        self.size = ((int)(temp[1]),(int)(temp[2]))
        musicFile = temp[temp.index("[Music]") + 1:][0]
        pygame.mixer.init()
        self.music = pygame.mixer.music.load("music/" + musicFile)

        keyTable = {}
        passTable = {}

        keyTable[" "] = "default.png"
        passTable[" "] = False
        #Sets up dictionaries
        temp = temp[temp.index("[Key]") + 1:temp.index("[Music]")] #Substring
        for line in temp:
            line = line.strip()
            sign = line[0:line.find("=")].strip()
            line = line[line.find("=")+1:].strip()

            if line.find("[]") == -1:
                value = line
                walk = True
            else:
                value = line[0:line.find("[]")].strip()
                walk = False

            passTable[sign] = walk
            keyTable[sign] = value

        #sets up the map
        self.map = []
        for x in xrange(self.size[0] + 2):
            column = []
            for y in xrange(self.size[1] + 2):
                column.append(Tile())
            self.map.append(column)

        for down in xrange(self.size[1]):
            across = 1
            for char in self.template[down]:
                if char != ' ':
                    self.map[across][down + 1] = Tile(keyTable[char],passTable[char])
                across += 1


    def __str__(self):
        output = ""
        for line in self.template:
            output = output + line + "\n"

        return output

    def draw (self,destination,x,y):
        # Author: Jacky Xao, 2015-01-25
        # Purpose: To draw the map
        # destination: The destination to draw to
        # x,y: the top left coordinates to draw

        for across in xrange(0, self.size[0] + 2):
            for down in xrange(0, self.size[1] + 2):
                #add if statement for -ve x,y coords, so if -ve, don't draw
                #use and
                self.map[across][down].draw(destination, (x + (across * 25)), (y + (down * 25)))

    def playMusic (self):
        # Author: Jacky Xao, 2015-04-02
        # Purpose: start playing the music FOREVER
        pygame.mixer.music.play(-1)

    def stopMusic (self):
        # Author: Jacky Xao, 2015-04-02
        # Purpose: stop playing the music
        pygame.mixer.music.stop()

    def mapOverride (self, mapOR):
        # Author: Jacky Xao, 2015-05-10
        # Purpose: Update the original map w/ event changes
            # Basically changes the tiles
        # mapOR: the Overriding file
            #Maybe lineN, line number or something, depending on how the file is saved

        #Map Override files are stored like this:
            # [x,y] image_file.png []

            # [x,y] is the coordinates of the affected tile
            # image file.png is the new image file with the same features as map ([])

        inputData = open(mapOR, 'r').read()
        temp = inputData.splitLines()
        for line in temp:
            c = line[1:line.index("]")]
            coord = [int(c[:c.index(",")]),int(c[c.index(",")+1:])]
            line = line[line.index("]")+1:]
            if line.find("[]") == -1:
                value = line.strip()
                walk = True
            else:
                value = line[0:line.find("[]")].strip()
                walk = False

            newTile = Tile(line,walk)
            self.map[coord[0]][coord[1]] = newTile
