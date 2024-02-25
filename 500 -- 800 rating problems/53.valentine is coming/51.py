# cook your dish here
T =int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if X <Y :
        print(0)
    else :
        print(X//Y)