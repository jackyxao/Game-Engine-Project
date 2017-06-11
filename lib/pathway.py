from lib.interactableObject import InteractableObject
from lib.tile import Tile

#Pathway Class
#Author: Jacky Xao
#Date: 26-04-15
#Purpose: To act as an interactable object where the character can
        # travel across different maps and rooms

    #Fields:
        #grid: coordinates of object on map, tuple
        #map: map reference
        
        #state: True for open, False for closed
        #path: next map.txt
        #condition: True if meet, false otherwise
            #for locked/blocked paths
        #images: open/closed* images
    #Methods:
        #action: calls unlock, open, or do nothing (event?)
        #draw: draws the pathway image
        #openPath: flips the boolean + draw
        #unlock: flips the boolean + message?

    #Object Import File Format:
    #p
    #[path]nextMap.txt
    #[image0]closed.png *None
    #[image1]open.png
    #[state]1 *0
    #[condition]1 *0

#Update 2015-05-10 by Jacky Xao
        #Improved the data import methods
        #Added a write method for the mapOverride4
#Update 2015-05-17 by Jacky Xao
        #Added the input file layout
        #Implemented class inheritance
        #Changed images to tiles
#Update 2015-05-24 by Jacky Xao
        #Added objType to constuctor
        
class Pathway(InteractableObject):
    def __init__(self,grid,mapRef,fileName,objType):
        InteractableObject.__init__(self,grid,mapRef)
        self.fileName = fileName
        self.type = objType
        if not "data/obl/" in self.fileName:
            self.fileName = "data/obl/" + self.fileName
        inputData = open(self.fileName, 'r').read()
        inputData = inputData.splitlines()
        self.path = inputData[1][6:].strip()
        
        if inputData[4][7] == '1':
            self.state = True
        else:
            self.state = False
        
        if inputData[5][11] == '1':
            self.condition = True
        else:
            self.condition = False
        if inputData[2][8:].strip() == "None":
            img0 = None
        else:
            img0 = Tile(inputData[2][8:].strip(),False)
        img1 = Tile(inputData[3][8:].strip(),True)
        self.images = (img0,img1)

    def draw(self,destination,x,y):
        #Author: Jacky Xao
        #Date: 2015-04-26
        #Purpose: Draws the objects to the screen
        #UPDATED 2015-05-11 by Jacky Xao
        #Input: destination, (x,y) SCREEN coords
        #UPDATED 2015-05-17 by Jacky Xao
        #Instead of blit, it sets the map tile to this one
        #and redraws it
        #Updated 2015-05-18 by Jacky Xao
        #added .map to mapRef
        if self.state:
            #print (self.grid)
            self.mapRef.map[self.grid[0]][self.grid[1]] = self.images[1]
        else:
            self.mapRef.map[self.grid[0]][self.grid[1]] = self.images[0]
            
        self.mapRef.map[self.grid[0]][self.grid[1]].draw(destination,x,y)

    """def openPath (self):
        if self.condition and not self.state:
            self.state = True"""
    #def action(self):
        #Author: Jacky Xao
        #Date: 18-05-2015
        #Purpose: I forgot

    #def travel(self):
        #Author: Jacky Xao
        #Date: 18-05-2015
        #Purpose: Travel to the next map
            
            
            
            
