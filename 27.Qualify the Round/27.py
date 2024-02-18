# cook your dish here
T = int(input())
for _ in range(T):
    X,A,B = map(int,input().split())
    score = (A*1)+(B*2) 
    if X <=score :print("Qualify")
    else:print("NotQualify")