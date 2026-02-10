import numpy as np
from random import randint

def quicksort(A):
    if (len(A) <= 1):
        return A
    B = []
    C = []
    D = []
    pivot = randint(0, len(A)-1)
    for i in range(0, len(A)):
        if A[i] < A[pivot]:
            B.append(A[i])
        elif A[i] == A[pivot]:
            C.append(A[i])
        else:
            D.append(A[i])
    return quicksort(B) + C + quicksort(D)


if __name__ == "__main__":
    A = np.array(list(map(int, input().split())))
    A = quicksort(A)
    for i in range(0, len(A)):
        print(A[i], end=" ")