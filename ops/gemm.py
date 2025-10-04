#!/usr/bin/env  python3
import time
import numpy as np
#np.__config__.show()


N = 1024

A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)


#FLOP
flop = 2*N*N*N
#print(f"{flop / 1e9:.2f} GFLOPS")

for _ in range(10):
    st = time.monotonic()
    C = A @ B
    et = time.monotonic()
    t = et - st
    print(f"{flop/t * 1e-12:.2f} TFLOPS")


