"""
- Use all capital letters when declaring global constant values.
- To distinguish constants defined at the module level (or global in a single
script) from imported names, use all uppercase letters.
"""


# Harmful solution
# seconds_in_a_day = 60 * 60 * 24


# def display_uptime(uptime_in_seconds):
#     """
#     Display the uptime percentage of a process within a day.

#     This function calculates and returns the uptime percentage of a process
#     within a day, based on the provided uptime in seconds.

#     Parameters:
#         uptime_in_seconds (int): The uptime of the process in seconds.

#     Returns:
#         str: A string indicating the uptime percentage.
#     """

#     percentage_run_time = (
#         uptime_in_seconds/seconds_in_a_day) * 100
#     # "Huh!? Where did seconds_in_a_day come from?"

#     return 'The process was up {percent} percent of the day'.format(
#         percent=int(percentage_run_time))


# uptime_in_seconds = 60 * 60 * 8
# uptime_percentage = display_uptime(uptime_in_seconds)
# print(uptime_percentage)


# Idiomatic solution
SECONDS_IN_A_DAY = 60 * 60 * 24


def display_uptime(uptime_in_seconds):
    """
    Display the uptime percentage of a process within a day.

    This function calculates and returns the uptime percentage of a process
    within a day, based on the provided uptime in seconds.

    Parameters:
        uptime_in_seconds (int): The uptime of the process in seconds.

    Returns:
        str: A string indicating the uptime percentage.
    """

    percentage_run_time = (
        uptime_in_seconds/SECONDS_IN_A_DAY) * 100
    # "Huh!? Where did seconds_in_a_day come from?"

    return 'The process was up {percent} percent of the day'.format(
        percent=int(percentage_run_time))


uptime_in_seconds = 60 * 60 * 8
uptime_percentage = display_uptime(uptime_in_seconds)
print(uptime_percentage)
