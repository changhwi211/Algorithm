# 알고스팟
# url : https://www.acmicpc.net/problem/1261
# ref : https://gist.github.com/Baekjoon/9da1eed82383645026cc
# desc: deque 사용
from sys import stdin, stdout

M, N = map(int, stdin.readline().split())
m = []
for _ in range(N):
    row = list(map(int, stdin.readline().rstrip()))
    m.append(row)
ans = [[None for _ in range(M)] for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dq = []

ans[0][0] = 0
dq.append((0, 0))

while ans[N-1][M-1] is None:
    x, y = dq.pop(0)
    for dx, dy in move:
        cur_x, cur_y = x + dx, y + dy
        if 0 <= cur_x <= N-1 and 0 <= cur_y <= M-1:
            if ans[cur_x][cur_y] is None:
                if m[cur_x][cur_y] == 0:
                    ans[cur_x][cur_y] = ans[x][y]
                    dq.insert(0, (cur_x, cur_y))
                else:
                    ans[cur_x][cur_y] = ans[x][y] + 1
                    dq.append((cur_x, cur_y))

stdout.write(str(ans[N-1][M-1])+"\n")