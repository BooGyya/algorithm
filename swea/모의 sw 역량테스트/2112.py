# 2112 - 보호 필름

''' 
"어디 단어가 들어갈 수 있을까" 유사 문제 

<부분 집합 사용>
N = 3
numbers = [1,2,3,4,5]

# count : 지금까지 고른 숫자 개수
# idx : 다음의 탐색 시작 인덱스 
def comb(count, idx):
    if count == N:
        # 다 골랐을 때 작업 
        return
    
    for i in range(idx, 5):
        comb(count+1, i+1)

comb(0,0)
'''

def test_film():
    # 통과 시 True
    # 실패 시 False

    for c in range(W):  # 열 우선 순회 
        count = 0
        before = -1     # 이전 값 (없는 값을 할당해야함, 0 or 1은 안됨)

        for r in range(D):  # 행 순회 
            if films[r][c] != before:
                count = 1
            else:
                count += 1
                if count >= K:  # K개 이상
                    break
            before = films[r][c]

        # 실패 시 중도하차 (해당 열을 다 돌았을 때 해야 함) 
        if count < K:   # K개 미만 
            return False

    # 실패를 안 했을 때는 True
    return True

def comb(count, idx):
    global answer

    if test_film():
        answer = count

    if count >= answer - 1: # 백트래킹
        return

    # count < answer - 1 일 때
    for i in range(idx, D):
        backup = films[i]
        films[i] = A
        comb(count+1, i+1)
        films[i] = B
        comb(count+1, i+1)
        films[i] = backup

T = int(input())
A = [0]*20  # 얕은 복사
B = [1]*20

for tc in range(1, T+1):
    D, W, K = map(int, input().split()) 
    films = [list(map(int, input().split())) for _ in range(D)] # 필름 정보 (전역변수)
    answer = K  # 약품의 최소 투입 횟수

    comb(0,0)

    print(f'#{tc} {answer}')