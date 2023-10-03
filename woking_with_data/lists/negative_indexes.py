"""
- Make use of negative indexes.
- Negative indices are perfectly acceptable. Rather than counting from the beginning of a list, negative indexes count backwards starting at the end of a list.
"""

# Harmful solution
# def get_suffix(word):
#     word_length = len(word)

#     return word[word_length - 2 :]


# Idiomatic solution
def get_suffix(word):
    return word[-2:]
