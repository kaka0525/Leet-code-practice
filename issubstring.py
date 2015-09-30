def isSubstring(s1, s2):
    """
    Assume you have a method isSubstring which checks if one word is a
    substring of another. Given two strings, s i and s2, write code to
    check if s2 is a rotation of si using only one call to isSubstring
    (e.g.,"waterbottle"is a rota- tion of "erbottlewat").
    """
    if len(s1) != len(s2):
        return False
    else:
        return s2 in s1 * 2 and len(s1) == len(s2)
