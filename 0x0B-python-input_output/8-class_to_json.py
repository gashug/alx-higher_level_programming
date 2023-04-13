#!/usr/bin/python3
"""returns the dict description for JSON serialization of object"""


def class_to_json(obj):
    """
    Convert an object to a dictionary representation with simple
    data structures for JSON serialization.

    Args:
        obj: Instance of a Class

    Returns:
        dict: Dictionary representation of the object
    """

    if isinstance(obj, dict) or isinstance(obj, list):
        return obj

    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj

    if hasattr(obj, '__dict__'):
        obj_dict = obj.__dict__

        ser_dict = {key: value for key, value in obj_dict.items()
                    if isinstance(value, (list, dict, str, int, bool))}

        return ser_dict

    else:
        raise TypeError("Object is not serializable to JSON")
