# 기타리스트
# url : https://www.acmicpc.net/problem/1495
# ref : https://gist.github.com/Baekjoon/307d2dd070857278d8f6
# desc: 
from sys import stdin, stdout

n, s, m = map(int, stdin.readline().split())
v = [0]
v.extend(list(map(int, stdin.readline().split())))
d = [[False for _ in range(m+1)] for _ in range(n+1)]
d[0][s] = True

for i in range(n):
    for j in range(m+1):
        if not d[i][j]:
            continue
        if j - v[i+1] >= 0:
            d[i+1][j-v[i+1]] = True
        if j + v[i+1] <= m:
            d[i+1][j+v[i+1]] = True

ans = -1
for i in reversed(range(m+1)):
    if d[n][i]:
        ans = i
        break
stdout.write(str(ans)+"\n")