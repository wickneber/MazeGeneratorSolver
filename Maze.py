
from Cell import Cell
import Direction as maze_dir
from Errors import OutOfBoundsError


class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = []
        self.visited = set()
        self.init()

    def __str__(self) -> str:
        return ""

    def init(self):
        """
        Initializes the maze with a grid of cells of given width and height and clear the visited array
        Returns: None

        """
        self.grid = [[Cell() for i in range(self.height)] for j in range(self.width)]
        self.visited = set()

    def remove_wall(self, x: int, y: int, direction: maze_dir.Direction) -> None:
        """
        Given the x and y values of a cell, remove
        Args:
            direction (): The direction object to check to see if the wall exists
            x (): The x coordinate of the Cell
            y (): The y coordinate of the Cell

        Returns: None

        """

        # First check to see if the x and y coordinates are in range
        if not self.is_within_bounds(x, y):
            raise OutOfBoundsError

        # Then remove the wall in given the direction
        self.grid[x][y].remove_wall(direction)

    def get_cell(self, x: int, y: int) -> type(Cell):
        """
        Given an x and y coordinate, get the Cell corresponding to it
        Args:
            x (): The x coordinate of the Cell
            y (): The y coordinate of the Cell

        Returns: The Cell at x, y

        """
        # Check to see if the given coordinate is valid
        if not self.is_within_bounds(x, y):
            raise OutOfBoundsError

        return self.grid[x][y]

    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Checks to see if the x and y coordinates given are valid
        Args:
            x (): The x coordinate to check
            y (): The y coordinate to check

        Returns: Boolean value of whether or not the value is within bounds

        """

        return (0 <= x < len(self.grid)) and (0 <= y < len(self.grid[0]))

    def is_visited(self, x: int, y: int) -> bool:
        """
        Given an x and y location, check to see if the value is visited or not
        Args:
            x (): X coordinate of the maze
            y (): Y coordinate of the maze

        Returns: A boolean value corresponding to whether or not the cell has been visited

        """
        if self.is_within_bounds(x, y):
            return self.get_cell(x, y).visited

        # If the maze is not within bounds raise an exception
        raise OutOfBoundsError

    # May not even need this function
    def is_valid_removal(self, x: int, y: int) -> bool:
        """
        Checks to see if the desired Cell given the coordinates has already been visited
        Args:
            x (): The x coordinate of the Cell to check
            y (): The y coordinate of the Cell to check

        Returns: Boolean (if the desired cell is within bounds and Cell at the coordinate has not been visited)

        """
        # First check to see if this is a valid coordinate
        if not self.is_within_bounds(x, y):
            return False

        return not (x, y) in self.visited

    def get_width(self) -> int:
        """
        Gets the width of the maze
        Returns: The width of the maze

        """
        return self.width

    def get_height(self) -> int:
        """
        Gets the length of the maze
        Returns: Length of the maze as an int

        """
        return self.height

    def get_size(self) -> int:
        """
        Gets the size of the maze (width*height)
        Returns: The size of the maze

        """
        return self.width * self.height
