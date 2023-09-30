"""
- Avoid using a temporary variable when performing a swap of two values.
- We can use tuples to make our intention more clear.
"""

# Harmful solution
# foo = "Foo"
# bar = "Bar"
# temp = foo
# foo = bar
# bar = temp


# Idiomatic solution
foo = "Foo"
bar = "Bar"
(foo, bar) = (bar, foo)
