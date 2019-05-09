# 알고스팟
# url : https://www.acmicpc.net/problem/1261
# ref : 
# https://gist.github.com/Baekjoon/3d8ed2a3976c7affbd73
# https://medium.com/@yhmin84/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-priority-queue-%EB%A5%BC-%EC%9C%84%ED%95%9C-heapq-%EB%AA%A8%EB%93%88-%EC%82%AC%EC%9A%A9%EB%B2%95-b33c4e0ef2b1
# desc: 우선순위 queue 사용
from sys import stdin, stdout
import heapq

M, N = map(int, stdin.readline().split())
m = []
for _ in range(N):
    row = list(map(int, stdin.readline().rstrip()))
    m.append(row)
ans = [[None for _ in range(M)] for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
h = []

ans[0][0] = 0
heapq.heappush(h, (ans[0][0], (0, 0)))

while ans[N-1][M-1] is None:
    x, y = heapq.heappop(h)[1]
    for dx, dy in move:
        cur_x, cur_y = x + dx, y + dy
        if 0 <= cur_x <= N-1 and 0 <= cur_y <= M-1:
            if ans[cur_x][cur_y] is None:
                if m[cur_x][cur_y] == 0:
                    ans[cur_x][cur_y] = ans[x][y]
                else:
                    ans[cur_x][cur_y] = ans[x][y] + 1
                heapq.heappush(h, (ans[cur_x][cur_y], (cur_x, cur_y)))

stdout.write(str(ans[N-1][M-1])+"\n")