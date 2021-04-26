'''
Basic Cell data structure for maze
'''

import Direction as maze_dir
from Errors import InvalidDirectionError


class Cell:
    def __init__(self):
        # default, each cell's walls are up
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.visited = False

    def remove_wall(self, direction: maze_dir.Direction) -> None:
        """
        Given a direction, remove the wall in the corresponding direction
        Args:
            direction (): The direction to remove the cell wall

        Returns: None

        """
        if type(direction) == maze_dir.BottomWall:
            self.bottom_wall = False

        elif type(direction) == maze_dir.TopWall:
            self.top_wall = False

        elif type(direction) == maze_dir.LeftWall:
            self.left_wall = False

        elif type(direction) == maze_dir.RightWall:
            self.right_wall = False

        else:
            raise InvalidDirectionError

    def __str__(self) -> str:
        to_return = ""
        if self.top_wall:
            to_return += "--\n"
        else:
            to_return += "  \n"

        if self.left_wall:
            to_return += "| "
        else:
            to_return += "  "

        if self.right_wall:
            to_return += "|"

        else:
            to_return += "  "

        if self.bottom_wall:
            to_return += "\n--"
        else:
            to_return += "\n  "

        return to_return
