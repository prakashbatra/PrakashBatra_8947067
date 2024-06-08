import triangle

# integration tests
def test_is_valid_triangle_by_sides_and_angles():
    # Test case where sides and angles form a valid triangle
    angles = (37, 47, 96)
    sides = (3, 4, 5)
    assert (triangle.is_valid_triangle_by_angles(*angles)) == True
    assert (triangle.is_valid_triangle_by_sides(*sides)) == True

def test_valid_equilateral_triangle():
    # Test case where sides and angles form a valid equilateral triangle
    angles = (60, 60, 60)
    sides = (3, 4, 5)
    assert (triangle.is_valid_triangle_by_angles(*angles)) == True
    assert (triangle.is_valid_triangle_by_sides(*sides)) == True
    assert (triangle.is_equilateral(*sides)) == True