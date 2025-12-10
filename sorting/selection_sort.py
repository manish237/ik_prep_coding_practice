def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    size = len(arr)
    for i in range(size):
        min = arr[i]
        min_index = i
        for j in range(i+1, size):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

inp = [5, 8, 3, 9, 4, 1, 7]
out = selection_sort(inp)
print(out)