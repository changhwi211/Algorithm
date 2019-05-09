def solution(A, k):
    li_add_k = list(map(lambda x: x+k, A))
    set_add_k = set(li_add_k)
    set_A = set(A)
    return len(set_A.intersection(set_add_k))

print(solution([1, 5, 3, 4, 2], 2))

print(solution([1,3,4,5,6,7,8,9], 1))

print(solution([1,3,4,5,6,7,8,9], 2))

print(solution([1,3,4,5,6,7,8,9], 3))

print(solution([2, 3], 1))

print(solution([2, 3], 3))