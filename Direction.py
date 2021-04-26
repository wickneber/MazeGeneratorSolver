
from Errors import InvalidDirectionError

'''
Direction classes that are used for the Maze logic
'''


class Direction:
    def __init__(self):
        pass

    @staticmethod
    def get_opposite_direction(direction):
        """
        Gets the opposite direction of the given direction
        Args:
            direction (): The direction object of which to get the opposite of

        Returns: The opposite direction

        """
        print("GIVEN DIRECTION {}".format(direction))
        print(type(direction) == LeftWall)
        if type(direction) == TopWall:
            return BottomWall()

        elif type(direction) == BottomWall:
            return TopWall()

        elif type(direction) == RightWall:
            return LeftWall()

        elif type(direction) == LeftWall:
            return RightWall()

        else:
            raise InvalidDirectionError



class LeftWall(Direction):
    def __init__(self):
        super().__init__()


class RightWall(Direction):
    def __init__(self):
        super().__init__()


class TopWall(Direction):
    def __init__(self):
        super().__init__()


class BottomWall(Direction):
    def __init__(self):
        super().__init__()