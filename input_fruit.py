in_file = open("input_data.txt", "r")
fruits = in_file.readlines()
print(fruits)
in_file.close()
print(fruits)


in_file = open("input_data.txt", "r")
for line in in_file:
    print(line)


def analyze_ID(input_line):
    patient_data = first_line.strip("\n").split("=")
    patient_id = int(patient_data[1])
    return patient_id


def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    patient_id = analyze_ID(first_line)
    return patient_id


def test_read_file():
    from module import read-file
    filename = "input_file.txt"
    answer = read_file(filename)
    expected = 50
    assert == expected
