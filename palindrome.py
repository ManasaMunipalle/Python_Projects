from itertools import combinations

def count_palindromic_subsequences(s):
    count = 0
    n = len(s)
    
    # Generate all subsequences of length 5
    for subseq in combinations(range(n), 5):
        sub_str = ''.join(s[i] for i in subseq)
        if sub_str == sub_str[::-1]:  # Check if it's a palindrome
            count += 1
    
    return count

# Example usage:
s = "11001101"
print(count_palindromic_subsequences(s))  # Output: Count of palindromic subsequences of length 5
