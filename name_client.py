import requests


out_data = {'name': 'Nikhita Gopisetty',
            'net_id': 'nrg21',
            'e-mail': 'nikhita.gopisetty@duke.edu'}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)
