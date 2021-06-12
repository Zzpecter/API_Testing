"""
Python module for handling everything related to regular expressions.

Classes:

    RegularExpressionHandler

Functions:

    replace_tag(pattern, base_string, replace_string) -> string

"""
import re


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
        return re.sub(pattern, str(replace_string), str(base_string))

    @staticmethod
    def replace_tag_old(pattern, base_string, replace_string):
        """
        Deprecated, old method for replacing a pattern in the string.

        :param pattern: the pattern that is going to be replaced from the
        string.
        :param base_string: the original string sent to the function
        :param replace_string: the string which should be inserted if the
        replacement pattern is found
        :return: string: the updated string.
        """
        return base_string.replace(pattern, replace_string)

    @staticmethod
    def search_text_between_tags(text):
        """
        Method for searching and extracting text between tags from an input.

        :param text: input text for searching
        :return: list: all the text between tags '<>'
        """
        return re.findall("<(.*?)>", text, re.DOTALL)


    @staticmethod
    def search_text_between_slashes(text):
        """
        Method for searching and extracting text between slashes from an input.
        Used for getting the endpoints from an url

        :param text: input text for searching
        :return: list: all the text between tags '<>'
        """
        return re.findall("/(.*?)/", text, re.DOTALL)
