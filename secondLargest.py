def second_largest_number(l):
    """
    Find the second largest number in an array

    :type l: list
    :rtype: int
    """
    largest = l[0]
    second_largest = None
    for idx in xrange(1, len(l)):
        if l[idx] > largest:
            second_largest = largest
            largest = l[idx]
        elif l[idx] == largest:
            pass
        elif l[idx] > second_largest or second_largest is None:
            second_largest = l[idx]
    return second_largest
