"""
This is where we do excpetions
"""


class Error(Exception):
    """
    Making a base exception type for your module is a good idea
    """
    pass


class FileError(Error):
    """
    All more specialist exceptions inherit from base class
    """
    pass


class FileFormatError(FileError):
    """
    All more specialist exceptions inherit from base class or a more generic error
    """
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def divide_exception_handling(x, y):
    """
    Example handling a built in exceptions
    """
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def custom_exceptions_handling_part1():
    """
    Now we handle custom exceptions
    """
    for cls in [Error, FileError, FileFormatError]:
        try:
            raise cls()
        except FileFormatError:
            print("FileFormatError")
        except FileError:
            print("FileError")
        except Error:
            print("Error")


def custom_exceptions_handling_part2():
    """
    Now we handle base exceptions
    """
    for cls in [Error, FileError, FileFormatError]:
        try:
            raise cls()
        except Error:
            print("Error")


def why_we_want_to_use_with():
    """
    The problem with this code is that it leaves the file open for an
    indeterminate amount of time after this part of the code has finished
    executing. This is not an issue in simple scripts, but can be a problem for
    larger applications.

    The with statement allows objects like files to be used in a way that ensures
    they are always cleaned up promptly and correctly.
    """
    # not so nice code
    for line in open("myfile.txt"):
        print(line)

    # nicer code uses 'with'
    with open("myfile.txt") as f:
        for line in f:
            print(line)
