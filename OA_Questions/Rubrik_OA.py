# Rubrik is processing a string consisting of three types of symbols: A, B, and C.

# You are given a string S of length N. 
# The system allows certain adjacent symbols to be swapped according to the following rules:

# Allowed Operations

# In one operation, you may perform exactly one of the following transformations:

# Replace an adjacent occurrence of AB with BA.
# Replace an adjacent occurrence of BC with CB.

# In other words:

# AB -> BA

# BC -> CB

# Only adjacent characters can participate in an operation.

# Your task is to determine the maximum number of operations that can be performed on the string.

# It can be proven that the maximum number of operations is always finite.

def max_operations(S):
    # Initialize a counter for the number of operations
    operations = 0
    
    # Convert the string to a list for easier manipulation
    S = list(S)
    
    # Continue performing operations until no more can be done
    while True:
        made_change = False
        
        # Check for AB -> BA
        for i in range(len(S) - 1):
            if S[i] == 'A' and S[i + 1] == 'B':
                S[i], S[i + 1] = S[i + 1], S[i]  # Swap A and B
                operations += 1
                made_change = True
                break  # Restart the loop after a change
        
        if made_change:
            continue
        
        # Check for BC -> CB
        for i in range(len(S) - 1):
            if S[i] == 'B' and S[i + 1] == 'C':
                S[i], S[i + 1] = S[i + 1], S[i]  # Swap B and C
                operations += 1
                made_change = True
                break  # Restart the loop after a change
        
        if not made_change:
            break  # No more changes can be made
    
    return operations

# Example usage:
S = "BACB"
print(max_operations(S))