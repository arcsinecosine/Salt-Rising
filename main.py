from game import * 
import pygame
from pygame.locals import *
from util import *

def main():
    pygame.init()
    display = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Salt Rising')
    ding = test()
    while True:
        display.blit(ding.image,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)

if __name__ == '__main__':
    main()



