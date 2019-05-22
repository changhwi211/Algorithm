# 부분합
# url : https://www.acmicpc.net/problem/1806
# ref : https://gist.github.com/Baekjoon/9ef1d516e28e46285cfb
# desc :
from sys import stdin, stdout

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

ans = n + 1
sum_ = arr[0]
left, right = (0, 0)
while True:
    if sum_ < s:
        right += 1
        if right >= n:
            break
        sum_ += arr[right]
    else:
        ans = min(right-left+1, ans)
        sum_ -= arr[left]
        left += 1
        if left > right:
            right = left
        if right >= n:
            break

if ans > n:
    ans = 0
stdout.write(str(ans)+"\n")