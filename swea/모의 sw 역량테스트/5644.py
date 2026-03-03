# 5644 - 무선충전

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    AP1 = list(map(int, input().split()))
    AP2 = list(map(int, input().split()))
    AP3 =list(map(int, input().split()))

    print(f'#{tc} {}')