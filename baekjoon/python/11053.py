# 가장 긴 증가하는 부분 수열
# url : https://www.acmicpc.net/problem/11053
# ref : https://gist.github.com/Baekjoon/667ca791c2b9d5b1d2d2
# desc : 

from sys import stdin, stdout

n = int(stdin.readline())
d = [0 for _ in range(n)]
A = list(map(int, stdin.readline().split()))

d[0] = 1
for i in range(1, n):
    d[i] = 1
    for j in range(i):
        if A[i] > A[j] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1

stdout.write(str(max(d))+"\n")