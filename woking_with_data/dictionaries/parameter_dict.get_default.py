"""
- Use the default parameter of dict.get to provide default values.
- Without using default (or the collections.defaultdict class), your code will be littered with confusing if statements.
"""

# Harmful solution
# log_severity = None

# if 'severity' in configuration:
#     log_severity = configuration['severity']
# else:
#     log_severity = 'Info'


# Idiomatic solution
log_severity = configuration.get('severity', 'Info')
