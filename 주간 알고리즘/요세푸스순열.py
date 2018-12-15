def solution(N, K):
    li = [i for i in range(1, N+1)]
    cur_idx = 0
    ret_str = "<"

    while True:
        cur_idx += K-1
        while cur_idx >= len(li):
            cur_idx = cur_idx - len(li)
        if len(li) > 1:
            ret_str += str(li.pop(cur_idx)) + ", "
        else:
            ret_str += str(li.pop(cur_idx)) + ">"
            return ret_str

print(solution(7, 3))