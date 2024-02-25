# cook your dish here
T = int(input())
for _ in range(T):
    X=int(input())
    if X %5 !=0 and X%10 !=0:print(-1)
    else : 
        A=X//10 
        B=X//5
        if A*10==X :print(A)
        else : 
            C = (X-(A*10))//5
            print(A+C)
        