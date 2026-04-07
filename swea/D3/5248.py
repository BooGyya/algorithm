# 5248 - 그룹 나누기

T = int(input())

def find_parent(a):
    if parents[a] == a:
        return a
    
    # 경로 압축
    parents[a] = find_parent(parents[a])
    return parents[a]

def union(a,b):
    # 그 그룹의 대장을 찾기
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    # 사이클이 존재함 
    if parent_a == parent_b:
        return
    
    # 사이클이 존재하지 않음 (부모가 더 작은 거에다가 합침)
    if parent_a > parent_b:
        parents[parent_a] = parent_b

    # b가 더 클 때
    else :
        parents[parent_b] = parent_a


for tc in range(1, T+1):
    N, M = map(int, input().split())    # 노드의 수, 입력관계의 수
    connections = list(map(int, input().split()))

    parents = [i for i in range(N+1)]  # 부모들의 집합

    # i번째 : 0번부터 시작 (총 M번)
    for i in range(0, M*2, 2):
        # 연결 > union
        union(connections[i], connections[i+1])

    # set으로 세어주기 위해서는?
    # > 경로 압축이 되었다는 가정이 필요(안 되어있다면 모든 노드에 대해 경로 압축 필요)
    # for i in range(1, N+1):
    #     find_parent(i)
    # answer = len(set(parents)) - 1

    # 경로 압축이 안 되어있어도 그룹의 수를 세려면?
    # 각 그룹의 대장만 세어주기
    answer = 0
    for i in range(1, N+1):
        if i == parents[i]:
            answer += 1

    print(f'#{tc} {answer}')