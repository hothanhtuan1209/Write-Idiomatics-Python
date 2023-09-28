"""
- Prefer raising a user-defined Exception to core Python Exceptions
- You shouldn't use core Python Exceptions, like RuntimeError, as generic catch-all exceptions in code.
- It can make it challenging to identify specific errors and their origins, leading to confusion for users.
- The recommendation is to define and use custom Exceptions for better error handling and clarity in code.
"""

# You shouldn't do like this
import requests

def fetch_url_contents(url):
    response = requests.get(url)
    print(response.status_code)
    
    if response.status_code != 200:
        raise RuntimeError('Unable to fetch contents. Received status code {}'.format(response.status_code))

    return response.content

# You should do like this
import requests

class URLFetchError(Exception):
    pass

def fetch_url_contents(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        raise URLFetchError(
            'Unable to fetch contents. Received status code {}'.format(
        response.status_code))

    return response.content
