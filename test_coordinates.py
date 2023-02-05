# test_coordinates.py
# Nikhita Gopisetty

def test_coordinates_function():
    from coordinates import coordinates_function
    # Arrange
    coord_1 = (0, 0)
    coord_2 = (10, 10)
    x = 5
    # Act
    answer = coordinates_function(coord_1, coord_2, x)
    # Assert
    assert answer == 5