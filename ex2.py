def squares_in_range(start, end):
    squares = [x*x for x in range(start, end+1)]
    return squares

print(squares_in_range(1,10))