# 23795 - 우주괴물
'''
괴물 찾기 (2일 때)
델타 사용해서 0을 찾기 
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2차원 리스트 입력받기  
    count = 0

    # 괴물 찾기 
    zero_sum = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                zero_sum += 1
            elif arr[r][c] == 2:
                a = r
                b = c

    # 4방향 탐색 
    for dir in range(4):
        x = a
        y = b
        while True:
            # 방향을 한 곳 정해서 쭉 전진
            nx = x + dr[dir]
            ny = y + dc[dir]
            # 우선적으로 좌표가 범위 안이여야 함
            if 0 <= nx < N and 0 <= ny < N:
                # 탐색한 곳이 1이면 종료 (더 전진할 필요 없음)
                if arr[nx][ny] == 1:
                    break
                # 0이면 괴물이 레이저를 쏘는 곳이므로 카운트하고 전진을 위해 x,y에 nx, ny를 갱신
                elif arr[nx][ny] == 0:
                    x = nx
                    y = ny
                    count += 1
            # 좌표가 범위를 벗어나면 종료 (전진할 필요 없음)
            else:
                break
                            
    result = zero_sum-count

    print(f'#{tc} {result}')