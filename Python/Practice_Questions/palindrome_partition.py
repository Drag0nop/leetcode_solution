def partition(s):
    res = []
    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:  # Check if the substring is a palindrome
                path.append(substring)
                backtrack(end, path)
                path.pop()  # Backtrack
    backtrack(0, [])
    return res

# Example usage:
s = "aab"
print(partition(s))  # Output: [['a', 'a', 'b'], ['aa', 'b']]