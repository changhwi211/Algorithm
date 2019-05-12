# 제곱수의 합
# url : https://www.acmicpc.net/problem/1699
# ref : https://gist.github.com/Baekjoon/66c23e0a64ae7924aa19
# desc : This code takes too much time for input of max N(100000) => O(n*sqrt(n))

from sys import stdin, stdout

n = int(stdin.readline())
d = [0 for _ in range(n+1)]

for i in range(1, n+1):
    d[i] = i
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j] + 1:
            d[i] = d[i-j*j] + 1
        j += 1

stdout.write(str(d[n])+"\n")