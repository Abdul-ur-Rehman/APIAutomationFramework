import requests
import payLoad
from utilities.configurations import getconfig
from utilities.resources import *
from payLoad import *

config = getconfig()
url = config['API']['endpoint'] + ApiResources.addBook

query = 'SELECT * FROM books;'

response = requests.post(url, json= buildPayloadFromDB(query))

print(response.text)

json_response = response.json()

book_id = json_response["ID"]
print(book_id)

assert response.status_code == 200
