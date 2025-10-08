import requests
from utilities.configurations import *

session = requests.session()
session.auth = auth=('abdul-ur-rehman', getPassword())

config = getconfig()

#url = "https://api.github.com/user/repos"
url = config['GitHub']['url']
github_response = session.get(url)

print(github_response.text)
print(github_response.status_code)