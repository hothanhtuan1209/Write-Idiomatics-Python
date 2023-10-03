"""
- Always use self or a @classmethod when referring to a class's attributes.
- Given a Blog model class, the value of __tablename__ may be blog.
- If you need to refer to __tablename__ from within a Blog method, avoid writing Blog.__tablename__.
- Creating a 'table_name' method in the Blog class that returns 'Blog.tablename' causes it to always reference 'Blog' and return 'blog' for any derived class, which is not desired.
- Two ways to solve this issue depend on the method's context.
"""

# Harmful solution
# class Blog():
#     __tablename__ = 'blog'
    
#     def table_name(self):
#         return Blog.__tablename__

# class DerivedBlog(Blog):
#     __tablename__ = 'derived_blog'

# derivedBlog = DerivedBlog()
# print(derivedBlog.table_name()) # prints 'blog'


# Idiomatic solution
class Blog():
    """
    A class representing a blog.

    Attributes:
    __tablename__ (str): The name of the blog's table.
    """

    __tablename__ = 'blog'

    def table_name(self):
        """
        Get the table name for the current instance.

        Returns:
            str: The table name.
        """
        
        return self.__tablename__

    @classmethod
    def other_table_name(cls):
        """
        Get the table name for the class.

        Returns:
            str: The table name.
        """

        return cls.__tablename__

class DerivedBlog(Blog):
    """
    A class representing a derived blog, inheriting from Blog.

    Attributes:
    __tablename__ (str): The name of the derived blog's table.
    """

    __tablename__ = 'derived_blog'

derivedBlog = DerivedBlog()
print(derivedBlog.table_name()) # prints 'derived_blog'
