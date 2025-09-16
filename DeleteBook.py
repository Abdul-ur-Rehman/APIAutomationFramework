import requests

import AddBook

response = requests.delete("http://216.10.245.166/Library/DeleteBook.php",
                           json={

                                    "ID" : AddBook.book_id
                                })

print(response.text)
json_response = response.json()

assert response.status_code == 200

assert "successfully" in json_response["msg"]