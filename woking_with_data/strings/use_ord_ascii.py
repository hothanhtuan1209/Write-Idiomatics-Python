"""
- Use ord to get the ASCII code of a character and chr to get the character from an ASCII code.
"""

# Harmful solution
# hash_value = 0
# character_hash = {
#     "a": 97,
#     "b": 98,
#     "c": 99,
#     # ...
#     "y": 121,
#     "z": 122,
# }

# for e in some_string:
#     hash_value += character_hash[e]


# Idiomatic solution
hash_value = 0

for e in some_string:
    hash_value += ord(e)
