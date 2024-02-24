# cook your dish here
T = int(input())
for _ in range(T):
    X,Y,Z = map(int,input().split())
    # x remaining levels Y min to complete z break after 3 levels
    total=X*Y
    if X <=3 :
        print(total)
    else :
        a = X //3
        if X % 3 !=0: print(total +(a*Z))
        else : print(total +((a-1)*Z))