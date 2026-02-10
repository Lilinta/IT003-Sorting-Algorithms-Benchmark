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
Quicksort took 3.089530100005504 seconds
Mergesort took 4.865926799997396 seconds
Heapsort took 7.109875200003444 seconds
Numpy sort took 0.015571500000078231 seconds
Running test 2
Quicksort took 2.9903212999997777 seconds
Mergesort took 4.4625717000017175 seconds
Heapsort took 5.174157699999341 seconds
Numpy sort took 0.0371242000037455 seconds
Running test 3
Quicksort took 3.7411751999970875 seconds
Mergesort took 5.939994000000297 seconds
Heapsort took 7.471854700001131 seconds
Numpy sort took 0.025202300006640144 seconds
Running test 4
Quicksort took 3.731935900003009 seconds
Mergesort took 5.946441499996581 seconds
Heapsort took 7.31703550000384 seconds
Numpy sort took 0.023544200004835147 seconds
Running test 5
Quicksort took 4.023698600001808 seconds
Mergesort took 5.98753189999843 seconds
Heapsort took 7.004205400000501 seconds
Numpy sort took 0.025486499995167833 seconds
Running test 6
Quicksort took 4.038387499997043 seconds
Mergesort took 5.824063799998839 seconds
Heapsort took 7.713528200001747 seconds
Numpy sort took 0.023675399999774527 seconds
Running test 7
Quicksort took 3.860722800003714 seconds
Mergesort took 6.053898000005574 seconds
Heapsort took 6.344855399998778 seconds
Numpy sort took 0.02828890000091633 seconds
Running test 8
Quicksort took 3.4793460000000778 seconds
Mergesort took 5.553413800000271 seconds
Heapsort took 6.869034399998782 seconds
Numpy sort took 0.024497600003087427 seconds
Running test 9
Quicksort took 3.49267559999862 seconds
Mergesort took 5.903003300001728 seconds
Heapsort took 5.745460199999798 seconds
Numpy sort took 0.02659500000299886 seconds
Running test 10
Quicksort took 3.6237241000053473 seconds
Mergesort took 6.104747500001395 seconds
Heapsort took 7.311971499999345 seconds
Numpy sort took 0.03132729999924777 seconds
"""
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