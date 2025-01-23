import json
import requests
from requests.auth import HTTPBasicAuth

class Test_Grafana:
    def test_print_teams(self):
        url = 'http://localhost:3000/'
        resources = 'api/teams/search'
        res = requests.get(url + resources, auth = HTTPBasicAuth('admin','admin'))
        res_json = res.json()
        print(json.dumps(res_json,indent=2))
