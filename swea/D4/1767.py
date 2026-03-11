# 1767 - 프로세서 연결하기

'''
전체 코드 구조
1. 입력 받기
2. 내부 코어만 리스트에 저장
3. DFS 탐색
4. 최대 코어 + 최소 전선 길이 출력
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# idx : 지금 고려 중이 코어의 인덱스
# core_count : 연결된 코어 수 
# wire_len :지금까지 연결된 라인 수
def dfs(idx, core_cnt, wire_len):  # idx: 현재 처리할 코어 번호, core_cnt: 지금까지 연결된 코어 수, wire_len: 사용한 전선 길이
    global max_core, min_len

    # 가지치기 - 연결 안 하는 선택지가 있어서 
    # 현재 연결된 코어 + 남은 코어 -> 현재 최대 코어보다 작으면 탐색할 필요 X
    if core_cnt + (len(cores) - idx) < max_core:
        return

    # 종료
    # 모든 코어를 다 검사했을 때
    if idx == len(cores):
        # 현재 결과 vs 최적 결과
        if core_cnt > max_core:
            max_core = core_cnt
            min_len = wire_len
        # 코어 수가 같으면 전선 길이 최소 갱신
        elif core_cnt == max_core:
            min_len = min(min_len, wire_len)
        return

    # 현재 코어 위치
    r, c = cores[idx]

    for dir in range(4):
        nr, nc = r, c
        length = 0

        # 연결 가능한지 확인
        while True:
            nr += dr[dir]
            nc += dc[dir]

            # 연결이 가능한 경우
            # 가장자리 도달 -> 성공
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            
            # 연결이 불가능한 경우 
            # 다음이 있으면 실패
            if cell[nr][nc] != 0:
                length = 0
                break
            
            # 가능하면 길이 증가
            length += 1

        # 연결 불가능한 방향은 스킵
        if length == 0:
            continue

        # 전선 설치 (다시 코어 위치로 돌아옴)
        nr, nc = r, c

        for _ in range(length):
            nr += dr[dir]
            nc += dc[dir]
            cell[nr][nc] = 2
        
        dfs(idx + 1, core_cnt + 1, wire_len + length)   # 다음 코어 탐색

        # 전선 제거
        nr, nc = r, c
        for _ in range(length):
            nr += dr[dir]
            nc += dc[dir]
            cell[nr][nc] = 0

    # 연결 안 한 케이스도 봐야되기 때문
    # 모든 코어를 연결하는게 항상 최적은 아님
    # 코어 최대 -> 전선 최소 이기 때문에 포기하는 경우도 탐색
    dfs(idx + 1, core_cnt, wire_len)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in range(N)]

    cores = []  # 코어들의 위치 

    for i in range(N):
        for j in range(N):
            if cell[i][j] == 1:

                # 가장자리에 있는 코어는 제외 
                if i == 0 or i == N-1 or j == 0 or j == N-1:   # 가장 자리 코어는 이미 전원 연결됐기 때문
                    continue
                cores.append((i, j))
                # 튜플 > 변화하지 않을 좌표일 때 사용 

    max_core = 0
    min_len = N**2  # 라인 수가 다 채워져도 N제곱보다는 안 넘으니까 float('int')와 같은 의미 

    dfs(0, 0, 0)

    print(f'#{tc} {min_len}')