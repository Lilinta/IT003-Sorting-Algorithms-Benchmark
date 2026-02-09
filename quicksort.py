import numpy as np
from random import randint

def quicksort(A, l, r):
    if l >= r:
        return
    pivot = randint(l, r)
    A[l], A[pivot] = A[pivot], A[l]
    j = l+1
    for i in range(l+1, r+1):
        if A[i] < A[l]:
            A[i], A[j] = A[j], A[i]
            j += 1
    A[l], A[j-1] = A[j-1], A[l]
    quicksort(A, l, j-2)
    while j <= r and A[j] == A[j - 1]:
        j += 1
    quicksort(A, j, r)
    

if __name__ == "__main__":
    A = np.array(list(map(int, input().split())))
    quicksort(A, 0, len(A)-1)
    for i in range(0, len(A)):
        print(A[i], end=" ")