from dynamic_array import DynamicArray
# Instantiate
arr = DynamicArray()
print(arr.is_empty())

def array_print():
    if len(arr) != 0:
        print(arr.A[:])
    else:
        print("Array is empty")


print("capacity: {}".format(arr.capacity))
print("size: {}".format(len(arr)))

# Append new element
arr.append(1)
print("capacity: {}".format(arr.capacity))
print("size: {}".format(len(arr)))
print(arr.is_empty())
#array_print()

# Append new element
arr.append(2)
# Check length
print("capacity: {}".format(arr.capacity))
print("size: {}".format(len(arr)))
#array_print()

# Append new element
arr.append(5)
# Check length
print("capacity: {}".format(arr.capacity))
print("size: {}".format(len(arr)))
#array_print()

arr.append(7)
# Check length
print("capacity: {}".format(arr.capacity))
print("size: {}".format(len(arr)))
#array_print()

# insert at given index
arr.insert(3, 9)
print(arr.is_empty())
