import square_generator

try:
    square = square_generator.SquareGenerator(1,10)
    cubes = square_generator.CubicGenerator(1,5)
    print(square.squares_in_range())
    print(cubes.cubes_in_range())
    print(cubes.squares_in_range())
except ValueError:
    print("Invalid range, start > end")