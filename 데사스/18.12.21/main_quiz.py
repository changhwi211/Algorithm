def solution(arr):
    cnt = 0
    if not arr:
        return cnt
    for i in range(len(arr)):
        temp_arr = arr[i:]
        min_val = min(temp_arr)
        
        if arr[i] != min_val:
            min_idx = arr.index(min_val)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            cnt += 1
    return cnt

print(solution([7, 1, 3, 2, 4, 5, 6]))

print(solution([4, 3, 1, 2]))

print(solution([2, 3, 4, 1, 5]))

print(solution([]))

print(solution([1, 1, 1, 1]))

print(solution([-1, 2, -3, 1, 5]))