# 4837 - 부분집합의 합

def dfs(num, cnt, current_sum):
    global answer
    
    # 1. 가지치기: 현재 합이 이미 K를 넘었거나, 사용한 원소 개수가 N을 넘은 경우
    if current_sum > K or cnt > N:
        return
    
    # 2. 기저 조건: 원소 개수가 N개일 때
    if cnt == N:
        if current_sum == K:
            answer += 1
        return
    
    # 3. 모든 원소(1~12)를 다 확인한 경우
    if num > 12:
        return

    # 현재 숫자(num)를 포함하는 경우
    dfs(num + 1, cnt + 1, current_sum + num)
    # 현재 숫자(num)를 포함하지 않는 경우
    dfs(num + 1, cnt, current_sum)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    answer = 0
    
    # 숫자 1부터 탐색 시작
    dfs(1, 0, 0)
    
    print(f"#{tc} {answer}")