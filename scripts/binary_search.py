def binary_search(v, low, high, target):
    """
    Perform binary search on a sorted list `v`, looking for `target` within the range specified by `low` and `high` indices.
    
    Args:
    v (List[int]): A sorted list of integers.
    low (int): The lower index of the search range.
    high (int): The upper index of the search range.
    target (int): The integer value to search for in the list.
    
    Returns:
    int: The index of the target value if found, or -1 if not found.
    
    >>> binary_search([1, 3, 5, 7, 9], 0, 4, 5)
    2
    >>> binary_search([1, 3, 5, 7, 9], 0, 4, 6)
    -1
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 8, 6)
    5
    """
    while low <= high:
        mid = (low + high) // 2
        if target == v[mid]:
            return mid
        elif target < v[mid]:
            high = mid - 1
        elif target > v[mid]:
            low = mid + 1
    return -1
