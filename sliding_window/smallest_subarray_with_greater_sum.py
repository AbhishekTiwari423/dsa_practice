def smallest_subarray_sum(s, arr):
    """
    Approach:
    -> Create window sum, check if exceeds the target sum
    -> if it exceeds the target, start shifting the window to the right till it is greater or equal to target
    -> track and return the minimum length window
    :param s: target sum
    :param arr: Input array
    :return: min window size having equal or greater summation value than target
    """
    window_sum = []
    window_start = 0
    min_len = 1000000
    for index, num in enumerate(arr):
        window_sum.append(num)

        while sum(window_sum) >= s:
            min_len = min(min_len, len(window_sum))
            window_sum.remove(arr[window_start])
            window_start += 1

    return min_len
