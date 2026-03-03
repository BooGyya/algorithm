T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # dfs 함수 정의 > 재귀를 사용하여 델타 탐색
    def dfs(r,c):
        global count    # 광산의 크기
        global size     # 최대 채굴량

        size = 0
        size += arr[r][c]
        arr[r][c] = 0
        count = 1

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 안이면서 0이 아닌 값 찾기
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0:
                count += dfs(nr,nc)

        return count

    # 광산 후보지 전체 탐색
    gold = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                gold.append(dfs(i,j))
                max_size = 0
                if size > max_size:
                    max_size = size

    max_gold = max(gold)

    print(f'#{tc} {max_gold} {max_size}')
