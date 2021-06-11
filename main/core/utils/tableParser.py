"""
Python module for handling string parsed data tables.

Classes:

    TableParser

Functions:

    parse_to_dict(keys, values) -> dict

"""


class TableParser:
    """
    Table parser for string based data tables.
    """
    @staticmethod
    def parse_to_dict(keys, values):
        """
        parses the keys and values of a table to a dict.
        :param keys: list of keys
        :param values: list of values
        :return: dict: dictionary containing keys:values
        """
        body_dict = {}
        for k, v in zip(keys, values):
            if k == 'iteration_length':
                v = int(v)
            body_dict.update({k: v})
        return body_dict
