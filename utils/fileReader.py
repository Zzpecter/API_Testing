import json
import yaml


def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data


def read_yaml(file):
    with open(file, 'r') as f:
        data = yaml.safe_load(f.read())
    return data