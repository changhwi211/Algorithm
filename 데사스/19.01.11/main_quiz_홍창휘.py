def solution(n, queries):
    li = [0 for _ in range(n)]
    for query in queries:
        if query[0] == query[1]:
            li[query[0]-1] += query[2]
        else:
            for i in range(query[0], query[1]+1):
                li[i-1] += query[2]
    print(li)
    return max(li)

n=5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]
print(solution(n=n, queries=queries))

n=5
queries = [
    [1, 1, 300],
    [2, 5, 100],
    [3, 4, 100]
]
print(solution(n=n, queries=queries))

n=3
queries = [
    [3, 3, 100],
    [3, 3, 100],
    [3, 3, 100]
]
print(solution(n=n, queries=queries))

n=int(1e7)
queries = [
    [1, 1, int(1e9)],
    [3, 3, 100],
    [3, 3, 100]
]
print(solution(n=n, queries=queries))