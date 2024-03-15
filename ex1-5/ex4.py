import math

class SquareGenerator:
    def squares_in_range(start, end):
        squares = [math.pow(x,2) for x in range(start, end+1)]
        return squares

print(SquareGenerator.squares_in_range(1,10))