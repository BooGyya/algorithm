# 5656 - 벽돌깨기
'''
0 빈 공간
N번 쏘기 
W X H 배열 
( 벽돌에 적힌 숫자 - 1 ) 칸 제거

남은 벽돌의 개수 구하기 


for문
    for문   
        if문 - 맨 아래가 0인지
            for문 - 맨 위 찾기
                if문 - 세로 탐색 (true면 큐에 넣고 종료)
            while문 - BFS 구현

'''

from itertools import product
from collections import deque
import copy 

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(H)]
    x_num = [i for i in range(W)]   # W의 인덱스 (x축)
    # 남은 벽돌 개수 세기
    count = 0
    for a in range(H):
        for b in range(W):
            if arr1[a][b] != 0:
                count += 1
    result = count           # 남은 벽돌의 개수
    for order in product(x_num, repeat = N): # 중복 순열된 값을 order에 넣음
        break_count = 0     # break_count > 벽돌을 깬 개수
        # 깊은 복사 
        arr = copy.deepcopy(arr1)
        for c_order in order:       # 튜플 order에 있는 값 하나를 c_order에 넣음

            # 높이의 맨 아래가 0이 아니면 실행
            if arr[H-1][c_order] != 0:
                # 맨 위 찾기 
                for height in range(H):
                    if arr[height][c_order] != 0:   # 세로 탐색할 값이 0이 아니면 실행 
                        q = deque()
                        q.append((height, c_order, arr[height][c_order])) # 최초 시작할 값을 찾으면 q에 넣고 종료
                        break   
                        # q : (x좌표, y좌표, 가중치(값))
                # BFS 구현
                while q:
                    r, c, v = q.popleft()   # 언패킹
                    arr[r][c] = 0   # 시작 좌표의 값을 0으로 (1일 경우에는 깨트리기 완료)
                    break_count += 1
                    # 1이 아니면 실행 (최적화)
                    if v != 1:
                        for i in range(1,v): # i > 깰 수 있는 범위
                            
                            # 4방향 탐색 
                            for d in range(4):
                                nr = r + dr[d]*i
                                nc = c + dc[d]*i
                                
                                # 범위 안
                                if 0 <= nr < H and 0 <= nc < W:

                                    # 탐색한 nr, nc가 0과 1이 아니면 실행
                                    if arr[nr][nc] != 0:
                                        if arr[nr][nc] != 1:
                                            q.append((nr, nc, arr[nr][nc])) # q에 넣기
                                            arr[nr][nc] = 0
                                        else:
                                            break_count += 1
                                            arr[nr][nc] = 0
                                    
                                    # 좌표 깨트리기

                # 가로 순회
                for j in range(W):
                    # 높이의 맨 아래의 좌표값을 가진 두 변수
                    sort = H-1      # sort > 항상 감소할 값
                    sub_sort = H-1  # sub_sort > 0이 아닐 때 감소할 값

                    # 정렬 
                    while sort >= 0:

                        if arr[sort][j] != 0 and arr[sub_sort][j] == 0:
                            arr[sort][j], arr[sub_sort][j] = arr[sub_sort][j],arr[sort][j]
                            sub_sort -= 1

                        if arr[sort][j] != 0:
                            sub_sort -= 1
                        sort -= 1
        if count - break_count < result:
            result = count - break_count
    
    print(f'#{tc} {result}')