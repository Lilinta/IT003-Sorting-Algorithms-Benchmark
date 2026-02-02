import numpy as np

def heapsort(A):
    for i in range(1, len(A)):
        curr = i
        parent = (curr-1)//2
        while curr > 0 and A[curr] > A[parent]:
            A[curr], A[parent] = A[parent], A[curr]
            curr = parent
            parent = (curr-1)//2
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        curr = 0
        while True:
            left = 2*curr + 1
            right = 2*curr + 2
            if (left >= i or A[left] <= A[curr]) and (right >= i or A[right] <= A[curr]): break
            if right >= i or A[left] >= A[right]:
                A[curr], A[left] = A[left], A[curr]
                curr = left
            else:
                A[curr], A[right] = A[right], A[curr]
                curr = right

if __name__ == '__main__':
    A = list(map(int, input().split()))
    heapsort(A)
    for i in range(0, len(A)):
        print(A[i], end=" ")