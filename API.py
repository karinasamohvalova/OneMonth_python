"""
This program allows you to find some information about some book
using Knowledge Graph Search API from Google

The original code from google contains errors because its imported urllib
that don't includes methods parse and request, required for new lib version,
so I corrected code from google :)))
"""
# Key AIzaSyBKAzQ8udli9FP1huI6NZAAUIYv5PmEVOA

from __future__ import print_function
import json
import urllib.parse
import urllib.request


def book_info():
    # assigning var for query
    book_name = input("Please enter the name of some book: ")
    # The key for API, https://console.developers.google.com/apis/credentials
    api_key = 'AIzaSyBKAzQ8udli9FP1huI6NZAAUIYv5PmEVOA'
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': book_name,  # the body of query in var book_name
        'types': 'Book',  # we take types from schema.org
        'limit': 1,  # defining amount of results from search
        'indent': True,
        'key': api_key,
    }
    # forming url for query to API
    url = service_url + '?' + urllib.parse.urlencode(params)
    # reading json in API answer
    response = json.loads(urllib.request.urlopen(url).read())

    # escaping problems with None results in diff. fields of response
    try:
        # decompose response from API
        for element in response['itemListElement']:
            # structuring results for user
            print(element['result']['name'] + ', some info: ' +
                  element['result']['description'])
            print('Details:')
            print(element['result']['detailedDescription']['articleBody'])
    # catching errors
    except Exception:
        print("Sorry, there is no additional info, or something gone wrong")
    # looping
    finally:
        again_book_name()


# defining func for looping
def again_book_name():
    continue_status = input('Do you want to search other book? YES or NO: ')
    if 'y' in continue_status.lower():
        book_info()
    elif 'n' in continue_status.lower():
        print("See you later, books' aligator'")


book_info()
