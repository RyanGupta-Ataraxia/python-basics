# dictionary_functions.py
# Essential dictionary functions for Python Basics

def merge_dicts(dict1, dict2):
    """Merge two dictionaries into one. If keys overlap, dict2 overwrites dict1."""
    return {**dict1, **dict2}

def invert_dict(d):
    """Invert keys and values in a dictionary. Assumes values are unique and hashable."""
    return {v: k for k, v in d.items()}

def dict_keys_to_list(d):
    """Return all keys of a dictionary as a list."""
    return list(d.keys())

def dict_values_to_list(d):
    """Return all values of a dictionary as a list."""
    return list(d.values())
