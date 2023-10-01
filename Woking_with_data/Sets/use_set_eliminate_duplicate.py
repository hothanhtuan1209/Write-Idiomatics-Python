"""
- Use sets to eliminate duplicate entries from Iterable containers.
- Sets are a useful tool for removing duplicate values from lists or dictionaries, thanks to their unique and efficient characteristics.
- They can often be seamlessly integrated into existing code, making them a convenient choice for data manipulation.
"""

# Harmful solution
unique_surnames = []

for surname in employee_surnames:
    if surname not in unique_surnames:
        unique_surnames.append(surname)

def display(elements, output_format='html'):
    if output_format == 'std_out':
        for element in elements:
            print(element)

    elif output_format == 'html':
        as_html = '<ul>'
        for element in elements:
            as_html += '<li>{}</li>'.format(element)

        return as_html + '</ul>'

    else:
        raise RuntimeError('Unknown format {}'.format(output_format))


# Idiomatic solution
unique_surnames = set(employee_surnames)

def display(elements, output_format='html'):
    """
    Create a set of unique values from an iterable and display them in the specified format.

    Args:
        elements (iterable): The source of elements.
        output_format (str, optional): The format for displaying elements ('html' or 'std_out'). Default is 'html'.

    Returns:
        str or None: If 'output_format' is 'html', returns an HTML-formatted string; if 'output_format' is 'std_out', prints
        elements to the standard output; otherwise, raises a RuntimeError for an unknown format.
    """

    if output_format == 'std_out':
        for element in elements:
            print(element)

    elif output_format == 'html':
        as_html = '<ul>'
        for element in elements:
            as_html += '<li>{}</li>'.format(element)

        return as_html + '</ul>'

    else:
        raise RuntimeError('Unknown format {}'.format(output_format))

