from utilities.configurations import *


def addBookPayload(isbn):
    payLoad = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "926242",
        "author": "Abdul-ur-Rehman"
    }

    return payLoad


def buildPayloadFromDB(query):

    paylaod_data = {}
    query_results = getQuery(query)
    paylaod_data['name'] = query_results[0]
    paylaod_data['isbn'] = query_results[1]
    paylaod_data['aisle'] = query_results[2]
    paylaod_data['author'] = query_results[3]
    return paylaod_data
