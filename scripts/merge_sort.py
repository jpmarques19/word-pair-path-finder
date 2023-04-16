def merge_sort(vector):
    """
    Perform merge sort on a list `vector`.
    
    Args:
    vector (List[int]): A list of integers.
    
    Returns:
    List[int]: The sorted list of integers.
    
    >>> merge_sort([3, 2, 5, 1, 7])
    [1, 2, 3, 5, 7]
    >>> merge_sort([9, 4, 8, 2, 6])
    [2, 4, 6, 8, 9]
    """
    mid = len(vector) // 2

    if len(vector) <= 1:
        return vector

    left_half = merge_sort(vector[:mid])
    right_half = merge_sort(vector[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """
    Merge two sorted lists `left` and `right` into a single sorted list.
    
    Args:
    left (List[int]): A sorted list of integers.
    right (List[int]): A sorted list of integers.
    
    Returns:
    List[int]: The merged sorted list of integers.
    """
    s = [0 for i in range(len(left)+len(right))]
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s[k] = left[i]
            i += 1
        else:
            s[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        s[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        s[k] = right[j]
        j += 1
        k += 1

    return s
