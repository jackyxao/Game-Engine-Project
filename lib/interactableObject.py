# Author: Jacky Xao
# Date: 26-04-15
# Purpose: Interable object class (chests, doors etc.)
    #Originally done by Jack.ie.Xu, but Jacky X remade it for
    #   adding subclasses
# Fields:
    #grid: coordinates of object on map, tuple
    #mapRef: a reference to the current map
    #tile: the tile which contains the object image
    #type: type of object
# Methods:
    # draw()*
    # action()*
# Update by Jacky Xao on 05-17-15
    #changed the constructor
    #"abstract" draw and action
        #will be defined in the subclass
# Update by Jacky Xao on 25-05-2015
    #Added new field, type, keeps track of type of obj

class InteractableObject:
    # Constructor
    # Inputs: the coords of the objects, location of map to place in
    
    def __init__(self,grid,mapRef):
        self.grid = grid
        self.mapRef = mapRef
        self.tile = None
        self.type = None
            
    # Draw() method
    # Draws the texture of object at a given location
    # Inputs: Distination of object, x and y coordinates of where the object is drawn

    #def draw(self, destination, x, y):
        # Author: Jacky Xao
        # Date: 11-05-2015
        # Purpose: draws the image
        # Input: the destination to draw to, (x,y) is the SCREEN coords
        #destination.blit(self.image, (x,y))


    #def action(self, command):
        #return "null"

    #Updated
