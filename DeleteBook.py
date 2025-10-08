import requests
from utilities.configurations import getconfig
from utilities.resources import *

config = getconfig()
url = config['API']['endpoint'] + ApiResources.deleteBook

response = requests.delete(url, json={
                                    "ID" : 'abc926242'
                                })

print(response.text)
json_response = response.json()

assert response.status_code == 200

assert "successfully" in json_response["msg"]