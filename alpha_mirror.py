"""
:type  param_1: {String}
:rtype: string
"""
def alpha_mirror(param_1):
    result = ""

    for mirror in param_1:
        if 'a' <= mirror <= 'z':
            # mirror lowercase letter
            result += chr(ord('z') - (ord(mirror) - ord('a')))
        elif 'A' <= mirror <= 'Z':
            # mirror uppercase letter
            result += chr(ord('Z') - (ord(mirror) - ord('A')))
        else:
            # non-letter characters stay the same
            result += mirror

    return result
