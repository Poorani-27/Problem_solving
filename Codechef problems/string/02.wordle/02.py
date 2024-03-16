# cook your dish here
n=int(input())
for _ in range (n):
    a=input()
    b=input()
    answer=""
    for i in range(len(a) ):
        if a[i] ==b[i]:
            answer +="G"
        else :
            answer +="B"
    print(answer)