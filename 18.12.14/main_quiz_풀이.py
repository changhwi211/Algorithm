def solution(A):
    num_dict = {}
    for i, key in enumerate(A):
        if num_dict.get(key):
            num_dict[key][1] += 1
        else:
            num_dict[key] = [i, 1]
    
    if num_dict:
        max_key = max(num_dict, key=lambda x: num_dict[x][1])
        if num_dict[max_key][1] > len(A)//2:
            return num_dict[max_key][0]
    return -1

A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))

A = []
print(solution(A))

A = [2, -1, 0, -1, 3, -1, -1]
print(solution(A))

A = [2, 2, 3, 3]
print(solution(A)) 