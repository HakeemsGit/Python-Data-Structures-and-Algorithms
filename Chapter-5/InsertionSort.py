def insertion_sort(lst):
    """
    Sort a list of comparable
    elements into ascending order
    """
    for index in range(1, len(lst)):                                     # Iterate from 1 - (length - 1)
        current = lst[index]                                             # Current element to be inserted
        correct_index = index                                            # Find the correct index for the element
        while correct_index > 0 and lst[correct_index - 1] > current:
            lst[correct_index] = lst[correct_index - 1]
            correct_index -= 1
        lst[correct_index] = current                                     # Current is now in the proper index
