#!/usr/bin/python3
"""define to_json_string function"""

import json


def to_json_string(my_obj):
    """returns json representation of an object"""
    return json.dumps(my_obj)
