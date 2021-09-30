
from Maze import Maze
import pygame
from MazeGenerator import DepthFirst
from MazeDisplay import MazeCanvas
from MazeDisplay import MazeInterface

if __name__ == "__main__":
    '''
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Playing with Pygame")
    clock = pygame.time.Clock()
    '''
    pygame.init()
    int = MazeInterface.MazeInterface(70, 70, 10)
    try:
        while(1):
            pygame.event.pump()
            int.mainloop()

    except KeyboardInterrupt:
        pygame.quit()


