"""
:type  param_1: {String}
:type  param_2: {String}
:rtype: string
"""
def my_union(param_1, param_2):
    result = ""
    for char in param_1 + param_2:
        if char not in result:
            result += char
    return result

"""
Takes two input strings.

Combines them.

Removes any duplicate characters.

Returns a new string containing each unique character only once — in the order they first appear.
"""
