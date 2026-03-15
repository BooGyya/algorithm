# 1486 - 장훈이의 높은 선반

def dfs(i, height):
    global answer

    # 가지치기
    # 현재까지 쌓은 탑의 높이가 이미 찾은 최소값보다 크면 중단
    if height >= answer:
        return

    # 정답 업데이트 - 기저 조건 1
    # 탑의 높이가 B 이상이면, 더 작은 값 저장 
    if B <= height:
        answer = min(height, answer)
        return
    
    # 모든 점원 확인 완료 - 기저 조건 2
    if i == N:
        return
    
    # 재귀 1. i번째 점원의 키를 더함 (포함)
    dfs(i + 1, height + S[i])
    # 재귀 2. i번째 점원의 키를 더하지 않음 (미포함)
    dfs(i + 1, height)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # N: 점원 수, B: 목표 높이
    S = list(map(int, input().split())) # S: 점원들의 키 리스트
    answer = float('inf')

    dfs(0,0)    # 인덱스 0번 점원, 시작 높이 0

    answer = answer - B

    print(f'#{tc} {answer}')