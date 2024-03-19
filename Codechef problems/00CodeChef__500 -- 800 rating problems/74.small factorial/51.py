t=int(input())
for _ in range (t):
    num = int(input())
    factorial = 1

    if num < 0:
        print("Factorial does not exist for negative numbers.")
    elif num == 0:
        print(1)
    else:
        for i in range(1, num + 1):
            factorial *= i
        print(factorial)

