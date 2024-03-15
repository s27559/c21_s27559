import math

class SquareGenerator:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def squares_in_range(self) -> list:
        if self.start > self.end:
            raise ValueError
        squares = [math.pow(x,2) for x in range(self.start, self.end+1)]
        return squares

class CubicGenerator(SquareGenerator):
    def cubes_in_range(self) -> list:
        if self.start > self.end:
            raise ValueError
        squares = [math.pow(x,3) for x in range(self.start, self.end+1)]
        return squares