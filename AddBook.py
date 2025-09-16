import requests
import payLoad
from utilities.configurations import getconfig
from utilities.resources import *

config = getconfig()
url = config['API']['endpoint'] + ApiResources.addBook

response = requests.post(url, json= payLoad.addBookPayload("abcd"))

print(response.text)

json_response = response.json()

book_id = json_response["ID"]
print(book_id)

assert response.status_code == 200
