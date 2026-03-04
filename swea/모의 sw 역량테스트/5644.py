# 5644 - 무선충전 

'''
좌표가 (1,1) 부터 시작함
범위 검사는 필요없음

필요한 데이터
    dr, dc > 방향 이동
    T > 테스트 케이스 수
    M > 이동 횟수 
    N > 배터리의 수
    A, B > 각각 A/B의 이동 경로 (델타의 인덱스로 주어짐)
    human_rcs > A(0번 인덱스),B(1번 인덱스)의 좌표
    BC_info > 배터리의 정보(N개)
    charge_idxs > (0) : A가 충전할 수 있는 위치 인덱스 모음
                  (1) : B가 충전할 수 있는 위치 인덱스 모음
      # [
         [], (-> A가 충전할 수 있는 위치)
         []  (-> B가 충전할 수 있는 위치)
        ]
설계
1. 이동 > M번

    2. 이동한 위치에서 A,B가 충전할 수 있는 충전소 파악하기
    - A,B 에서 충전소 간의 거리를 파악해서 해당 거리가 충전 범위 이내이면 충전 가능 > 번호를 저장해야 함 (charge_idxs)

    3. 최적의 충전량을 고르기 > max
    ㄱ. A만 충전할 수 없는 경우 (일중 for문 돌도록)
        > B를 반복 
    ㄴ. B만 충전할 수 없는 경우 (일중 for문 돌도록)
        > A를 반복 
    ㄷ. A,B 둘 다 충전 가능한 경우 (이중 for문을 돌도록)

    4. max 누적 

'''

# 방향 이동 (원래랑 다르게 이동하지 않음도 추가)
# 0: 이동하지 않음/ 1 : 상/ 2 : 우/ 3 : 하/ 4 : 좌
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]

T = int(input())

for tc in range(1, T+1):
    answer = 0  # 최대 충전량

    # M : 이동 횟수 / N : 배터리의 수
    M, N = map(int, input().split())
    
    A = list(map(int, input().split())) # A 이동 경로
    B = list(map(int, input().split())) # B 이동 경로
    human_rcs = [[1,1], [10,10]]    # 위치

    # BC_info > N
    # 0, 1 > 배터리 좌표
    # 2 > 배터리 충전 범위
    # 3 > 배터리 충전량 
    BC_info = [0]*N

    for i in range(N):
        BC_info[i] = list(map(int, input().split()))


    # 충전 > M+1번 (제약사항 7번 참고)  / 이동 > N번 
    for time in range(M+1): # time은 문제에서의 t를 의미함 -> 현재 시간 

        # 충전 가능한 위치 탐색 - A, B
        charge_idxs = [[], []]
        # A, B 중 누구를 돌지 > 0 or 1
        # i : A인지 B인지 (0이면 A, 1이면 B)
        for i in range(2):
            r, c = human_rcs[i] # 현재 사람의 좌표
            # 어떤 충전소인지 선택
            # j : 충전소 번호
            for j in range(N):
                BC_r, BC_c, coverage, charge_amount = BC_info[j] 

                # 범위 검사
                if abs(r - BC_r) + abs(c - BC_c) <= coverage:  # 해당 충전소와 사람 간의 차이 <= 
                    charge_idxs[i].append(j)    # i번째 사람은 j번의 충전소에 방문 가능

        # 최적 충전량 - ㄱ,ㄴ,ㄷ 참고
        charge = 0  # 최적 충전량
        # ㄱ. A가 충전할 수 없는 경우 
        if not charge_idxs[0]: # false일 때만 들어감 
            for i in charge_idxs[1]:    # B만 순회하면 됨
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]

        # ㄴ. B가 충전할 수 없는 경우 
        elif not charge_idxs[1]:
            for i in charge_idxs[0]:    # A만 순회하면 됨
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]

        # ㄷ. A와 B 모두 충전 가능한 경우
        else:
            # i : A의 충전소 번호
            for i in charge_idxs[0]:
                # j : B의 충전소 번호
                for j in charge_idxs[1]:
                    if i == j:
                        if BC_info[i][3] > charge: # i이든 j이든 상관없음
                            charge = BC_info[i][3]
                    else:
                        if BC_info[i][3] + BC_info[j][3] > charge:
                            charge = BC_info[i][3] + BC_info[j][3]
        # 위 코드까지의 결과는 현재 위치에서의 최적 충전량이 뽑힘 
        answer += charge

        # if time == M:
        #     break

            # human_rcs[0][0] += dr[A[time]]   
            # human_rcs[0][1] += dc[A[time]]

            # human_rcs[1][0] += dr[B[time]]
            # human_rcs[1][1] += dc[B[time]]

        # 이동
        if time != M:   # time은 0~M 까지 # 충전은 M+1 # 이동은 M
            human_rcs[0][0] += dr[A[time]]     # A의 현재 위치 r    
            human_rcs[0][1] += dc[A[time]]     # A의 현재 위치 c

            human_rcs[1][0] += dr[B[time]]     # B의 현재 위치 r
            human_rcs[1][1] += dc[B[time]]     # B의 현재 위치 c


    print(f'#{tc} {answer}')