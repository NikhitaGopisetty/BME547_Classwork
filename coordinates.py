# coordinates.py
# Nikhita Gopisetty

def input_function():
    x1, y1 = map(float, input("Enter the first coordinate 'x y': ").split())
    x2, y2 = map(float, input("Enter the first coordinate 'x y': ").split())
    x = float(input("Enter a new value on the x-coordinate of the  plane: "))
    return x1, y1, x2, y2, x


def coordinates_function(x1, y1, x2, y2, x):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    answer = m * x + b
    return answer


if __name__ == '__main__':
    x1, y1, x2, y2, x = input_function()
    coordinates_function(x1, y1, x2, y2, x)
