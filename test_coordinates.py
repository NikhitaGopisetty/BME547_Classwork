# test_coordinates.py
# Nikhita Gopisetty

def test_coordinates_function():
    from coordinates import coordinates_function
    # Arrange
    x1, y1 = 0, 0
    x2, y2 = 10, 10
    x = 5
    # Act
    answer = coordinates_function(x1, y1, x2, y2, x)
    # Assert
    assert answer == 5
