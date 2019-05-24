# 합이 0인 네 정수
# url : https://www.acmicpc.net/problem/7453
# ref : 
# desc
# This code uses a lot of memory then over memory limit
from sys import stdin, stdout

n = int(stdin.readline().strip())
A = []
B = []
C = []
D = []
for _ in range(n):
    tmp = list(map(int, stdin.readline().split()))
    A.append(tmp[0])
    B.append(tmp[1])
    C.append(tmp[2])
    D.append(tmp[3])
    del tmp

arr_l = []
arr_r = []
for i in range(n):
    for j in range(n):
        arr_l.append(A[i]+B[j])
        arr_r.append(C[i]+D[j])
del A, B, C, D
arr_sorted_l = sorted(arr_l)
del arr_l
arr_sorted_r = sorted(arr_r)
del arr_r

m = n * n
left = m-1
right = 0
ans = 0
while left >= 0 and right < m:
    cnt_r = 1
    cnt_l = 1
    while right < m-1 and arr_sorted_r[right+1] == arr_sorted_r[right]:
        right += 1
        cnt_r += 1
    while left > 0 and arr_sorted_l[left-1] == arr_sorted_l[left]:
        left -= 1
        cnt_l += 1
    if arr_sorted_l[left] == -arr_sorted_r[right]:
        ans += cnt_r * cnt_l
        left -= 1
        right += 1
    elif arr_sorted_l[left] > -arr_sorted_r[right]:
        left -= 1
    elif arr_sorted_l[left] < -arr_sorted_r[right]:
        right += 1

stdout.write(str(ans)+"\n")