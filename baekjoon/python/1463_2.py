# 1로 만들기
# url : https://www.acmicpc.net/problem/1463
# ref : https://gist.github.com/Baekjoon/31e553ab3b371fe06384
# desc : Bottom-up

from sys import stdin, stdout

n = int(stdin.readline())
d = [None for _ in range(n+1)]

d[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
    if i % 2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1

stdout.write(str(d[n])+"\n")