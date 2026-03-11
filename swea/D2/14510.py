# 14510 - 나무 높이

'''
홀수 날 +1
짝수 날 +2
최소 날짜 수 구하기
'''

T = int(input())

for tc in range(1, T+1):
    # 나무 개수
    N = int(input())
    # 각 나무의 높이
    heights = list(map(int, input().split()))
    # 가장 큰 나무의 높이
    max_height = max(heights)
    # 가장 적게 쓴 날짜
    answer = 0
    
    one_count = 0
    two_count = 0
    for height in heights:
        if height == max_height:
            continue
        one_count += (max_height-height) % 2 # 0 또는 1
        two_count += (max_height-height) // 2 # 최대한 2 블럭 확보
    
    # 최대한 교차할 수 있을 때까지 > 2블럭 수와 1블럭 수의 차이가 가장 작을 때까지
    while two_count - one_count > 1:
        two_count -= 1
        one_count += 2
    
    if one_count > two_count:
        answer = 2*one_count-1
    else:
        answer = 2*two_count
    
    print(f'#{tc} {answer}')

