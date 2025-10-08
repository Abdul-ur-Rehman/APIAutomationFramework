import requests
from behave import *
from utilities.resources import *
from payLoad import *



@given('the book details which needs to be added to library')
def step_impl(context):
    config = getconfig()
    context.url = config['API']['endpoint'] + ApiResources.addBook
    query = 'SELECT * FROM books;'
    context.payload=buildPayloadFromDB(query)


@when('we execute the AddBook Post API method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload)

@then('book is successfully added')
def step_impl(context):
    json_response = context.response.json()

    context.book_id = json_response["ID"]
    print(context.book_id)

    assert context.response.status_code == 200
    assert json_response['Msg'] == 'successfully added'

@given('the hard coded book details which needs to be added to library')
def step_impl(context):
    config = getconfig()
    context.url = config['API']['endpoint'] + ApiResources.addBook
    context.payload = addBookPayload('abcd', '926242')

@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    config = getconfig()
    context.url = config['API']['endpoint'] + ApiResources.addBook
    context.payload = addBookPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):

    config = getconfig()
    context.session = requests.session()
    context.session.auth = auth = ('abdul-ur-rehman', getPassword())

    context.url = config['GitHub']['url']

@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.session.get(context.url)

@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.text)
    assert context.response.status_code == statusCode



