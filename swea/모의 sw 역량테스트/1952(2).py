# 1952 - 수영장
# 완전 탐색 활용

# 단, month는 실제 월에서 -1 
# 누적요금 = fee
def dfs(month, fee):
    global answer # 전역변수 

    if fee >= answer:
        return 

    if month >= 12:
        if answer > fee: # 비용이 최소인지 확인 
            answer = fee
        return 
    
    # 일권
    dfs(month+1, fee + day_fee * days[month])
    # 월권
    dfs(month+1, fee + month_fee)
    # 3개월권 
    dfs(month+3, fee + quater_fee)


