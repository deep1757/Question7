t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    ans=[]
    for j in b:
        if a.count(j)>=4:
            ans.append(j)
            ans.append(j)
        if a.count(j)>=2:
            ans.append(j)
    ans.sort()
    if len(ans)>1:
        print(ans[-1]*ans[-2])
    else:
        print(-1)