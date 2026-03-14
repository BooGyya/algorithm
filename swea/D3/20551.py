# 20551 - 증가하는 사탕 수열

T = int(input())

for tc in range(1, T+1):
    A, B, C  = map(int, input().split())

    # 1. 문제 조건이 불가능한 케이스
    if B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    # 2. B = C -1 / A = B - 1로 만들면 된다.
    eat_count = 0

    # B 상자
    if B >= C:
        eat_count += B - (C - 1)    # 높이의 차이 + 1 만큼 먹는다
        B = C - 1

    # A 상자
    if A >= B:
        eat_count += A - (B - 1)    # 높이의 차이 + 1 만큼 먹는다
        A = B - 1

    print(f'#{tc} {eat_count}')
