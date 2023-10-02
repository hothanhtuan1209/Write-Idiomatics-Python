"""
- Avoid “swallowing” useful exceptions with bare except clauses.
- Programmers often make the mistake of overly relying on generic exception handling, especially when using third-party packages.
- This leads to a loss of crucial debugging information.
"""

import requests

# Harmful solution
# def get_json_response(url):
#     try:
#         r = requests.get(url)
#         return r.json()

#     except:
#         print("Oops, something went wrong!")

#     return None


# Idiomatic solution
def get_json_response(url):
    """Fetch JSON data from a given URL and return it as a Python object."""

    return requests.get(url).json()

# If we need to make note of the exception, we
# would write the function this way...

def alternate_get_json_response(url):
    """Fetch JSON data from a given URL, log any exceptions, and re-raise them."""

    try:
        r = requests.get(url)
        return r.json()

    except:
        # do some logging here, but don't handle the exception
        # ...
        raise
