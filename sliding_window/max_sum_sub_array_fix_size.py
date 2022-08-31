def max_sub_array_of_size_k(k, arr):
    """
    Approach:
    -> Iterate through array till number of elem exceeds fix size window
    -> remove elem from start of window when window size exceeds fix size
    -> Adjust window start to right by 1
    :param k: fix size of the window
    :param arr: Input array
    :return: maximum sum possible out of input array with fix size
    """
    max_sum = 0
    sum_till_now = 0
    window_start = 0

    for index, num in enumerate(arr):
        sum_till_now += num

        if index >= k - 1:
            max_sum = max(max_sum, sum_till_now)
            sum_till_now -= arr[window_start]
            window_start += 1

    return max_sum
