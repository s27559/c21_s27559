import square_generator

try:
    #square = square_generator.SquareGenerator(1,10)
    cubes = square_generator.CubicGenerator(1,5)
    #print(square.squares_in_range())
    #print(cubes.cubes_in_range())
    print(cubes.generate_squares())
except ValueError:
    print("Invalid range, start > end")