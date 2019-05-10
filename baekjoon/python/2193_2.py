# 이친수
# url : https://www.acmicpc.net/problem/2193
# ref : https://gist.github.com/Baekjoon/49b2bfd22be42707bb88
# desc : Bottom-up

from sys import stdin, stdout

d = [None for _ in range(90+1)]
n = int(stdin.readline())

d[1] = 1
d[2] = 1
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

stdout.write(str(d[n])+"\n")