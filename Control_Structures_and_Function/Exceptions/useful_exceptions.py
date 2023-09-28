"""
- Avoid “swallowing” useful exceptions with bare except clauses.
- Programmers often make the mistake of overly relying on generic exception handling, especially when using third-party packages.
- This leads to a loss of crucial debugging information.
"""

# You shouldn't do like this
import requests


def get_json_response(url):
    try:
        r = requests.get(url)
        return r.json()

    except:
        print("Oops, something went wrong!")

    return None


# You should do like this
import requests


def get_json_response(url):
    return requests.get(url).json()


# If we need to make note of the exception, we
# would write the function this way...


def alternate_get_json_response(url):
    try:
        r = requests.get(url)
        return r.json()

    except:
        # do some logging here, but don't handle the exception
        # ...
        raise
