import math
from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self):
        pass

class CubicGenerator(SquareGenerator):
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def generate_squares(self):
        if self.start < self.end:
            squares = [math.pow(x,2) for x in range(self.start, self.end+1)]
            return squares
        else:
            return ValueError

    def squares_in_range(self) -> list:
        if self.start < self.end:
            squares = [math.pow(x,2) for x in range(self.start, self.end+1)]
            return squares
        else:
            return ValueError

    def cubes_in_range(self) -> list:
        if self.start > self.end:
            raise ValueError
        squares = [math.pow(x,3) for x in range(self.start, self.end+1)]
        return squares