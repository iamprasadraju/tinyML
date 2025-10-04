import time
import numpy as np


N = 1000


A = np.random.rand(N, N)
B = np.random.rand(N, N)

if A.shape[1] == B.shape[0]:
	C = np.zeros((A.shape[0], B.shape[1]))
	for i in range(A.shape[0]):
		for j in range(B.shape[1]):
			c = 0.0
			for k in range(A.shape[1]):
				c += A[i][k] * B[k][j]
			C[i][j] = c
else:
	raise ValueError("Please check the matrices")