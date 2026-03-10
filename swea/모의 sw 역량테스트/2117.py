# 2117 - 홈 방범 서비스

def calc_cost(K): # K일때 비용 계산
    return K*K+(K-1)*(K-1)

def search_K(K, cost):
    max_home_count = 0

    for r in range(N):
        for c in range(N):

            home_count = 0
            for dis in range(K):
                home_count += dp[r][c][dis]
            
            if home_count > max_home_count and home_count*M >= cost:
                max_home_count = home_count

    return max_home_count


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 1

    # dp[r][c][dis] = count => [r][c] : 기준점 / [dis] : r,c 지점으로 만큼의 거리
    dp = [[[0] * ((N-1) * 2+1) for _ in range(N)] for _ in range(N)]
    '''
    [0] * ((N-1) * 2+1) > dis
    for _ in range(N) > c
    for _ in range(N) > r
    '''

    # 기준점
    for home_r in range(N):
        for home_c in range(N):
            if graph[home_r][home_c] == 1:

                # 모든 지점에 대해서
                for r in range(N):
                    for c in range(N):
                        dp[r][c][abs(home_r-r)+abs(home_c-c)] += 1

    max_k = N+1 if N % 2 == 0 else N
    for K in range(max_k, 1, -1):
        result = search_K(K, calc_cost(K))
        if result :
            answer = result
            break

    print(f'#{tc} {answer}')