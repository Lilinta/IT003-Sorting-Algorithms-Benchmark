import numpy as np
from quicksort import quicksort
from heapsort import heapsort
from mergesort import mergesort
import time
import os

def validate(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            print("Wrong at index", i)
            print(A[i], A[i+1])
            return False
    return True

if __name__ == '__main__':
    for num in range(1, 11):
        print("Running test", num)
        with open(os.path.join(os.path.dirname(__file__), "testcases/test" + str(num) + ".txt"), "r") as f:
            if 1 <= num <= 5:
                inp = list(map(float, f.readline().split()))
            if 6 <= num <= 10:
                inp = list(map(int, f.readline().split()))
            A = np.array(inp.copy())
            start_time = time.perf_counter()
            A = quicksort(A)
            end_time = time.perf_counter()
            if not validate(A):
                print("Quicksort failed")
                exit(1)
            print("Quicksort took", round(end_time - start_time, 3), "seconds")
            A = np.array(inp.copy())
            start_time = time.perf_counter()
            mergesort(A, 0, len(A)-1)
            end_time = time.perf_counter()
            if not validate(A):
                print("Mergesort failed")
                exit(1)
            print("Mergesort took", round(end_time - start_time, 3), "seconds")
            A = np.array(inp.copy())
            start_time = time.perf_counter()
            heapsort(A)
            end_time = time.perf_counter()
            if not validate(A):
                print("Heapsort failed")
                exit(1)
            print("Heapsort took", round(end_time - start_time, 3), "seconds")
            A = np.array(inp.copy())
            start_time = time.perf_counter()
            np.sort(A)
            end_time = time.perf_counter()
            print("Numpy sort took", round(end_time - start_time, 3), "seconds")

"""
Running test 1
Quicksort took 3.885 seconds
Mergesort took 9.047 seconds
Heapsort took 27.127 seconds
Numpy sort took 0.026 seconds
Running test 2
Quicksort took 4.297 seconds
Mergesort took 9.078 seconds
Heapsort took 17.555 seconds
Numpy sort took 0.02 seconds
Running test 3
Quicksort took 5.203 seconds
Mergesort took 11.269 seconds
Heapsort took 17.842 seconds
Numpy sort took 0.023 seconds
Running test 4
Quicksort took 5.552 seconds
Mergesort took 11.441 seconds
Heapsort took 18.235 seconds
Numpy sort took 0.02 seconds
Running test 5
Quicksort took 5.482 seconds
Mergesort took 11.343 seconds
Heapsort took 17.705 seconds
Numpy sort took 0.025 seconds
Running test 6
Quicksort took 5.543 seconds
Mergesort took 11.82 seconds
Heapsort took 19.671 seconds
Numpy sort took 0.036 seconds
Running test 7
Quicksort took 5.907 seconds
Mergesort took 12.173 seconds
Heapsort took 18.652 seconds
Numpy sort took 0.035 seconds
Running test 8
Quicksort took 5.429 seconds
Mergesort took 12.429 seconds
Heapsort took 20.37 seconds
Numpy sort took 0.035 seconds
Running test 9
Quicksort took 5.641 seconds
Mergesort took 11.418 seconds
Heapsort took 20.113 seconds
Numpy sort took 0.022 seconds
Running test 10
Quicksort took 5.706 seconds
Mergesort took 12.308 seconds
Heapsort took 19.949 seconds
Numpy sort took 0.033 seconds
"""