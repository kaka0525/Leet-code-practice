def stock(input):
    """
     You have an array of stock prices. i-th element in that array represents
     the stock price of that day. Find the maximum profit
    """
    input_len = len(input)
    if (input_len < 2):
        return 0
    else:
        highest_rev = 0
        current_idx = 0
        next_idx = 0
        for next_idx in xrange(input_len):
            highest_rev = max(highest_rev, input[next_idx] - input[current_idx])
            if input[next_idx] < input[current_idx]:
                current_idx = next_idx
        return highest_rev
