def add_two_numbers(a, b):
    if type(a) is str:
        raise TypeError("Needs Integers")
    if type(b) is str:
        raise TypeError("Needs Integers")
    if a < 0 or b < 0:
        raise ValueError("No negative numbers")

    return a + b


if __name__ == "__main__":
    try:
        answer = add_two_numbers(2, 3)
        print(answer)
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')
    else:
        print("no error")
