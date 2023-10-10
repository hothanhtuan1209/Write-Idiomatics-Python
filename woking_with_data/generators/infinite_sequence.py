"""
- Use a generator to lazily load infinite sequences.
- Generators are valuable in scenarios with infinite sequences or costly
calculations, as they provide a way to iterate without precomputing.
- They're special coroutines that yield iterables and save their state for
efficient continuation.
"""

# Harmful solution
# def get_twitter_stream_for_keyword(keyword):
#     """Get's the 'live stream', but only at the moment
#     the function is initially called. To get more entries,
#     the client code needs to keep calling
#     'get_twitter_livestream_for_user'. Not ideal.
#     """

#     imaginary_twitter_api = ImaginaryTwitterAPI()
#     if imaginary_twitter_api.can_get_stream_data(keyword):
#         return imaginary_twitter_api.get_stream(keyword)

# current_stream = get_twitter_stream_for_keyword('#jeffknupp')
# for tweet in current_stream:
#     process_tweet(tweet)


# Uh, I want to keep showing tweets until the program is quit.
# What do I do now? Just keep calling
# get_twitter_stream_for_keyword? That seems stupid.

# def get_list_of_incredibly_complex_calculation_results(data):
#     return [first_incredibly_long_calculation(data),
#             second_incredibly_long_calculation(data),
#             third_incredibly_long_calculation(data),
#             ]


# Idiomatic solution
class ImaginaryTwitterAPI:
    def can_get_stream_data(self, keyword):
        pass

    def get_stream(self, keyword):
        pass


def process_tweet(tweet):
    pass


def get_twitter_stream_for_keyword(keyword):
    imaginary_twitter_api = ImaginaryTwitterAPI()
    while imaginary_twitter_api.can_get_stream_data(keyword):
        yield imaginary_twitter_api.get_stream(keyword)


got_stop_signal = False


def first_incredibly_long_calculation(data):
    pass


def second_incredibly_long_calculation(data):
    pass


def third_incredibly_long_calculation(data):
    pass


# Because it's a generator, I can sit in this loop until
# the client wants to break out

for tweet in get_twitter_stream_for_keyword('#jeffknupp'):
    if got_stop_signal:
        break
    process_tweet(tweet)


def get_list_of_incredibly_complex_calculation_results(data):
    """A simple example to be sure, but now when the client
    code iterates over the call to
    'get_list_of_incredibly_complex_calculation_results',
    we only do as much work as necessary to generate the
    current item.
    """

    yield first_incredibly_long_calculation(data)
    yield second_incredibly_long_calculation(data)
    yield third_incredibly_long_calculation(data)
