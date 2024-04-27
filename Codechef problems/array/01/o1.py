t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    mini =min(a)
    count= 0
    for i in a :
        if i > mini :
            count +=1
    print(count)
           
    t -= 1
