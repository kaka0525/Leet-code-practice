def shortest_word_distance(l, word1, word2):
    """
    Given a list of words and two words word1 and word2, return the shortest
    distance between these two words in the list.

    For example,
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Given word1 = "coding", word2 = "practice", return 3.
    Given word1 = "makes", word2 = "coding", return 1.

    Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are
    both in the list.
    """
    difference = []
    word1_idx = [i for i, j in enumerate(l) if j == word1]
    word2_idx = [i for i, j in enumerate(l) if j == word2]
    for i in word1_idx:
        for j in word2_idx:
            difference.append(abs(i - j))
    return min(difference)

shortest_word_distance(l=["practice", "makes", "perfect", "coding", "makes"],
                       word1="makes", word2="coding")
