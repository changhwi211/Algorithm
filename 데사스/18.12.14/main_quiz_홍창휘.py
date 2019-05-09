def solution(A):
    num_dict = {}
    length = len(A)
    for idx, key in enumerate(A):
        cnt_li = num_dict.get(key)
        if cnt_li:
            cnt_li.append(idx)
            num_dict[key] = cnt_li
        else:
            num_dict[key] = [idx]
    
    max_key = sorted(num_dict, key=lambda x: len(num_dict[x]), reverse=True)[0]
    max_li = num_dict.get(max_key) 
    if len(max_li) > (length // 2):
        return max_li[0]
    else:
        return -1

A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))

A = [3, 4, 2, 2, -1, -1, -1, 3]
print(solution(A))

A = [3, 2, 2, 2, 3, 2, 3, 3, 2, 2]
print(solution(A))