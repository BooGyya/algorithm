# 4831 - 전기버스 

T = int(input())

for tc in range(1, T + 1):
    answer = 0
    K, N, M = map(int, input().split())
    bus_stops = [0] + list(map(int, input().split()))

    cur_pos = stop_idx = 0   # stop_idx = 최근에 충전한 충전소의 위치
    
    while cur_pos+K < N:
        
        for i in range(M, stop_idx, -1):
            if bus_stops[i] <= cur_pos+K:
                stop_idx = i
                cur_pos = bus_stops[i]
                answer += 1
                break
        # 다음 충전소를 못 찾았을 때 
        else:
            answer = 0
            break

    print(f'#{tc} {answer}')