import pygame

class Tile(object):

    # Author: Dustin Hu, 2014-11-25; Jacky Xao, 2015-01-22;
    # Purpose: To hold a tile that makes up the background
    
    # Parameters:
        # filename: filename of the tile
        # blnpass: is the tile passable
    # Fields: 
        # image: The image to load from
        # passable: Whether you can pass over the tile
    # Methods:
        # draw: Draws the tile

    # TODO: change seperate artwork images into one giant tileset
            # this would change filename to the tileset image
            # and add tile coordinates?
    def __init__(self, filename = "default.png", blnpass = False):
        # Author: Dustin Hu. 2014-11-25; Jacky Xao, 2015-05-08;
        if not ("artwork/" in filename):
            filename = "artwork/"+ filename
        self.passable = blnpass
        try:
            self.image = pygame.image.load(filename).convert()
        except Exception:
            print ("Error in Tile __init__")
            raise Exception
            pygame.quit()

    def draw(self, destination, x, y):
        # Author: Dustin Hu, 2014-11-25
        # Purpose: To draw the tile
        # Input: The destination to draw to, and the x y coordinates of the top left of where it is to be drawn
        destination.blit(self.image, (x, y))
        return (self.passable)
        