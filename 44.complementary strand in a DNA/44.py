T = int(input())
for _ in range (T):
    N = int(input())
    S = input()
    Complement = {"A":"T","T":"A","C":"G","G":"C"}
    answer = ""
    for s in S :
        answer +=Complement[s]
    print(answer)