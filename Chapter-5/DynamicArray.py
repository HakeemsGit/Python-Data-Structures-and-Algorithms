import ctypes


class DynamicArray:
    """
    A dynamic array class that models
    a simplified version of Python's list.
    """

    def __init__(self):
        """
        Create an empty array.
        """
        self._size = 0                                                      # Count actual elements
        self._capacity = 1                                                  # Default array capacity
        self._array = self._make_array(self._capacity)                      # Create a low-level array

    def __len__(self):
        """
        Return the number of
        elements stores in the array.
        """
        return self._size

    def __getitem__(self, i):
        """
        Return element at index i.
        """
        if not 0 <= i < self._size:
            raise IndexError('Invalid index!')
        return self._array[i]                                               # Retrieve from the array

    def append(self, obj):
        """
        Add object to the end of the array.
        """
        if self._size == self._capacity:                                    # Not enough space to append
            self._resize(2 * self._capacity)                                # Double the capacity
        self._array[self._size] = obj
        self._size += 1

    def insert(self, value, i):
        """
        Insert a value at index i,
        shifting other values rightward.
        """
        if not 0 <= i < self._size:
            raise IndexError('Invalid index!')
        if self._size == self._capacity:                                    # If there is no room
            self._resize(2 * self._capacity)                                # Double the capacity
        for element in range(self._size, i, -1):                            # Shift elements rightward
            self._array[element] = self._array[element - 1]
        self._array[i] = value                                              # Store new element
        self._size += 1                                                     # Increment size

    def remove(self, value):
        """
        Remove the first occurrence of a value or
        raise a ValueError if it is not present.
        """
        for index in range(self._size):
            if self._array[index] == value:                                 # Found a match
                for new_index in range(index, self._size - 1):
                    self._array[new_index] = self._array[new_index + 1]     # Shift other elements
                self._array[self._size - 1] = None                          # Garbage collection
                self._size -= 1                                             # Decrement size
                return                                                      # Exit the loop
        raise ValueError("Value not found in Dynamic Array.")               # Raised if no element is found

    @staticmethod
    def _make_array(c):                                                     # Non-public utility function
        """
        Return new array with capacity c.
        """
        return (c * ctypes.py_object)()

    def _resize(self, c):                                                   # Non-public utility function
        """
        Resize internal array to capacity c.
        """
        new_array = self._make_array(c)                                     # Create a larger array
        for i in range(self._size):                                         # Add in all values of old array
            new_array[i] = self._array[i]
        self._array = new_array                                             # Set old array equal to the new array
        self._capacity = c

    def print_list(self):
        """
        Print the contents of this Dynamic
        Array in the form of a Python List
        """
        print([val for val in self])
