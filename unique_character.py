def unique_characters(input):
    """
    Implement an algorithm to determine if a string has all unique characters.
    """
    s = set()
    for i in input:
        s.add(i)
    return len(s) == len(input)
