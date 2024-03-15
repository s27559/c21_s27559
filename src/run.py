import square_generator

try:
    print(square_generator.squares_in_range(1,10))
except ValueError:
    print("Invalid range, start > end")