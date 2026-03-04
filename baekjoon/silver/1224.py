# 1244 - 스위치 켜고 끄기

'''
switch_num > 스위치 개수
switch_info > 스위치의 상태 (꺼짐 0, 켜짐 1)
students > 학생수

1. 남학생(1)이면
    받은 수에 대한 배수의 스위치 바꿈
2. 여학생(2)이면 
    받은 수에 대한 대칭인 스위치가 같으면 스위치 바꿈

'''
switchs = int(input())   # 스위치 개수

switch_info = list(map(int, input().split()))   # 스위치의 상태 (꺼짐 0, 켜짐 1)
students = int(input()) # 학생수 
result = []     # 마지막 스위치 상태 

person_info = []    # 학생에 대한 정보받기 (0 성별, 1 학생이 받은 수)
for _ in range(students):
    info = list(map(int, input().split()))
    person_info.append(info)

for gender in range(students):  # 학생수만큼 반복
    if person_info[gender][0] == 1: # 남학생일 때 
        n = person_info[gender][1]  # 받은 수



    else:   # 여학생일 때



    
print(*result)
