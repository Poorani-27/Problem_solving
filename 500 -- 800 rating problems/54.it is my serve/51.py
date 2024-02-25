T = int(input())
for _ in range(T):
    P,Q = map(int,input().split())
    if (P+Q)%4==0 or (P+Q)%4==1 :print("Alice")
    else:print("Bob")