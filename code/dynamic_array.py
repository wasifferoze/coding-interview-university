import ctypes


def make_array(capacity):
    """
    Returns a new array with given capacity
    """
    return (capacity * ctypes.py_object)()


class DynamicArray:
    """
    class for dynamic array like built-in List type in python
    """
    def __init__(self):
        self.n = 0  # count actual elements in array
        self.capacity = 1  # Default capacity is 1
        self.A = make_array(self.capacity)

    def __capacity__(self):
        """
        Return capacity of array
        """
        return self.capacity

    def __len__(self):
        """
        Return number of elements in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # check it k index is in bound of array
            return IndexError(k + ' is out of bound!')
        return self.A[k]  # Retrieve from array at index k

    def __getall__(self, k):
        """
        Return element at index k
        """
        if not self.is_empty():
            # TODO: implement how to get all elements of array
            return self.A[k]  # Retrieve from array at index k

    def append(self, element):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # double capacity if not enough room
            self._resize(2 * self.capacity)
        self.A[self.n] = element  # set element at end
        self.n += 1  # increase length count

    def insert(self, index, element):
        """
        Add element at given index
        :param index: index of array
        :param element: value
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # double the size
        for i in range(self.n-1, index, -1):
            # shift all element to right from given index
            self.A[i+1] = self.A[i]
        # insert element at given index
        self.A[index] = element
        self.n += 1

    def prepend(self, element):
        """
        insert item at beginning of array
        :param element: item to insert
        """
        if self.is_empty():
            return IndexError('Array is empty!')
        self.insert(0, element)

    def pop(self):
        """
        Remove last item in array
        """
        # TODO: implement pop

    def _resize(self, new_capacity):
        """
        Resize internal array to capacity given
        """
        b = make_array(new_capacity)  # new bigger array
        for k in range(self.n):  # reference all existing values
            b[k] = self.A[k]
        self.A = b
        self.capacity = new_capacity  # reset capacity

    def is_empty(self):
        """
        check array is empty
        :return: true or false
        """
        if self.n != 0:
            return False
        return True
