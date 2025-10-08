import requests
from utilities.configurations import getconfig
from utilities.resources import *


def after_scenario(context, scenario):
    config = getconfig()
    url = config['API']['endpoint'] + ApiResources.deleteBook

    response = requests.delete(url, json={"ID": context.book_id})

    #print(response.text)
    json_response = response.json()

    assert response.status_code == 200

    assert "successfully" in json_response["msg"]