n=int(input())
a=list(map(int,input().split()))
max_element = max(a)

count = 0
for i in a:
    if i== max_element : 
        count +=1
print(count)