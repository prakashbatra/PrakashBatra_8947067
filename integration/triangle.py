# Check if three angles form a valid triangle.
def is_valid_triangle_by_angles(a, b, c):
    # Parameters: a, b, c (int) in degrees

    # Check if the sum of angles is 180 degrees
    return (a + b + c) == 180


# Check if three sides form a valid triangle.
def is_valid_triangle_by_sides(x, y, z):
    # Parameters: x, y, z (int or float) for the sides in cm.

    # Check if the sum of any two sides is greater than the third side
    return (x + y > z) and (x + z > y) and (y + z > x)


# Check if triangle is equilateral
def is_equilateral(a, b, c):
    # Parameters: x, y, z (int or float) for the sides in cm.

    # Check if all sides are equal
    return a == b == c
