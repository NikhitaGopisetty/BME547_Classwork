import pytest
from pymodm import connect
from PatientModel import Patient
from secrets import mongodb_acct, mongodb_pswd

connect("mongodb+srv://{}:{}@bme547.leiggs8.mongodb.net/"
        "health_db?retryWrites=true&w=majority"
        .format(mongodb_acct, mongodb_pswd))


def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    patient_id = 234
    patient_name = "Test"
    blood_type = "O+"
    answer = add_patient_to_db(patient_id, patient_name, blood_type)
    x = Patient.objects.raw({"_id": patient_id}).first()
    x.delete()
    assert answer.patient_id == patient_id


def test_add_test_to_db():
    from health_db_server import add_test_to_db
    # Arrange
    patient_id = 123
    patient_name = 'Test'
    patient_blood_type = 'O+'
    from health_db_server import add_patient_to_db
    add_patient_to_db(patient_id, patient_name, patient_blood_type)
    test_name = 'HDL'
    test_value = 150
    # Act
    add_test_to_db(patient_id, test_name, test_value)
    # Assert
    x = Patient.objects.raw({"_id": patient_id}).first()
    answer = x.tests[-1]
    x.delete()
    assert answer == [test_name, test_value]
