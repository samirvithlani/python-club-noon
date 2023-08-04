import numpy as np

a =np.array([[1,4,2],[3,4,6],[0,-1,5]])
b =np.array([[1,4,2],[3,4,6],[0,-1,5]])
print(a)

#arr =np.sort(a,kind="heapsort")
arr =a.transpose()
print(arr)

x = a * b
print(x)
