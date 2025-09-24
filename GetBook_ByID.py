import json
import requests
from utilities.configurations import getconfig
from utilities.resources import *

config = getconfig()
url = config['API']['endpoint'] + ApiResources.getBook_ByID

response = requests.get(url,{"ID": "bnid3475"})

print(response.text)
print(type(response))
new_list = json.loads(response.text)
print(new_list)
print(type(new_list))
print(new_list[0]["author"])

print("************************")

json_response = response.json()
print(json_response)
print(type(json_response))
print(json_response[0]["author"])


print(response.headers)
assert response.status_code == 200