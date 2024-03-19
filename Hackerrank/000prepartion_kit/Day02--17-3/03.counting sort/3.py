def countingSort(arr):
    max_val = 100 
    count = [0] * max_val
    
    for i in arr:
        count[i] += 1
    
    return count

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(' '.join(map(str, result)))
