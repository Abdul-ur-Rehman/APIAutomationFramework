import requests

import payLoad

response = requests.post("http://216.10.245.166/Library/Addbook.php",
                         json= payLoad.addBookPayload("abcd"))

print(response.text)

json_response = response.json()

book_id = json_response["ID"]
print(book_id)

assert response.status_code == 200
