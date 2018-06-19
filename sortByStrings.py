#!/usr/bin/python3

def sortByStrings(s,t):
    """ Sorts letters in string s
    by the order they occur in string t
    
    Keyword arguments:
    s: string to sort
    t: string which letters sort string s
    """
    z = ""
    for letter in t:
        if letter in s:
            counter = s.count(letter)
            z += counter * letter
    return z
print(sortByStrings("weather","therapyw"))
