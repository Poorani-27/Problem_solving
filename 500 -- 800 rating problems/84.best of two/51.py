# cook your dish here
t=int(input())
for _ in range(t):
    a1,a2,a3,b1,b2,b3=map(int,input().split())
    a=(a1+a2+a3)-min(a1,a2,a3)
    b=(b1+b2+b3)-min(b1,b2,b3)
    if a>b:print("Alice")
    elif b>a:print("Bob")
    else:print("Tie")
    