# 이동하기
# url : https://www.acmicpc.net/problem/11048
# ref : https://gist.github.com/Baekjoon/65f34d5cf5f329dde337
# desc: 

from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
A = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    A[i][1:] = map(int, stdin.readline().split())
d = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max([d[i-1][j], d[i][j-1], d[i-1][j-1]]) + A[i][j]

stdout.write(str(d[n][m])+"\n")