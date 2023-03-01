import requests


r_id = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nrg21")
print(r_id.text)

r_type_rep = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M4")
print(r_type_rep.text)

r_type_don = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M5")
print(r_type_don.text)

if r_type_rep == r_type_don:
    answer = "Yes"
else:
    answer = "No"

out_data = {'Name': 'nrg21',
            'Match': answer}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=out_data)
print(r.status_code)
print(r.text)
