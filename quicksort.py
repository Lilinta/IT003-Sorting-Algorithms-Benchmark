from random import randint

def quicksort(A, l, r):
    if (l >= r):
        return
    pivot = randint(l, r)
    # A[l], A[pivot] = A[pivot], A[l]
    # pivot = l
    # for i in range(l+1, r+1):
    #     if A[i] <= A[pivot]:
    #         A[i], A[pivot] = A[pivot], A[i]
    #         pivot += 1
    A[l], A[pivot] = A[pivot], A[l]
    j = l+1
    for i in range(l+1, r+1):
        if (A[i] < A[l]):
            A[i], A[j] = A[j], A[i]
            j += 1
    A[l], A[j-1] = A[j-1], A[l]
    quicksort(A, l, j-2)
    quicksort(A, j, r)
    

if __name__ == "__main__":
    A = list(map(int, input().split()))
    n = len(A)
    quicksort(A, 0, n-1)
    for i in range(0, n):
        print(A[i], end=" ")