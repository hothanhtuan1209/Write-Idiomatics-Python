"""
- Use collections.namedtuple to make tuple-heavy code more clear.
- Namedtuples in the collections module provide a convenient way to work with
structured data, enhancing code readability and maintainability.
"""

from collections import namedtuple

# Harmful solution
# Assume the 'employees' table has the following columns:
# first_name, last_name, department, manager, salary, hire_date
# def print_employee_information(db_connection):
#     db_cursor = db_connection.cursor()
#     results = db_cursor.execute('select * from employees').fetchall()
#     for row in results:
#     It's basically impossible to follow what's getting printed
#         print(row[1] + ', ' + row[0] + ' was hired '
#         'on ' + row[5] + ' (for $' + row[4] + ' per annum)'
#         ' into the ' + row[2] + ' department and reports to ' + row[3])


# Idiomatic solution
# Assume the 'employees' table has the following columns:
# first_name, last_name, department, manager, salary, hire_date

EmployeeRow = namedtuple('EmployeeRow',
                         ['first_name', 'last_name', 'department',
                          'manager', 'salary', 'hire_date'])


EMPLOYEE_INFO_FMT = '{last_name}, {first_name} was hired on \
e_date} (for ${salary} per annum) into the {department} \
rtment and reports to {manager}'


def print_employee_information(db_connection):
    """
    Prints employee information from a database connection.
    """

    db_cursor = db_connection.cursor()
    results = db_cursor.execute('select * from employees').fetchall()

    for row in results:
        employee = EmployeeRow._make(row)
        # It's now almost impossible to print a field in the wrong place
        print(EMPLOYEE_INFO_FMT.format(**employee._asdict()))
