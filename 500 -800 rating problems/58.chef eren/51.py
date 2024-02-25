# cook your dish here
T= int(input())
for _ in range(T):
    N,A,B = map(int,input().split())
    print(B*(N%2) + (A+B)*(N//2))