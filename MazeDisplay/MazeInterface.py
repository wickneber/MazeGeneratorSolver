from MazeDisplay.MazeCanvas import MazeCanvas
from Maze import Maze
import pygame as pg
from MazeGenerator import DepthFirst
from MazeDisplay import MazeDisplay

'''
Main interface of where everything is drawn, this is still a work in progress
'''


class MazeInterface(MazeDisplay.MazeDisplay):

    # Static margins for the maze interface
    right_margin = 150
    left_margin = 20
    bottom_margin = 150
    top_margin = 20

    def __init__(self, cell_rows: int, cell_cols: int, cell_size: int = 20, maze_generators=None, maze_solvers=None):

        super().__init__()
        self.rows = cell_rows
        self.cols = cell_cols
        self.width = screen_width = (cell_rows * cell_size) + MazeInterface.right_margin + MazeInterface.left_margin
        self.height = screen_height = (cell_cols * cell_size) + MazeInterface.top_margin + MazeInterface.bottom_margin
        self.canvas = pg.display.set_mode((screen_width, screen_height))

        # Give the MazeCanvas control over the main canvas so the algorithms can draw onto the screen
        self.algorithm_interface = MazeCanvas((cell_rows, cell_cols), self.canvas)
        self.maze = Maze(cell_rows, cell_cols)  # maze instance

        if not maze_generators:
            self.maze_generators = [DepthFirst.DepthFirst(self.maze, self.algorithm_interface)]
        else:
            self.maze_generators = maze_generators.append(
                DepthFirst.DepthFirst(self.maze, self.algorithm_interface))

        # TODO, when maze solvers are made, append a default one to the solver
        self.maze_solvers = maze_solvers
        self.init_interface()

    def init_interface(self) -> None:
        '''

        Initializes all the variables needed to (re)start the solving and draw a new unsolved maze onto the screen
        Returns: None

        '''
        for generator in self.maze_generators:
            generator.init()
        '''
        for solver in self.maze_solvers:
            solver.init()
        '''
        maze_width = self.width
        maze_height = self.height
        self.width *= self.cell_size
        self.height *= self.cell_size
        self.canvas.fill(MazeDisplay.MazeDisplay.white)

        current_x = MazeInterface.left_margin
        current_y = MazeInterface.top_margin

        # Draw a maze with all the cells unvisited
        for row in range(maze_height):
            for col in range(maze_width):
                self.draw_left_wall(current_x, current_y)
                self.draw_top_wall(current_x, current_y)
                self.draw_right_wall(current_x, current_y)
                self.draw_bottom_wall(current_x, current_y)
                current_x += self.cell_size
            current_x = MazeInterface.left_margin
            current_y += self.cell_size
        pg.display.flip()

    def mainloop(self) -> None:
        '''

        Where the interface loop resides.
        Returns: None

        '''

        while(True):
            for env in pg.event.get():
                pg.event.pump()
                # just to check to see if depth first works
                self.maze_generators[0].create_maze()
                if env.type == pg.QUIT:
                    pg.quit()