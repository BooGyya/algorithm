# 1226 - 미로1 

'''
1. 
2. 방문 리스트 배열 만들기
3. dfs 
(4. bfs)
델타
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():

    visited = [[0]*16 for _ in range(16)]   # 빈 16×16 격자 생성


T = 10
for tc in range(1, T+1):
    answer = 0
    input()
    arr = [list(map(int, input())) for _ in range(16)]
    r, c, goal_r, goal_c = -1, -1, -1, -1   # 초기화

    # 출발점과 도착점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2: 
                r = i
                c = j
            elif arr[i][j] == 2:
                goal_r = i
                goal_c = j
    
    # 방문 리스트 배열 생성 

    

    
    bfs(r,c)

    print(f'#{tc} {answer}')