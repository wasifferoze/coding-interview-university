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
        self.inc_size()
        self.A[self.n] = element  # set element at end
        self.n += 1  # increase length count

    def insert(self, index, element):
        """
        Add element at given index
        :param index: index of array
        :param element: value
        """
        self.inc_size()
        for i in range(self.n - 1, index, -1):
            # shift all element to right from given index
            self.A[i + 1] = self.A[i]
        # insert element at given index
        self.A[index] = element
        self.n += 1

    def prepend(self, element):
        """
        insert item at beginning of array
        :param element: item to insert
        """
        if self.is_empty():
            return IndexError('Array is empty! use append()')
        self.insert(0, element)

    def pop(self):
        """
        Remove last item in array
        """
        if self.is_empty():
            return IndexError("Array is empty")
        else:
            self.A[self.n] = self.A[self.n - 1]  # slicing last element
            self.n -= 1  # decreasing size count
            self.dec_size()

    def delete(self, index):
        """
        remove item in array at given index
        :param index:
        :return:
        """
        if self.is_empty():
            return IndexError("Array is empty! add some values")
        for i in range(index, self.n - 1, 1):
            self.A[i-1] = self.A[i] # TODO: have to complete this

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
        return self.n == 0

    def inc_size(self):
        """
        Increase capacity of array
        'double the capacity if size (n) equal to capacity'
        :return: resized array
        """
        if self.n == self.capacity:
            return self._resize(2 * self.capacity)  # double the size

    def dec_size(self):
        """
        Decrease the capacity of array
        'formula: if size n = capacity/4 then decrease capacity to half'
        :return: resize array
        """
        if self.n == int(self.capacity / 4):
            return self._resize(int(self.capacity / 2))  # reducing capacity of array
