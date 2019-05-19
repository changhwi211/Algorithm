# 부분수열의 합
# url : https://www.acmicpc.net/problem/1182
# ref : https://gist.github.com/Baekjoon/5d90f9d1582559c619ad2821b126ac16
# desc: 
from sys import stdin, stdout

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
cnt = 0

def go(i, sum_):
    global cnt

    if i == n:
        if sum_ == s:
            cnt += 1
        return
    
    go(i+1, sum_+arr[i])
    go(i+1, sum_)

if s == 0:
    cnt -= 1
go(0, 0)
stdout.write(str(cnt)+"\n")