
import pygame as pg
from Cell import Cell

'''
General Maze display class that MazeInterface and MazeCanvas inherit from
'''


class MazeDisplay:

    white = (255, 255, 255)
    black = (0, 0, 0)
    cell_size = 20  # Cell size in pixels
    line_width = 2  # Line width in pixels

    def __init__(self):
        self.canvas = None
        self.cell_size = MazeDisplay.cell_size    # Default cell size
        self.line_width = MazeDisplay.line_width  # Default line width
        self.start_x = 0
        self.start_y = 0

    def draw_cell(self, row: int, col: int, cell: Cell) -> None:
        start_x = (self.cell_size * col) + self.start_x
        start_y = (self.cell_size * row) + self.start_y

        if cell.left_wall:
            self.draw_left_wall(start_x, start_y)

        if cell.right_wall:
            self.draw_right_wall(start_x, start_y)

        if cell.top_wall:
            self.draw_top_wall(start_x, start_y)

        if cell.bottom_wall:
            self.draw_bottom_wall(start_x, start_y)

    def draw_left_wall(self, start_x: int, start_y: int) -> None:
        """
        Given the starting x and y values, draw the left wall of a cell onto the screen
        Args:
            start_x (): The starting x coordinate
            start_y (): The starting y coordinate

        Returns: None

        """
        self.draw_line((start_x, start_y),
                       (start_x, start_y + self.cell_size))

    def draw_right_wall(self, start_x: int, start_y: int) -> None:
        """
        Given the starting x and y addresses, draw the right wall of a cell onto the screen
        Args:
            start_x (): The starting x coordinate
            start_y (): The starting y coordinate

        Returns: None

        """
        self.draw_line((start_x + self.cell_size, start_y),
                       (start_x + self.cell_size, start_y + self.cell_size))

    def draw_top_wall(self, start_x: int, start_y: int) -> None:
        """
        Given the starting x and y addresses, draw the top wall of a cell onto the screen
        Args:
            start_x (): The starting x coordinate
            start_y (): The starting y coordinate

        Returns: None

        """
        self.draw_line((start_x, start_y),
                       (start_x + self.cell_size, start_y))

    def draw_bottom_wall(self, start_x: int, start_y: int) -> None:
        """
        Given the starting x and y addresses, draw the bottom wall of a cell onto the screen
        Args:
            start_x (): The starting x coordinate
            start_y (): The starting y coordinate

        Returns: None

        """
        self.draw_line((start_x, start_y + self.cell_size),
                       (start_x + self.cell_size, start_y + self.cell_size))

    def draw_line(self, fro: (int, int), to: (int, int), color: (int, int, int) = (0, 0, 0)) -> None:
        """
        Does the same thing as pg.draw.line() but is a shorter function call
        Args:
            color (): The color of which to draw the line
            to (): Tuple containing the starting x and y locations
            fro (): Tuple containing the ending x and y locations

        Returns: None

        """

        pg.draw.line(self.canvas, color, fro, to, self.line_width)

