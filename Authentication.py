import requests
from utilities.configurations import *

session = requests.session()
session.auth = auth=('abdul-ur-rehman', getPassword())

url = "https://api.github.com/user/repos"
github_response = session.get(url)

print(github_response.text)