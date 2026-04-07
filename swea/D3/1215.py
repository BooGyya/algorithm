# 1215 - 회문1

T=10

def 회문검사기(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input()))for _ in range(8)]
    count =0
    
    # 가로 검사 
    for r in range(8):
        for start in range(8 - N +1):
            word = arr[r][start:start+N]
            if 회문검사기(word):
                count+=1
    
    # 세로 검사 
    for c in range(8):
        for start in range(8 - N + 1):
            word  = []
            for r in range(start, start+N):
                word.append(arr[r][c]) 

            if 회문검사기(word):
                count+=1
    print(f"#{tc} {count}")