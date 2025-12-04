import os
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
GREY = "\033[90m" 
RESET = "\033[0m"

# Read DEBUG environment variable once
DEBUG = int(os.environ.get("DEBUG", 0))
N = int(os.environ.get("N", 1024))

def DEBUG_PRINT(*args):
	ops = N * N * N
	ops_format = "GEMM"  + GREY + "_" + BLUE + str(N) + GREY + "_" + str(ops) + GREY + "_" + CYAN + "32" + RESET   
	flops = "     "  + YELLOW + f"{args[0]:.0f}" + RESET + " GFLOP/S" 
	time = "     "  + GREEN + f"{args[1]:.3f}" + RESET + " SEC"
	
	if DEBUG == 1:
		print(ops_format, flops, time)
        


def FLOPS(func, N):
	st = time.monotonic()
	ops = func(N)
	et = time.monotonic()
	
	t = et - st
	flops = ops / t
	
	GFLOPS = flops / 1e9
	return (GFLOPS, t)
	

	
	