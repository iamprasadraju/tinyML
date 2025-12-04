import time
import numpy as np
from debug.helpers import DEBUG, DEBUG_PRINT, FLOPS, N

def manymatmul(N):
    A = np.random.rand(N, N).astype(np.float32)
    B = np.random.rand(N, N).astype(np.float32)
    A @ B
    return N * N * N

if __name__ == "__main__":
	while True:
		GFLOPS, elapsed = FLOPS(manymatmul, N)
		DEBUG_PRINT(GFLOPS, elapsed)
