# A marathon is being organised in the hilly terrains of Ladakh. Since the region is sparsely populated, 
# care must be taken to ensure that no runner gets lost along the route. 
# There are multiple checkpoints along the route, and each checkpoint must connect to only one downstream checkpoint. 
# However, since there were multiple teams working on setting up the connections, there have been some mistakes, 
# and there are some checkpoints which are connecting to more than one downstream checkpoints.
# The checkpoint details are given, with each checkpoint represented by a random integer. 
# Write a program to identify the checkpoints which are connecting to more than one downstream checkpoirits, 
# and print their sum as the output.

# The route details are given as a list of relations between the Starting point and the checkpoints. 
# The relations are indicated as L, R, LL, LR... and so on, 
# where the checkpoint is to the left (L), or left-left (LL) or right-left (RL) to the Starting point.

# Read the input from STDIN and print the output to STDOUT. 
# Do not print arbitrary strings anywhere in the program, as these contribute to the output and test cases will fail.

# Constraint:
# 3 < z Number of checkpoints c = 100

# Input Format:
# The first line of input contains an integer, N, the number of checkpoints in the route, including the Starting point
# The second line of input contains an integer, which is the Starting point of the route.
# The next N-1 lines of input contain a string, S and an integer, X separated by a single white space, 
# where X is a checkpoint along the route and S is the relation between the Starting point and X.

# Output Format:
# The output contains an integer which is the sum of all checkpoints connecting to more than one downstream checkpoint.
# Sample Input1:
# 6
# 70
# L50
# LR 65
# LRL 60
# LRR 68
# LRRL 69

# Sample Output1:
# 65


# Explanation 1
# The marathon route can be represented as below. Starting point is 70
#  70
# /
# 50
#  \
#  65
#  /\
# 60 68
#    /
#   69

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


answer = 0


def postorder(root):
    global answer

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    # Print postorder traversal (optional)
    print(root.data, end=" ")

    # If a node has more than one downstream checkpoint
    if root.left is not None and root.right is not None:
        answer += root.data


def main():
    global answer

    n = int(input())
    root_value = int(input())

    root = Node(root_value)
    head = root

    for _ in range(n - 1):
        path, value = input().split()
        value = int(value)

        curr = head

        for ch in path:
            if ch == 'L':
                if curr.left is None:
                    curr.left = Node(0)   # Temporary value
                curr = curr.left
            else:  # R
                if curr.right is None:
                    curr.right = Node(0)
                curr = curr.right

        curr.data = value

    postorder(head)
    print()
    print(answer)


if __name__ == "__main__":
    main()

# O(N × H) time (where H is the maximum path length) and O(N) space

# class Node:
#     def __init__(self, val=0):
#         self.data = val
#         self.left = None
#         self.right = None


# def postorder(root):
#     if root is None:
#         return 0

#     left = postorder(root.left)
#     right = postorder(root.right)

#     ans = left + right

    # Node having more than one downstream checkpoint
#     if root.left is not None and root.right is not None:
#         ans += root.data

#     return ans


# def solve():
#     n = int(input())
#     root_value = int(input())

#     root = Node(root_value)

#     for _ in range(n - 1):
#         path, value = input().split()
#         value = int(value)

#         curr = root

#         for ch in path:
#             if ch == 'L':
#                 if curr.left is None:
#                     curr.left = Node()
#                 curr = curr.left
#             else:  # 'R'
#                 if curr.right is None:
#                     curr.right = Node()
#                 curr = curr.right

#         curr.data = value

#     print(postorder(root))