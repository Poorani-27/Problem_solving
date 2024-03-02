# cook your dish here
t=int(input())
for _ in range (t):
    x,y,r =map(int,input().split())
    r=r//30
    total_stick = r+x 
    plate= total_stick//y 
    count =0
    if total_stick%y !=0 : count+=1
    count = count + plate
    print (count)
