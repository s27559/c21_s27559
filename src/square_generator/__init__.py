import math

def squares_in_range(start, end, ) -> list:
    if start > end:
        raise ValueError
    squares = [math.pow(x,2) for x in range(start, end+1)]
    return squares