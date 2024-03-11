n=int(input())
a=list(map(int,input().split()))
positive=[]
negative=[]
zero=[]
for i in a:
    if i>0:
        positive.append(i)
    elif i<0:
        negative.append(i)
    else:
        zero.append(i)
positive_porportion=len(positive)/n
negative_porportion=len(negative)/n
zero_porportion=len(zero)/n
print(positive_porportion)
print(negative_porportion)
print(zero_porportion)