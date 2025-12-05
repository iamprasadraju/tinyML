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

def DEBUG_PRINT(func):
	def enhanced_debug(*args):
		st = time.monotonic()
		func(*args)
		et = time.monotonic()
		t = et - st
		ops = N * N * N 	# calcute flop/s
		flops = ops / t
		GFLOPS = flops / 1e9   
		
		ops_format = RED + "GEMM"  + GREY + "_" + BLUE + str(N) + GREY + "_" + str(ops) + GREY + "_" + CYAN + "32" + RESET   
		flops_format = "     "  + YELLOW + f"{GFLOPS:.0f}" + RESET + " GFLOP/S" 
		time_format = "     "  + GREEN + f"{t:.3f}" + RESET + " SEC"
		if DEBUG == 1:
			print(ops_format, flops_format, time_format)
	return enhanced_debug	

	
def timeit(func):
	def enhanced_fuc(*args):
		st = time.monotonic()
		func(*args)
		et = time.monotonic()
		print(et - st)
	return enhanced_fuc