# 1486 - 장훈이의 높은 선반

def comb(idx,total):
    global answer
    if B<=total<answer:
        answer=total
        return
    if idx==N:
        return

    if total>=answer or total+remain[idx]<B:
        return   
    comb(idx+1,total+arr[idx])
    comb(idx+1,total)


T=int(input())
for tc in range(1,T+1):
    N,B=map(int,input().split())
    arr=list(map(int,input().split()))
    answer=sum(arr)
    remain=[0]*(N+1)
    for i in range(len(arr)-1,-1,-1):
        remain[i]=remain[i+1]+arr[i]
    comb(0,0)
    print(f'#{tc} {answer-B}')