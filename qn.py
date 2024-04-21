def isKthBitSet(n, k):
    n=int(n)
    k=int(k)
    n=(bin(n))
    if len(n)<=k:
        if n[k] == 1:
            return "YES"
    else:
        return "NO"

n, k = map(int, input().split())
print(isKthBitSet(n, k))
