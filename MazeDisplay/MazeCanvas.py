import pygame as pg
from Maze import Maze
import Cell
from MazeDisplay import MazeDisplay

'''
Class that handles the drawing of a maze. This is the main interface of which the drawing algorithms will draw to the
screen.
'''


class MazeCanvas(MazeDisplay.MazeDisplay):

    def __init__(self, start_x_y: (int, int), canvas: pg.display, cell_size: int = 20):
        super().__init__()
        self.start_x, self.start_y = start_x_y
        self.canvas = canvas
        self.cell_size = cell_size  # size of the cell in pixels
        self.line_width = 2

    '''
    def init_canvas(self) -> None:
        maze_width = self.
        maze_height = self.height
        self.width *= self.cell_size
        self.height *= self.cell_size
        self.canvas.fill(MazeCanvas.white)

        current_x = self.start_x
        current_y = self.start_y

        # Draw a maze with all the cells unvisited
        for row in range(maze_height):
            for col in range(maze_width):
                self.draw_left_wall(current_x, current_y)
                self.draw_top_wall(current_x, current_y)
                self.draw_right_wall(current_x, current_y)
                self.draw_bottom_wall(current_x, current_y)
                current_x += self.cell_size
            current_x = int(self.padding/2)
            current_y += self.cell_size
        pg.display.flip()
    '''

    def render_maze(self, maze: Maze) -> None:
        """

        Given a maze object draw it onto the screen
        Args:
            clock (): The pygame clock instance for frame rate handling
            maze (): The maze object of which to draw to the screen

        Returns: None

        """
        # Clear the screen
        self.canvas.fill(MazeCanvas.white)
        for row in range(len(maze.grid)):
            for col in range(len(maze.grid[row])):  # go through each row
                self.draw_cell(row, col, maze.get_cell(row, col))
        pg.event.pump()
        pg.display.flip()
