# 부분수열의 합 2
# url : https://www.acmicpc.net/problem/1208
# ref : https://gist.github.com/Baekjoon/9a29c36ef0fcc80cbaf5
# desc: 
# This code doesn't make it in time.
# but, same algorithm in this code using C language would make it in time.

from sys import stdin, stdout

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr_l = arr[:n//2]
arr_r = arr[n//2:]
sum_l = []
sum_r = []
for i in range(1<<(n//2)):
    sum_ = 0
    for j in range(n//2):
        if i & (1<<j):
            sum_ += arr_l[j]
    sum_l.append(sum_)

for i in range(1<<(n-n//2)):
    sum_ = 0
    for j in range(n-n//2):
        if i & (1<<j):
            sum_ += arr_r[j]
    sum_r.append(sum_)

ans = 0
sum_l = sorted(sum_l)
sum_r = sorted(sum_r)
left = 0
right = len(sum_r) - 1
while left < len(sum_l) and right >= 0:
    sum_ = sum_l[left] + sum_r[right]
    cnt_l = 1
    cnt_r = 1

    while left < len(sum_l)-1 and sum_l[left+1] == sum_l[left]:
        left += 1
        cnt_l += 1
    while right > 0 and sum_r[right-1] == sum_r[right]:
        right -= 1
        cnt_r += 1
    if sum_ == s:    
        left += 1
        right -= 1
        ans += cnt_l * cnt_r
    elif sum_ > s:
        right -= 1
    else:
        left += 1
if s == 0:
    ans -= 1
stdout.write(str(ans)+"\n")