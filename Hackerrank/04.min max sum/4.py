n=list(map(int,input().split()))
min_element= min(n)
max_element =max(n)
min_sum=sum(n)-min_element
max_sum=sum(n)-max_element
print(max_sum,min_sum)