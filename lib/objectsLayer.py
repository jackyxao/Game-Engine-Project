from lib.interactableObject import InteractableObject
from lib.pathway import Pathway

class Objects:
# Author: Jacky Xao, 2016-05-08
# Purpose: To hold all the objects that corrisponds to a map,
    # Sets up the object layer by creating the array

# Parameters:
    #mapRef: a pointer* of the map, for communications
    #objFile: file containing all the objects needed for the map
    # import files look like this (ignore #):
    #   [x,y][p] Object.txt
    #   [x2,y2][c] Object2.txt
    #   ...etc.
# Fields:
    # map: map address
    # grid: 2D array of objects and nulls
# Methods:
    # draw: draw the objects on top of the map
    # [x,y] is grid coords, counting starts at 1
    # [p] is type of object, single character
        # p: pathway
        # c: chest
        # TODO: and more
    # filename of the object
    def __init__(self,mapRef,objFile):
        #Grid Set-up
        self.map = mapRef
        self.grid = []
        for x in xrange(self.map.size[0] + 1):
            temp = []
            for y in xrange(self.map.size[1] + 1):
                temp.append(None)
            self.grid.append(temp)
            
        #Object Import
        if not "data/obl/" in objFile:
            objFile = "data/obl/" + objFile
        inputData = open(objFile, 'r').read()
        temp = inputData.splitlines()
        for line in temp:
            c = line[1:line.index("]")]
            coord = [int(c[:c.index(",")]),int(c[c.index(",")+1:])]
            objType = line[line.index("]")+2]
            line = line[line.index("]")+4:].strip()
            #'line' = file_name
            #object creation
            if objType == 'p':
                newObj = Pathway(coord,self.map,line,objType)
            self.grid[coord[0]][coord[1]] = newObj
            
    def draw(self,destination,x,y):
        #Author: Jacky Xao
        #Date: 26-04-15
        #Purpose: draws the objects on top of the map
        #Input:
            #destination: object to draw on
            #x,y:Initial x,y coordinates
        # Update 10-05-2015 by Jacky Xao
        # added +1 to across and down to accomendate for the map borders
        # Update 24-05-2015 by Jacky Xao
        # removed +1 to across and down, for coord system fix
        for across in xrange(len(self.grid)):
            for down in xrange(len(self.grid[across])):
                if self.grid[across][down] != None:
                    self.grid[across][down].draw(destination,(across)*25+x,(down)*25+y)
