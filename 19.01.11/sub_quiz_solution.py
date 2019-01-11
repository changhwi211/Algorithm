def solution(s):
    d_cnt = 0
    pre_c = s[0]
    for cur_c in s[1:]:
        if pre_c == cur_c:
            d_cnt += 1
        else:
            pre_c = cur_c
    return d_cnt

# 3번 지워서 A 1 장
print(solution("AAAA"))
# 4번 지워서 B 1장
print(solution("BBBBB"))
# 0번 AB 4장
print(solution("ABABABAB"))
# 0번 BA 3장
print(solution("BABABA"))
# 4번 AB 1장
print(solution("AAABBB"))