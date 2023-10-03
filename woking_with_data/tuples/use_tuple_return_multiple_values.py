"""
- Use a tuple to return multiple values from a function.
- This pattern is widely used in Python code and may not be immediately obvious to newcomers but greatly enhances code readability and functionality.
"""

from collections import Counter

# Harmful solution
# STATS_FORMAT = """Statistics:
# Mean: {mean}
# Median: {median}
# Mode: {mode}"""

# def calculate_mean(value_list):
#     return float(sum(value_list) / len(value_list))

# def calculate_median(value_list):
#     return value_list[int(len(value_list) / 2)]

# def calculate_mode(value_list):
#     return Counter(value_list).most_common(1)[0][0]

# values = [10, 20, 20, 30]
# mean = calculate_mean(values)
# median = calculate_median(values)
# mode = calculate_mode(values)
# print(STATS_FORMAT.format(mean=mean, median=median,
#     mode=mode))


# Idiomatic solution
STATS_FORMAT = """Statistics:
Mean: {mean}
Median: {median}
Mode: {mode}"""

def calculate_staistics(value_list):
    """
    Calculate statistics from a list of numerical values.

    Args:
        value_list (list): A list of numerical values.

    Returns:
        tuple: A tuple containing the mean, median, and mode of the input values.
    """

    mean = float(sum(value_list) / len(value_list))
    median = value_list[int(len(value_list) / 2)]
    mode = Counter(value_list).most_common(1)[0][0]
    
    return (mean, median, mode)

(mean, median, mode) = calculate_staistics([10, 20, 20, 30])
print(STATS_FORMAT.format(mean=mean, median=median, mode=mode))
