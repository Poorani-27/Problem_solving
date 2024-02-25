# cook your dish here
T = int(input())
for i in range (T):
    a,b,c = map(int,input().split())
    avg = (a+b)/2 
    if avg > c :
        print("YEs")
    else :
        print ("no")