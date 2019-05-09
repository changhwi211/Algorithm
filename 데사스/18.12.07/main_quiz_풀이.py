def test(func):
    cases = [
        (5, [2, 1, 2, 6, 2, 4, 3, 3]),
        (4, [4, 4, 4, 4, 4]),
        (10, [3, 4, 5, 3, 4, 4]),
        (10, [9])
    ]
    results = [
        [3, 4, 2, 1, 5],
        [4, 1, 2, 3],
        [5, 4, 3, 1, 2, 6, 7, 8, 9, 10],
        [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]
    ]

    for i, case in enumerate(cases):
        try:
            assert func(*case) == results[i]
        except AssertionError:
            print(func(*case), case)
            raise
        print("success", i)
    print("SUCCESS")

def solution(N, stages):
    dict_fail = {i: 0 for i in range(1, N+1)}
    denominator = len(stages)

    for i in range(1, N+1):
        cnt = stages.count(i)
        dict_fail[i] = cnt / denominator
        denominator -= cnt
        if denominator == 0:
            break
    
    return sorted(dict_fail, key=lambda x: (dict_fail[x], -x), reverse=True)

test(solution)