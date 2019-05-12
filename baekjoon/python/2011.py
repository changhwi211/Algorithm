# 암호코드
# url : https://www.acmicpc.net/problem/2011
# ref : https://gist.github.com/Baekjoon/dc071a89a81cb88fb887
# desc : 

from sys import stdin, stdout

mod = 1000000
d = [0 for _ in range(5000+1)]
s = stdin.readline().rstrip()
n = len(s)
s = " " + s
d[0] = 1

for i, c in enumerate(s[1:], 1):
    if 1 <= int(c) <= 9:
        d[i] += d[i-1]
    if i == 1:
        continue
    if 10 <= int(s[i-1:i+1]) <= 26:
        d[i] += d[i-2]
    d[i] %= mod
stdout.write(str(d[n])+"\n")