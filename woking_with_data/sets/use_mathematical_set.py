"""
- Sets are a simple data structure similar to dictionaries without values.
- They are iterable and can be used with the in statement. Sets are rooted in mathematics and offer essential operations: union (A | B), intersection (A & B), difference (A - B), and symmetric difference (A ^ B).
- They are valuable for selecting elements shared among multiple sequences.
"""

# Harmful solution
# def get_both_popular_and_active_users():
# Assume the following two functions each return a
# list of user names
    # most_popular_users = get_list_of_most_popular_users()
    # most_active_users = get_list_of_most_active_users()
    # popular_and_active_users = []
    
    # for user in most_active_users:
    #     if user in most_popular_users:
    #         popular_and_active_users.append(user)
        
    # return popular_and_active_users


# Idiomatic solution
def get_both_popular_and_active_users():
    """
    Get a set of users who are both popular and active.

    Returns:
    set: A set containing user names that are both popular and active.
    """
    
    return(set(
        get_list_of_most_active_users()) & set(
            get_list_of_most_popular_users()))
