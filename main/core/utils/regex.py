import re
"""
Python module for handling everything related to regular expressions.

Classes:

    RegularExpressionHandler

Functions:

    replace_tag(pattern, base_string, replace_string) -> string

"""


class RegularExpressionHandler:
    """
    Regular expression handler is a static class for manipulating strings
    based on RE's
    """
    @staticmethod
    def replace_tag(pattern, base_string, replace_string):
        """

        :param pattern: the pattern that is going to be replaced from the
        string.
        :param base_string: the original string sent to the function
        :param replace_string: the string which should be inserted if the
        replacement pattern is found
        :return: string: the updated string.
        """
        # TODO: why is the RE replacing the whole string?
        # return re.sub(pattern, base_string, replace_string)
        return base_string.replace(pattern, replace_string)
