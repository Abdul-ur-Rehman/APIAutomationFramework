import requests
import payLoad
from utilities.configurations import getconfig
from utilities.resources import *
import json


config = getconfig()
url = config['API']['endpoint'] + ApiResources.addBook

#ADD BOOK
response = requests.post(url, json= payLoad.addBookPayload("abcd"))

print(response.text)

json_response = response.json()

book_id = json_response["ID"]
print(book_id)

assert response.status_code == 200

#GET BOOK DETAILS BY ID
url2 = config['API']['endpoint'] + ApiResources.getBook_ByID

response = requests.get(url2,{"ID": book_id})

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

#DELETE BOOK
url3 = config['API']['endpoint'] + ApiResources.deleteBook

response = requests.delete(url3, json={
                                    "ID" : book_id
                                })

print(response.text)
json_response = response.json()

assert response.status_code == 200

assert "successfully" in json_response["msg"]
