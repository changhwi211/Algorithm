def solution(s):
    cnt = 0
    if s.count("AB"):
        cnt = 2 * s.count("AB")
    elif s.count("BA"):
        cnt = 2 * s.count("BA")
    elif s.count("A"):
        cnt = 1
    elif s.count("B"):
        cnt = 1
    return len(s) - cnt

# 3번 지워서 A 1 장
print(solution("AAAA"))
# 4번 지워서 B 1장
print(solution("BBBBB"))
# 0번 AB 4장
print(solution("ABABABAB"))
# 2번 AB 2장
print(solution("BABABA"))
# 4번 AB 1장
print(solution("AAABBB"))