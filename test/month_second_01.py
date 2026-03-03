T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 술래를 찾아서 persons에 할당
    persons = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                persons.append((r,c))

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 4방향 탐색
    for xr, xc in persons:
        for d in range(4):
            nr = xr + dr[d]
            nc = xc + dc[d]

            # 범위 안이면서 벽이 아니면(1) while문 동작
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = -1    # 술래가 감시할 수 있는 칸을 -1로 할당
                nr += dr[d]     # 한 방향에서 계속 탐색
                nc += dc[d]

    # 감시를 피할 수 있는 통로 칸의 수(0) 구하기
    count = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                count += 1

    print(f'#{tc} {count}')