import numpy as np
arr = np.array([[1,5,6],[4,7,2],[3,1,9]])

print(arr.max())
print(arr.min())
print(arr.sum())
print(arr.max(axis=0))
print(arr.max(axis=1))
print(arr.sum(axis=0))
print(arr.sum(axis=1))
