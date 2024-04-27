import numpy as np
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
sum_axis_0 = np.sum(arr, axis=0)
product = np.prod(sum_axis_0)
print("Product : ",product)