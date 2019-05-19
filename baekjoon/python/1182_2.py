# 부분수열의 합
# url : https://www.acmicpc.net/problem/1182
# ref : https://gist.github.com/Baekjoon/f4154089addcd1adacc5
# desc: 비트마스크 사용
from sys import stdin, stdout

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
cnt = 0

for i in range(1, 1<<n):
    sum_ = 0
    for k in range(n):
        if i & (1<<k):
            sum_ += arr[k]
    if sum_ == s:
        cnt += 1

stdout.write(str(cnt)+"\n")