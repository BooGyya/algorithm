# 2667 - 단지번호 붙이기
# BFS 활용

from collections import deque

N = int(input())
danji = [list(map(int, input().strip())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    danji[r][c] = 0  # 방문 표시
    count = 1        # 단지 내 집 개수 세기 시작 
    
    while queue:
        cur_r, cur_c = queue.popleft() # 큐의 맨 앞에서부터 꺼냄
        
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]
            
            # 범위 내에 있고 집(1)인 경우
            if 0 <= nr < N and 0 <= nc < N and danji[nr][nc] == 1:
                danji[nr][nc] = 0       # 방문 처리
                queue.append((nr, nc))  # 큐에 넣어서 나중에 탐색하게 함
                count += 1
                
    return count

result = []
for i in range(N):
    for j in range(N):
        if danji[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
for x in sorted(result):
    print(x)