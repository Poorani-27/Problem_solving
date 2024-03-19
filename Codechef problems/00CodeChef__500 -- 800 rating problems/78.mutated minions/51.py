# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in a: 
        i += k
        b.append(i)
    count=0
    for i in b:
        if i%7==0:count +=1
    print(count)