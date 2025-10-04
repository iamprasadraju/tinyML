import time
import numpy as np


N = 100


A = np.random.rand(N, N)
B = np.random.rand(N, N)

C = np.zeros((A.shape[0], B.shape[1]))
for i in range(A.shape[0]):
	for j in range(B.shape[1]):
		c = 0.0
		for k in range(A.shape[1]):
			c += A[i][k] * B[k][j]
		C[i][j] = c
