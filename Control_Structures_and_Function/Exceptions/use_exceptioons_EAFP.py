"""
- Use Exceptions to write code in an “EAFP” style
- Two programming styles: "Look Before You Leap (LBYL)," which involves extensive pre-condition checks. 
- And "Easier to Ask for Forgiveness than Permission (EAFP)," which focuses on catching exceptions when things go wrong, emphasizing code clarity and efficiency.
"""

# You shouldn't do like this
def get_log_level(config_dict):
    if 'ENABLE_LOGGING' in config_dict:
        if config_dict['ENABLE_LOGGING'] != True:
            return None
        elif not 'DEFAULT_LOG_LEVEL' in config_dict:
            return None
        else:
            return config_dict['DEFAULT_LOG_LEVEL']

    else:
        return None

# You should do like this
def get_log_level(config_dict):
    try:
        if config_dict['ENABLE_LOGGING']:
            return config_dict['DEFAULT_LOG_LEVEL']

    except KeyError:
    # if either value wasn't present, a
    # KeyError will be raised, so
    # return None
        return None
