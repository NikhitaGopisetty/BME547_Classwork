import requests

server = "http://127.0.0.1:5000"

patient = {"id": 1, "name": "Nikhita", "blood_type": "O+"}
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)

patient = {"id": 2, "name": "John", "blood_type": "A+"}
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)

test = {"id": 1, "test_name": "HDL", "test_result": 150}
r = requests.post(server + "/add_test", json=test)
print(r.status_code)
print(r.text)

test = {"id": 1, "test_name": "LDL", "test_result": 100}
r = requests.post(server + "/add_test", json=test)
print(r.status_code)
print(r.text)
