def replace_spaces(s):
    """
    Write a method to replace all spaces in a string with '%20'.
    You may assume that the string has sufficient space at the end of the
    string to hold the additional characters, and that you are given the
    "true" length of the string.
    """
    result = []
    for char in s:
        if char == " ":
            char = "%20"
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)
