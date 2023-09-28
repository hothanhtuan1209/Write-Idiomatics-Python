"""
- Chain string functions to make a simple series of transformations more clear
- When applying a simple sequence of transformations on some datum, chaining the calls in a single expression is often more clear than creating a temporary variable for each step of the transformation.
- “No more than three chained functions” is a good rule of thumb.
"""

# Harmful solution
book_info = " The Three Musketeers: Alexandre Dumas"
formatted_book_info = book_info.strip()
formatted_book_info = formatted_book_info.upper()
formatted_book_info = formatted_book_info.replace(":", " by")


# Idiomatic solution
book_info = " The Three Musketeers: Alexandre Dumas"
formatted_book_info = book_info.strip().upper().replace(":", " by")
