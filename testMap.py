import sys
import pygame

from lib.map import Map

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))

    try:
        # enter the filename and path
        a = Map("data/map/testMap.map")
    except:
        #print sys.exc_info()[0]
        pygame.quit()
        raise Exception
    a.draw(screen, 10, 10)
    a.playMusic()
    pygame.display.flip()
        
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

# tests the map and tile class