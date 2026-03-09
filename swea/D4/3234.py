# 준환이의 양팔저울

'''
1. 뽑은 애들 > key
2. 왼쪽에 무엇을 놓았는지 > left
3. 오른쪽에 무엇을 놓았는지 -> 알 필요 없음
dp[key][left] = val
    key의 경우의 수 : 2^n -1
    left는 연속되어 있지 않음 > 인덱스로 사용하기 적절하지 않음 > 딕셔너리로 넣음 
'''

# count : 뽑은 개수
# visited : 현재 뽑아 놓은 상태
# left / right : 왼쪽과 오른쪽의 무게

def dfs(count, visited, left, right):

    if count == N:
        return 1    # 다 골랐을 때 return 1
    
    # 현재 방문 상태에서 left 무게를 이미 세었다면
    if dp[visited].get(left):
        return dp[visited][left]

    temp = 0
    for i in range(N):
        # i번째 무게추를 골랐다면 건너뛰기 
        if visited & (1 << i): # 비트 마스킹
            continue
        
        # 안 골랐을 때
        temp += dfs(count+1, visited | (1 << i), left + weights[i], right)
        if left >= right + weights[i]:
            temp += dfs(count+1, visited | (1 << i), left, right + weights[i])

    # 현재 visited 상태에서 left 무게일 때의 경우의 수를 반환
    dp[visited][left] = temp
    return dp[visited][left]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))

    dp = [{} for _ in range(2**N)] # 0 ~ (2^n)-1까지

    answer = dfs(0, 0, 0, 0)
    
    print(f'#{tc} {answer}')