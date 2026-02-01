def mergesort(A, l, r):
    if (l >= r): 
        return
    m = l + (r-l)//2
    mergesort(A, l, m)
    mergesort(A, m+1, r)
    B = [0]*(r-l+1)
    i = l
    j = m+1
    k = 0
    while (i <= m or j <= r):
        if (j > r or (i <= m and A[i] <= A[j])):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    for idx in range(l, r+1):
        A[idx] = B[idx-l]

if __name__ == "__main__":
    A = list(map(int, input().split()))
    n = len(A)
    mergesort(A, 0, n-1)
    for i in range(0, n):
        print(A[i], end=" ")