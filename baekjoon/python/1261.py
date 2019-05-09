# 알고스팟
# url : https://www.acmicpc.net/problem/1261
# ref : https://gist.github.com/Baekjoon/3d8ed2a3976c7affbd73
# desc: queue 사용
from sys import stdin, stdout

M, N = map(int, stdin.readline().split())
m = []
for _ in range(N):
    row = list(map(int, stdin.readline().rstrip()))
    m.append(row)
ans = [[None for _ in range(M)] for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cur_q = []
next_q = []

ans[0][0] = 0
cur_q.append((0, 0))

while ans[N-1][M-1] is None:
    x, y = cur_q.pop(0)
    for dx, dy in move:
        cur_x, cur_y = x + dx, y + dy
        if 0 <= cur_x <= N-1 and 0 <= cur_y <= M-1:
            if ans[cur_x][cur_y] is None:
                if m[cur_x][cur_y] == 0:
                    ans[cur_x][cur_y] = ans[x][y]
                    cur_q.append((cur_x, cur_y))
                else:
                    ans[cur_x][cur_y] = ans[x][y] + 1
                    next_q.append((cur_x, cur_y))
    if not cur_q:
        cur_q = next_q
        next_q = []

stdout.write(str(ans[N-1][M-1])+"\n")