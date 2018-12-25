def solution(heights):
    li = []
    answer = []
    for idx, height in enumerate(heights, 1):
        recv = False
        while li:
            if li[-1][1] <= height:
                li.pop()
            else:
                answer.append(li[-1][0])
                recv = True
                break
        if not recv:
            answer.append(0)
        li.append((idx, height))
    return answer

print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))