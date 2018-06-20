#!/usr/bin/python3
def decodeStrings(s):
    """ Sorts letters in string s
    by the order they occur in string t
    Keyword arguments:
    s: string to sort
    t: string which letters sort string s
    """
    list_s = list(s)
    for idx, letter in enumerate(list_s):
        if letter == '[':
            list_s[idx] = '*('
        elif letter == ']':
            list_s[idx] = ')'
        elif letter.isdigit():
            list_s[idx] = '+' + letter
        elif letter != '[' and letter != '*(' and letter != ')':
            list_s[idx] = '"{}"'.format(letter)
    decoded = ''.join(list_s)
    return eval(decoded)
