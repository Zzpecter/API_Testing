import json
import yaml


def read_json(file):
    """
    Helper function for reading JSON files

    Parameters
    ----------
        file : str
            Path to the file to be read

    Returns
    ----------
        data : dict
            Dict-parsed data of the JSON file read
    """
    with open(file) as f:
        data = json.load(f)
    return data


def read_yaml(file):
    """
    Helper function for reading YAML files

    Parameters
    ----------
        file : str
            Path to the file to be read

    Returns
    ----------
        data : dict
            Dict-parsed data of the YAML file read
    """
    with open(file, 'r') as f:
        data = yaml.safe_load(f.read())
    return data
