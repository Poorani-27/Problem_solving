t=int(input())
for _ in range(t):
    a,b,x=map(int,input().split())
    c=b-a
    ans=c//x
    print(ans)