# cook your dish here
t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    d = [a,b,c]
    d=sorted(d)
    ans=d[1]
    print(ans)
    