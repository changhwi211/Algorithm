def solution(A):
    sum = 0
    cnt = 0
    for i, val in enumerate(A, 1):
        sum += val
        if val == 1:
            cnt += (i - sum)
    if cnt==0:
        return 0
    return cnt

print(solution([0, 1, 0, 1, 1]))

print(solution([1, 0]))