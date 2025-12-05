import time
import numpy as np
from debug.helpers import DEBUG, DEBUG_PRINT, N, timeit


@DEBUG_PRINT
def manymatmul(N):
    A = np.random.rand(N, N).astype(np.float32)
    B = np.random.rand(N, N).astype(np.float32)
    A @ B
    return N * N * N


if __name__ == "__main__":
	while True:
		manymatmul(N)