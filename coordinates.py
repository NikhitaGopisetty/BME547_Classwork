# coordinates.py
# Nikhita Gopisetty

def coordinates_function():
    x1, y1 = map(float, input("Enter the first coordinate (values separated by one space) 'x y': ").split())
    x2, y2 = map(float, input("Enter the first coordinate (values separated by one space) 'x y': ").split())
    x = float(input("Enter a new value on the x-coordinate of the above plane: "))
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    answer = m * x + b
    return answer

coordinates_function()