# cook your dish here
T = int(input())
for _ in range(T):
    A,B,C = map(int,input().split())
    final_score =max(A,B,C)
    print(final_score)