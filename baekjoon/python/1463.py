# 1로 만들기
# url : https://www.acmicpc.net/problem/1463
# ref : https://gist.github.com/Baekjoon/63b659f985beb8f64ca7
# desc : 
# Top-Down
# This code raise RecursionError for recursion limit

from sys import stdin, stdout

n = int(stdin.readline())
d = [None for _ in range(n+1)]

def go(n):
    if n == 1:
        return 0
    if d[n] is not None:
        return d[n]
    d[n] = go(n-1) + 1
    if n % 3 == 0:
        tmp = go(n//3) + 1
        if d[n] > tmp:
            d[n] = tmp
    if n % 2 == 0:
        tmp = go(n//2) + 1
        if d[n] > tmp:
            d[n] = tmp
    return d[n]

stdout.write(str(go(n))+"\n")