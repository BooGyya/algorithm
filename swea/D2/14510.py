# 14510 - 나무 높이

'''
홀수 날 +1
짝수 날 +2

최소 날짜 수 구하기

1. 가장 큰 나무의 키 구하기

'''

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    length_gap = []

    max_length = max(arr)   # 가장 키 큰 나무 

    # 가장 키가 큰 나무와 나머지 나무들의 갭 구하기
    for i in arr:
        length_gap.append(max_length-i)
    
    

    


    print(f'#{tc} {result}')

