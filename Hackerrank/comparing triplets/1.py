a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_count=0
b_count=0
for i in range(len(a)):
    if a[i]>b[i]:
        a_count +=1
    elif a[i] < b[i]:
        b_count +=1
    else:
        a_count=a_count
        b_count=b_count
print(a_count,b_count)