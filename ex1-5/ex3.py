class SquareGenerator:
    def squares_in_range(start, end):
        squares = [x*x for x in range(start, end+1)]
        return squares

print(SquareGenerator.squares_in_range(1,10))