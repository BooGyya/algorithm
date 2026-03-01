# 응용 
# 23795 - 우주괴물 
# <괴물이 여러 마리일 때>

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 모든 괴물의 위치 찾기
    monsters = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                monsters.append((r, c))

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 2. 각 괴물마다 광선 발사
    for xr, xc in monsters:
        for d in range(4):
            nr = xr + dr[d]
            nc = xc + dc[d]

            # 범위 안이고 벽(1)을 만나기 전까지 광선 이동
            # 괴물(2)은 이미 지나친 곳으로 간주하여 통과 가능하게 처리
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
                # 안전한 칸(0)이면 광선이 닿았다는 표시(-1)
                if arr[nr][nc] == 0:
                    arr[nr][nc] = -1
                
                # 다음 칸으로 계속 이동
                nr += dr[d]
                nc += dc[d]

    # 3. 안전한 빈 칸(0) 세기
    count = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                count += 1

    print(f'#{tc} {count}')