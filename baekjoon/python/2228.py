# 구간 나누기
# url : https://www.acmicpc.net/problem/2228
# ref : https://gist.github.com/Baekjoon/a751e2551ca4577dc1a5
# desc: 

from sys import stdin, stdout
from math import ceil

min_num = -32768*100 - 1
n, m = map(int, stdin.readline().split())

arr = [None for _ in range(n+1)]
for i in range(1, n+1):
    arr[i] = int(stdin.readline().strip())

s = [0]
for el in arr[1:]:
    s.append(s[-1]+el)

d = [[None for _ in range(m+1)] for _ in range(n+1)]
d[1][1] = arr[1]

def go(n, m):
    if m == 0:
        return 0
    if ceil(n/2) < m:
        return min_num
    if d[n][m] is not None:
        return d[n][m]
    else:
        d[n][m] = go(n-1, m)
        for i in range(1, n+1):
            ans = go(i-2, m-1) + s[n] - s[i-1]
            if ans > d[n][m]:
                d[n][m] = ans
    return d[n][m]

stdout.write(str(go(n, m))+"\n")