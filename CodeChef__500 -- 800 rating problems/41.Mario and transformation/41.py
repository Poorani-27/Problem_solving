# cook your dish here
T = int(input())
for _ in range(T):
    X = int(input())
    if X %3 ==0 :
        print("NORMAL")
    elif X %3==1:
        print("HUGE")
    else:
        print("SMALL")
    
    