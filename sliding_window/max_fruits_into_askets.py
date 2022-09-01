def fruits_into_baskets(fruits):
    """
    Approach:
    -> Create dictionary of fruit type
    -> Iterate till we have at max two type of fruit in sequence(since we have two basket which can contain a type of
      fruit each.
    -> Decrease counter of fruit type of first fruit from the window when it exceeds limit 2
    -> Delete fruit type from dictionary if frequency becomes 0 after decrement in last step
    -> Increase window start by 1 when distinct fruit type exceeds 2
    :param fruits: Input fruit type trees
    :return: maximum fruits in sequence that can be picked in two baskets
    """
    window_start = 0
    max_fruits = 0
    fruit_type_map = dict()

    for index, f in enumerate(fruits):
        if f in fruit_type_map:
            fruit_type_map[f] += 1
        else:
            fruit_type_map[f] = 1

        if len(fruit_type_map) > 2 and fruit_type_map[fruits[window_start]] == 1:
            del fruit_type_map[fruits[window_start]]
            window_start += 1
        elif len(fruit_type_map) > 2:
            fruit_type_map[fruits[window_start]] -= 1
            window_start += 1

        max_fruits = max(max_fruits, (index - window_start + 1))

    return max_fruits
