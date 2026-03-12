# 1952 - 수영장
# DP 활용

'''
dp : 부분문제를 바탕으로 전체 문제를 해결함 
'''

T = int(input())
for tc in range(1, T+1):
    # day_cost: 1일, month_cost: 1달, quater_cost: 3달, answer: 1년권 가격
    day_cost, month_cost, quater_cost, answer = map(int, input().split())   
    plans = list(map(int, input().split()))
    
    # dp[i] : i월까지 수영장을 이용했을 때의 최소 비용
    dp = [0]*12
    dp[0] = min(month_cost, day_cost*plans[0])  # 1월: 1달권 vs (1일권 * 이용일수) 

    # 2월 ~ 11월까지 순회 
    for current in range(1, 12):
        dp[current] = dp[current-1] + min(month_cost, day_cost*plans[current])  # 이전 달까지의 최적 비용 + 이번 달 비용
        
        # 3달권 vs (1일권 or 1달권)
        if current >= 2:
            dp[current] = min(dp[current], dp[current-3]+quater_cost)   # 현재 달까지의 최적 비용 vs (3개월 전까지의 최적 비용 + 3달권 가격)
    
    # 1월 ~ 11월 가격 vs 연간권 
    answer = min(answer, dp[11])

    print(f'#{tc} {answer}')
