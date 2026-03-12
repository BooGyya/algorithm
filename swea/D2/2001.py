# 2001 - 파리퇴치

T = int(input())
 
for tc in range(1, T+1):
    answer = 0
     
    N, M = map(int, input().split())  # M은 파리채의 크기
    files = [list(map(int, input().split())) for _ in range(N)]
 
    for r in range(N-M+1):
        for c in range(N-M+1):
             
            # 기준점(r, c)이 잡혔음
            temp_sum = 0
            for dr in range(M):
                for dc in range(M):
                    temp_sum += files[r+dr][c+dc]
 
            if temp_sum > answer:
                answer = temp_sum
 
    print(f"#{tc} {answer}")