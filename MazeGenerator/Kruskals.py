import MazeGenerator.CreationAlgo as MazeCreator
from Maze import Maze
import random
import Direction as maze_dir
from MazeDisplay.MazeCanvas import MazeCanvas


class Kruskals(MazeCreator.CreationAlgo):

    def __init__(self, maze: Maze, canvas: MazeCanvas):
        super().__init__(maze, canvas)
        self.name = "DepthFirst"
        self.generation_sets = []  # List of sets of tuples (int, int)
        self.init()

    def init(self) -> None:
        for i in range(self.maze.width):
            for j in range(self.maze.height):
                self.generation_sets.append({(i, j)})

    def create_maze(self) -> None:
        row_col = (random.randint(0, self.maze.height), random.randint(0, self.maze.width))
            
