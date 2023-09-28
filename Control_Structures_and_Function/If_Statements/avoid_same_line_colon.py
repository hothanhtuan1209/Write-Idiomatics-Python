"""
- Avoid placing conditional branch code on the same line as the colon.
- Using indentation to indicate scope
- if, elif, and else statements should always be on their own line. No code should follow the :.
"""

# Harmful solution
name = "Jeff"
address = "New York, NY"

if name:
    print(name)
print(address)


# Idiomatic solution
name = "Jeff"
address = "New York, NY"

if name:
    print(name)
print(address)
