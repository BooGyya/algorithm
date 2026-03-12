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


T = int(input())

for tc in range(1, T+1):
    day_fee, month_fee, quater_fee, answer = map(int, input().split())
    # answer : 이 문제는 최대값이 정해져있음 -> 1년(연간이용권)
    days = list(map(int, input().split())) # 수영 계획

    dfs(0, 0) # 1월의 수영계획은 0번 인덱스 # 누적 요금은 0
    
    print(f"#{tc} {answer}")


