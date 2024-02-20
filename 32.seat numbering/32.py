# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    if 1<=N<=10 :print("lower double") 
    elif  16<=N<=25: print("upper double")
    elif 11<=N<=15 : print("lower single")
    else: print("upper single")