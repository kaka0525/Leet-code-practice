def compress_string(s):
    """
    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string a a b c c c c c a a a would
    become a2blc5a3. If the "compressed" string would not become smaller than
    the original string, your method should return the original string.
    """
    result = []
    count = 0
    last_char = ""
    for char in s:
        if char == last_char:
            count += 1
        else:
            if last_char != "":
                result.append(last_char + str(count))
            last_char = char
            count = 1
    result.append(last_char + str(count))
    result = ''.join(result)
    if len(result) < len(s):
        return result
    else:
        return s
