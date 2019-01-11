def my_accum(arr):
    result = 0
    for el in arr:
        result += el
        yield result

def solution(n, queries):
    B = [0 for _ in range(n+1)]
    for start, end, k in queries:
        B[start-1] += k
        B[end] -= k
        print(list(my_accum(B)))
    return max(my_accum(B))

n=5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]
print(solution(n=n, queries=queries))
    