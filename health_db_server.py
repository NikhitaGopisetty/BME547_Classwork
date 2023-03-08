from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "Tests": []}
    db[id] = new_patient
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data = request.get_json()
    # Call other functions to do the work
    answer = new_patient_driver(in_data)
    # Return a response
    return jsonify(answer)


def new_patient_driver(in_data):
    # Validate input
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    # Do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return an answer
    return "Patient successfully added", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


def get_patient_entry(db, id):
    patient = db.get(id)
    if patient is None:
        return False
    return patient


def add_test_to_db(db, id, test_name, test_result):
    patient = get_patient_entry(db, id)
    if patient is False:
        print("Bad entry")
    else:
        patient["Tests"].append([test_name, test_result])
    print(db)


@app.route("/add_test", methods=["POST"])
def post_add_test():
    # Get input data
    in_data = request.get_json()
    # Call other functions to do the work
    answer = add_test_driver(in_data)
    # Return a response
    return jsonify(answer)


def add_test_driver(in_data):
    # Validate input
    validation = validate_test_data(in_data)
    if validation is not True:
        return validation, 400
    # Do the work
    add_test_to_db(db, in_data["id"], in_data["test_name"], 
                   in_data["test_result"])
    # Return an answer
    return "Test successfully added", 200


def validate_test_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


if __name__ == '__main__':
    app.run()
