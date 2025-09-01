import json
import requests

response = requests.post("http://216.10.245.166/Library/Addbook.php",
                         json={
                                "name":"Learn Appium Automation with Java",
                                "isbn": "abcd",
                                "aisle": "926242",
                                "author": "Abdul-ur-Rehman"})

print(response.text)

json_response = response.json()

book_id = json_response["ID"]
print(book_id)
