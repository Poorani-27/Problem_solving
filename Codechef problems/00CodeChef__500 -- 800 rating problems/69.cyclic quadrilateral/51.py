# cook your dish here
t = int(input())
for _ in range (t):
    a,b,c,d = map(int,input().split())
    if a+c ==180 or b+d == 180 :print("Yes")
    else:print("No")