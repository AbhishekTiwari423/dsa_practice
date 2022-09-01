def non_repeat_substring(str):
    """
    Approach:
    -> keep iterating till we get repeated char
    -> reset window start when char is repeated
    -> keep track of max sub string
    :param str: Input string
    :return: Maximum length substring without any repeated chars
    """
    window_start = 0
    char_frequency = dict()
    max_len_substr = 0

    for index, char in enumerate(str):
        if char not in char_frequency:
            char_frequency[char] = 1
            max_len_substr = max(max_len_substr, index - window_start + 1)
        else:
            max_len_substr = max(max_len_substr, index - window_start)
            window_start = index

    return max_len_substr
