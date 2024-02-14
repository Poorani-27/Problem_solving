# cook your dish here
T = int(input())
for _ in range(T):
    X,Y,Z =map(int,input().split())
     #school X
     #student Y
     # passed student Z
    #to calculate percentage
    S=X*Y
    
    pass_percentage = (Z/S)*100
    if pass_percentage > 50:
        print("Yes")
    else : 
        print("No")

    