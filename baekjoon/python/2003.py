from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

left, right = (0, 0)
cnt = 0
sum_ = arr[0]
while True:
    if sum_ < m:
        right += 1
        # 수열의 합이 더 이상 m으로 커질 수 없는 경우
        if right >= n:
            break
        sum_ += arr[right]
    elif sum_ == m:
        cnt += 1
        right += 1
        # 수열의 합이 더 이상 m으로 커질 수 없는 경우
        if right >= n:
            break
        sum_ += arr[right]
    else:
        sum_ -= arr[left]
        left += 1
        if left > right and left < n:
            right = left
            sum_ = arr[right]
        # 수열의 합이 더 이상 m으로 작아질 수 없는 경우
        elif left >= n:
            break

stdout.write(str(cnt)+"\n")    