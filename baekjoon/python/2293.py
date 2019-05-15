# 동전 1
# url : https://www.acmicpc.net/problem/2293
# ref : https://gist.github.com/Baekjoon/64855ce0c5f17cf40901
# desc: 

from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(stdin.readline().strip()))
d = [0 for _ in range(k+1)]

d[0] = 1
for i in range(n):
    for j in range(1, k+1):
        if j >= coins[i]:
            d[j] += d[j-coins[i]]

stdout.write(str(d[k])+"\n")