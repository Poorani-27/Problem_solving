# cook your dish here
T = int(input())
for i in range (T):
    B1,B2,B3=map(int,input().split())
    full = 0
    empty = 0
    a=[B1,B2,B3]
    for i in a:
        if i == 0 :
            empty +=1
        else :
            full +=1 
    if empty > full:
        print("Water filling time")
    else :
        print("Not now")