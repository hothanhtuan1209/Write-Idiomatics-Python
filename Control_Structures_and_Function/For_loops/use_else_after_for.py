"""
- Use else to execute code after a for loop concludes.
- In example, I use else to execute code instead of if not after a for loop concludes
"""

# Harmful solution
# for user in get_all_users():
#     has_malformed_email_address = False
#     print("Checking {}".format(user))

#     for email_address in user.get_all_email_addresses():
#         if email_is_malformed(email_address):
#             has_malformed_email_address = True
#             print("Has a malformed email address!")
#             break

# if not has_malformed_email_address:
#     print("All email addresses are valid!")


# Idiomatic solution
for user in get_all_users():
    print("Checking {}".format(user))

for email_address in user.get_all_email_addresses():
    if email_is_malformed(email_address):
        print("Has a malformed email address!")
        break

else:  # this else matches the `for` loop, not the if!
    print("All email addresses are valid!")
