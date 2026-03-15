# 2565 - 전깃줄

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

# 시작점으로 sort를 한 후 도착점 수열에 대해서 가장 긴 부분 증가수열을 찾기
# 그것이 교차하지 않는 전선을 고른 것이기에
# LIS 알고리즘 활용 -> 최장 증가 부분 수열
answer = [lines[0][1]]
for i in range(1, N):
    candidate = lines[i][1]
    if answer[-1] < candidate:
        answer.append(candidate)
    else:
        idx = bisect_left(answer, candidate)
        answer[idx] = candidate

print(N-len(answer))