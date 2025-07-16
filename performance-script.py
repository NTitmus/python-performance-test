import time
import pandas as pd
import psutil
import os
import sys

def memory_usage():
  return psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)
num1 = sys.argv[1]
#print(num1)
#print( "Pandas CSV Loading" )
start = time.time()
start_memory = memory_usage()
#print(f"start memory: {start_memory:.2f} MB")
df_pandas = pd.read_csv(num1)
end = time.time()
end_memory = memory_usage()
#print(f"Pandas: {end - start:.2f} sec, Memory: {memory_usage():.2f} MB" )
#print("******************")
print(f"{num1}, {end - start:.3f}, {end_memory - start_memory:.3f}")

