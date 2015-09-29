def permutation_strings(input, input_two):
    """
    Given two strings, write a method to decide if one is a permutation of
    the other
    """
    if len(input) != len(input_two):
        return False
    else:
        return sorted(input) == sorted(input_two)
