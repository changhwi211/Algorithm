# 소수의 연속합 성공
# url : https://www.acmicpc.net/problem/1644
# ref : https://gist.github.com/Baekjoon/9ef1d516e28e46285cfb
# desc :
from sys import stdin, stdout

n = int(stdin.readline().strip())
# get prime number
is_sosu = [True for _ in range(n+1)]
sosu = []
for i in range(2, n+1):
    if is_sosu[i]:
        sosu.append(i)
    else:
        continue
    for j in range(i*i, n+1, i):
        is_sosu[j] = False

ans = 0
left, right = (0, 0)
sum_ = sosu[0] if len(sosu) > 0 else None
while sum_:
    if sum_ < n:
        right += 1
        if right >= len(sosu):
            break
        sum_ += sosu[right]
    else:
        if sum_ == n:
            ans += 1
        sum_ -= sosu[left]
        left += 1
        if left > right and left < len(sosu):
            right= left
            sum_ = sosu[left]
        elif left >= len(sosu):
            break

stdout.write(str(ans)+"\n")