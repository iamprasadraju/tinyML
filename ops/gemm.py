#!/usr/bin/env  python3
import time
import numpy as np
#np.__config__.show()


N = 1024

A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)

"""
FLOP(Floating point operations)

For a Square Matrix

    - Flops per element 

        - Multiplication: n
        - Additions: n - 1

        Total Flops per element: n+(n-1) = 2n - 1

    Total elements = n^2

so, Total flops = n^2 * (2n - 1) = 2n^3

""" 

flop = 2*N*N*N
#print(f"{flop / 1e9:.2f} GFLOPS")

for _ in range(10):
    st = time.monotonic()
    C = A @ B
    et = time.monotonic()
    t = et - st
    print(f"{flop/t * 1e-12:.2f} TFLOPS")


