import MazeGenerator.CreationAlgo as MazeCreator
from Maze import Maze
import random
import Direction as maze_dir
from MazeDisplay.MazeCanvas import MazeCanvas

'''
Breadth first maze creation algorithm
'''


class DepthFirst(MazeCreator.CreationAlgo):
    def __init__(self, maze: Maze, canvas: MazeCanvas):
        super().__init__(maze, canvas)
        self.name = "DepthFirst"
        self.backtrack_stack = [] # a list of tuples (int, int) of coordinates for the backtracking

    def init(self) -> None:
        '''

        Initializes all the variables needed to (re)start the solving
        Returns: None

        '''
        self.backtrack_stack = []

    def create_maze(self, row_col=(0, 0)) -> None:
        row, col = row_col
        self.backtrack_stack.append(row_col)
        # Make current cell as visited
        while len(self.backtrack_stack):
            self.maze.get_cell(row, col).visited = True
            valid_moves = self.get_valid_moves(row, col)

            # Draw the cell onto the canvas
            self.canvas.render_maze(self.maze)
            if not len(valid_moves):
                if len(self.backtrack_stack):
                    row, col = self.backtrack_stack.pop()

            else:  # there are valid moves

                    # Add current cell to the stack
                    self.backtrack_stack.append((row, col))

                    # Choose random valid direction
                    valid_move = random.choice(valid_moves)
                    row1, col1, direction = valid_move

                    #print("RANDOMLY CHOSEN VALID MOVE: {}".format(valid_move))

                    # Knock down the walls between the two
                    # First knock down the randomly chosen wall
                    self.maze.get_cell(row, col).remove_wall(direction)

                    # Then get the opposite wall of the randomly chosen wall and knock the current cells wall down
                    opposite_direction = maze_dir.Direction.get_opposite_direction(direction)
                    #print("Opposite Direction: {}".format(opposite_direction))
                    self.maze.get_cell(row1, col1).remove_wall(opposite_direction)

                    # Call create_maze on newly chosen random move
                    row, col = row1, col1

    def get_valid_moves(self, row: int, col: int) -> [(int, int, maze_dir.Direction)]:
        """
        Given a x, y, and maze object get all the valid moves for that given coordinate
        Args:
            row (): Row coordinate in the maze
            col (): Column coordinate in the maze

        Returns: A list of (int, int) tuples that correspond to directions that the agent can traverse

        """
        valid_moves = []
        coordinates_to_check = [(row, col + 1, maze_dir.RightWall()), (row - 1, col,  maze_dir.TopWall()),
                                (row, col - 1, maze_dir.LeftWall()), (row + 1, col, maze_dir.BottomWall())]
        for coordinate in coordinates_to_check:
            row, col, _ = coordinate
            if self.maze.is_within_bounds(row, col) and not self.maze.is_visited(row, col):
                valid_moves.append(coordinate)
        return valid_moves
