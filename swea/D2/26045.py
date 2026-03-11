# 26045 - 부분 수열 판별

T = int(input())  # 테스트케이스 개수 

for tc in range(1, T+1): # 테스트케이스를 T번 반복
    N, M = map(int, input().split())   # 변수의 개수가 정해져 있으니까 > map
    A_nums = list(map(int, input().split()))    # 수열 A
    B_nums = list(map(int, input().split()))    # 수열 B # 여러 개의 정수를 리스트에 저장해서 변수에 넣음

    B_index = 0  # B 인덱스의 초기값을 지정해줌 # B 수열에서 현재 비교중인 위치(인덱스)

    # A를 가지고 와서 순서대로 비교 
    for i in range(N):     # A의 길이(N)만큼 반복문 진행 
        if A_nums[i] == B_nums[B_index]:
            B_index += 1        # 두 숫자가 같으면 B인덱스 값 추가해서 B의 다음 정수와 비교  

            if B_index == M:    # B의 모든 원소를 순서대로 찾았다면 
                break           # B 인덱스 값과 M의 값이 같으면 가장 가까운 반복문(for문) 탈출

    # 판별 
    if B_index == M:    # B의 모든 원소를 찾은 경우
        print(f'#{tc} YES')
    else:               # 하나라도 못 찾은 경우 
        print(f'#{tc} NO')

# 첫 번째 if문이 true -> b인덱스+1 -> 두 번째 if문 실행
    # 두 번째 if문이 true면 break로 for문 종료 -> 판별 if문 실행
    # 두 번째 if문이 false면 for문으로 돌아가서 i+1
# 첫 번째 if문이 false -> for문으로 돌아가서 i+1