# 2667 - 단지번호 붙이기
'''
방문 표시가 안 돼있는 1이 있는지 찾고
찾으면 거기서 부터 dFS로 인접한 1까지 찾으면서 0으로 방문 표시
방문 표시 한 만큼이 단지내 집의 수
BFS를 수행한 만큼이 총 단지 수
'''

# 1. 변수 설정
N = int(input())
danji = [list(map(int, input().strip())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 3. dfs 함수 > 재귀를 사용하여 델타로 아파트 수 저장
def dfs(r, c):
    danji[r][c] = 0     # 방문한 곳은 0으로 바꿔 다시 방문하지 않도록 함 
    count = 1           # 단지 내 아파트 수 저장, 방문하면 1 할당 

    # 4방향 탐색
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 범위 안이면서 집이 있는 곳(1)이면 
        if 0 <= nr < N and 0 <= nc < N and danji[nr][nc] == 1:
            count += dfs(nr, nc)    # 인접한 칸을 탐색하여 얻은 집의 개수(반환값)를 현재 count에 더함

    return count    # 해당 단지의 총 집 개수 반환 

# 2. 단지 전체 탐색 
result = [] # 단지 수 저장할 리스트

for i in range(N):
    for j in range(N):
        if danji[i][j] == 1:    # 집을 발견하면 
            result.append(dfs(i, j))    # 그곳부터 dfs 탐색 시작

print(len(result))          # 단지의 개수
for x in sorted(result):    # 단지 수 오름차순 정렬
    print(x)