# cook your dish here
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    approved = X * (50/100)
    if Y >=approved:
        print("YES")
    else :
        print("NO")