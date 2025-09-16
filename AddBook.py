import requests
import payLoad
from utilities.configurations import getconfig

config = getconfig()


response = requests.post(config['API']['endpoint'] + "/Library/Addbook.php",
                         json= payLoad.addBookPayload("abcd"))

print(response.text)

json_response = response.json()

book_id = json_response["ID"]
print(book_id)

assert response.status_code == 200
