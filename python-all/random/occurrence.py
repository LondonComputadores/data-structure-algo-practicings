def solution(A, X):
    if len(A) == 0:
        return -1
    l = 0
    r = len(A) -1
    while l < r:
        n = (l + r) // 2
        if A[n] > X:
            r = n - 1
        else:
            l = n
    if A[l] == X:
        return l
    return -1
    

print(solution([0], 5))
print(solution([1,2,5,9,9], 5))