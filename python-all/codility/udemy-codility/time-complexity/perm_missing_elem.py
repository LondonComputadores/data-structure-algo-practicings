def solution(A):
    actual_sum = 0
    for number in A:
        actual_sum += number
    max_number = len(A) + 1
    expected_sum = (max_number * (max_number + 1) // 2)
    return expected_sum - actual_sum

print(solution([2, 3, 1, 5]))       # Should return= 4, ok.

print(solution([1, 2, 3]))          # Should return= 4, ok.

print(solution([1, 3, 6, 4, 1, 2])) # Should return= 5, but returning 11.

print(solution([-1, -3]))           # Should return= 1, but returning 10.
