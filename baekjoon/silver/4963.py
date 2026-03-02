# 4963 - 섬의 개수
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, 1, -1, -1, 1]


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    def dfs(r, c):
        graph[r][c] = 0
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < h and 0 <= nc < w and graph[nr][nc] == 1:
                dfs(nr, nc)


    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
