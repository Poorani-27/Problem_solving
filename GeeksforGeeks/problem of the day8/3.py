#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        # code here
        count = 0
        freq = {}
        
        # Count frequencies of sums of pairs from mat1
        for i in range(n):
            for j in range(n):
                pair_sum = mat1[i][j]
                if pair_sum in freq:
                    freq[pair_sum] += 1
                else:
                    freq[pair_sum] = 1
        
        # Check pairs from mat2 and increment count if the complement exists in freq
        for i in range(n):
            for j in range(n):
                complement = x - mat2[i][j]
                if complement in freq:
                    count += freq[complement]
        
        return count
