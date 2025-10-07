import requests
from behave import *
from utilities.resources import *
from payLoad import *

@given('the book details which needs to be added to library')
def stepImplementation(context):
    config = getconfig()
    context.url = config['API']['endpoint'] + ApiResources.addBook
    query = 'SELECT * FROM books;'
    context.payload=buildPayloadFromDB(query)


@when('we execute the AddBook Post API method')
def stepImplementation(context):
    context.response = requests.post(context.url, json=context.payload)

@then('book is successfully added')
def step_impl(context):
    json_response = context.response.json()

    book_id = json_response["ID"]
    print(book_id)
    print(context.response.text)

    assert context.response.status_code == 200
    assert json_response['Msg'] == 'successfully added'