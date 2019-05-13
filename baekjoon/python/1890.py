# 점프
# url : https://www.acmicpc.net/problem/1890
# ref : https://gist.github.com/Baekjoon/b5f8bae461a2e43a35b25d515a6b5946
# desc: 

from sys import stdin, stdout

n = int(stdin.readline())
A = []
for _ in range(n):
    A.append(list(map(int, stdin.readline().split())))
d = [[0 for _ in range(n)] for _ in range(n)]

d[0][0]= 1
for i in range(n):
    for j in range(n):
        for k in range(1, j+1):
            if A[i][j-k] == k:
                d[i][j] += d[i][j-k]
        for k in range(1, i+1):
            if A[i-k][j] == k:
                d[i][j] += d[i-k][j]

stdout.write(str(d[n-1][n-1])+"\n")