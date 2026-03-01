# 23795 - 우주괴물

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    xr = xc = 0 # (xr, xc) 괴물 좌표
    count = 0   # 안전한 빈 칸 

    # 1. 괴물의 위치 찾기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                xr = r
                xc = c

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 2. 괴물마다 광선 발사
    for d in range(4):
        nr = xr + dr[d]
        nc = xc + dc[d]

        # 이동한 칸이 범위 안이고 1(벽)이 아닐 때
        while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
            if arr[nr][nc] == 0:
                arr[nr][nc] = -1

            # 다음칸 이동
            nr += dr[d]
            nc += dc[d]

        # 이동한 칸이 범위를 넘거나 1(벽)을 만나면 while문 종료,
        # 방향(d)을 바꿔 다시 탐색 진행

    # 3. 안전한 빈 칸 세기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                count += 1

    print(f'#{tc} {count}')