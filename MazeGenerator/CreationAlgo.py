
from Maze import Maze
import abc
import Direction as maze_dir
from MazeDisplay.MazeCanvas import MazeCanvas

'''
Base class for maze solving, does not do anything by itself made to be inherited
'''


class CreationAlgo(abc.ABC):
    def __init__(self, maze: Maze, canvas: MazeCanvas):
        self.name = 'Default name'
        CreationAlgo.maze_maze_directions = [maze_dir.LeftWall,
                                             maze_dir.RightWall,
                                             maze_dir.BottomWall,
                                             maze_dir.TopWall]  # valid maze_directions
        self.maze = maze
        self.canvas = canvas

    @abc.abstractmethod
    def init(self) -> None:
        '''

        Initializes all the variables needed to (re)start the solving
        Returns: None

        '''
        pass

    @abc.abstractmethod
    def create_maze(self, row_col: (int, int) = (0, 0)) -> None:
        """
        Given a maze instance, use a specified algorithm to solve the maze
        Args:
            row_col (): The starting coordinate for the algorithm to generate the maze
            maze (): Maze instance to solve

        Returns: None

        """
        pass

    @abc.abstractmethod
    def get_valid_moves(self, x: int, y: int) -> [(int, int)]:
        """
        Given a x, y, and maze object get all the valid moves for that given coordinate
        Args:
            x (): X coordinate in the maze
            y (): Y coordinate in the maze
            maze (): The maze object of which we are trying to create a maze from

        Returns: A list of (int, int) tuples that correspond to maze_directions that the agent can traverse

        """
        pass
