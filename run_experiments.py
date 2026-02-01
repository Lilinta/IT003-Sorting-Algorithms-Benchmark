import numpy as np
from quicksort import quicksort
from heapsort import heapsort
from mergesort import mergesort
import time
import os

def validate(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True

if __name__ == '__main__':
    for num in range(1, 11):
        print("Running test", num)
        with open(os.path.join(os.path.dirname(__file__), "testcases/test" + str(num) + ".txt"), "r") as f:
            if num == 1 or 3 <= num <= 6:
                inp = list(map(float, f.readline().split()))
            if num == 2 or 7 <= num <= 10:
                inp = list(map(int, f.readline().split()))
            A = inp.copy()
            start_time = time.perf_counter()
            quicksort(A, 0, len(A)-1)
            end_time = time.perf_counter()
            if not validate(A):
                print("Quicksort failed")
                exit(1)
            print("Quicksort took", end_time - start_time, "seconds")
            A = inp.copy()
            start_time = time.perf_counter()
            mergesort(A, 0, len(A)-1)
            end_time = time.perf_counter()
            if not validate(A):
                print("Mergesort failed")
                exit(1)
            print("Mergesort took", end_time - start_time, "seconds")
            A = inp.copy()
            start_time = time.perf_counter()
            heapsort(A)
            end_time = time.perf_counter()
            if not validate(A):
                print("Heapsort failed")
                exit(1)
            print("Heapsort took", end_time - start_time, "seconds")
            A = np.array(inp.copy())
            start_time = time.perf_counter()
            np.sort(A)
            end_time = time.perf_counter()
            print("Numpy sort took", end_time - start_time, "seconds")

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