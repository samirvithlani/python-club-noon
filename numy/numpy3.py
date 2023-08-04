import numpy as np

data = [1,2,3,4,5,6,7,8,9,10]

arr = np.array(data)
arr = np.reshape(arr,(2,5))
print(arr)

#arithmatic operations
arr = arr + 2
arr = arr - 2
arr = arr * 2
arr = arr / 2
print(arr)