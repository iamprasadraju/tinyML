import numpy as np
import time

# W = [w1, w2, w3]
# b is a number
# x = [x1, x2, x3]


# N = 10000 size of array
n = 10000000

w = np.random.randn(n)
b = 4
x = np.random.randn(n)


# Without Vectorization
# ---------------------

# f(x) = w1x1 + w2x2 + w3x3 + b

"""
f = w[0] * x[0] + 
    w[1] * x[1] + 
    w[2] * x[2] + b
"""
start = time.monotonic_ns()
f = 0
for i in range(len(w) if len(w) == len(x) else exit("W and X have different sizes")):
    f = f + w[i] * x[i]
f = f + b  
end = time.monotonic_ns()
print(f"f(x) : {f} -> without Vectorization (N = {n}):  Executed in {(end - start) / 1e6} millisec")


# With Vectorization
# -------------------


# f(x) = W.X + b

start = time.monotonic_ns()
f = np.dot(w, x) + b #.dot() func works on vectorization using simd intructions -> parallel computing (avx and fma instruction sets)
end = time.monotonic_ns()

print(f"f(x) : {f} -> with Vectorization (N = {n}):  Executed in {(end - start) / 1e6} millisec")






