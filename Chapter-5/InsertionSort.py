# [5, 4, 3, 2, 1]
# [4, 5, 3, 2, 1]
# [3, 4, 5, 2, 1]
# [2, 3, 4, 5, 1]
# [1, 2, 3, 4, 5]
def insertion_sort(lst):
    """
    :param lst: A list of comparable Objects
    Sort the list into ascending order.
    Best case:  O(N)
    Worst case: O(N^2)
    """
    for k in range(1, len(lst)):                # iterate from 1 to n-1
        current = lst[k]                        # current element to be inserted
        j = k                                   # find correct index, j, for insertion
        while j > 0 and lst[j-1] > current:     # elements lst[j-1] must be after current element
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = current                        # assign current to the correct location
        print(lst)


insertion_sort([5, 4, 3, 2, 1])
