#!/usr/bin/env python
import numpy as np
import time
import matplotlib.pyplot as plt

# Numpy implementation
def numpy_speedtest():
    for i in range(1, 100):
        rows = i
        cols = i
        # matrix multiplication using numpy
        A = np.random.rand(rows, cols)
        B = np.random.rand(rows, cols)

        initial_time = time.perf_counter()

        AB = np.dot(A, B)

        final_time = time.perf_counter()

        yield (final_time - initial_time)


# for loop implementation
def for_speedtest():
    for i in range(1, 100):
        rows = i
        cols = i

        C = np.random.randint(0, 10, size = (rows, cols))

        D = np.random.randint(0, 10, size = (rows, cols))

        CD = np.zeros((C.shape[0], D.shape[1]), dtype=int)


        intial_time = time.perf_counter()

        for i in range(C.shape[0]):
            for j in range(D.shape[1]):
                for k in range(C.shape[1]):
                    CD[i][j] += C[i][k] * D[k][j]

        final_time = time.perf_counter()

        yield (final_time - intial_time)

size = 1
for i, j in zip(for_speedtest(), numpy_speedtest()):
    print(f"Time taken for shape({size},{size}) Matmul : using for loop {i:.5f} - using numpy {j:.5f}")
    size += 1
