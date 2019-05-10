# 이친수
# url : https://www.acmicpc.net/problem/2193
# ref : https://gist.github.com/Baekjoon/49b2bfd22be42707bb88
# desc : Top-Down

from sys import stdin, stdout

d = [None for _ in range(90+1)]
n = int(stdin.readline())

def go(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if d[n] is not None:
        return d[n]
    d[n] = go(n-1) + go(n-2)
    return d[n]

stdout.write(str(go(n))+"\n")