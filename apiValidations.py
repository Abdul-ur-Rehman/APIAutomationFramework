import json

import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php",
                       {"ID": "abcd926242"})
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
print(response.links)
assert response.status_code == 200