# Tower of Hanoi: We have three rods and N disks. 
# The objective of the puzzle is to move the entire stack to another rod. 
# Initially, these discs are in the rod 1. 
# You need to print all the steps of discs movement so that all the discs reach the 3rd rod. 
# Also, find & return the total moves.
# Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. 
# Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. 
# You can only move 1 disk at a time.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {target}")
        return 1
    else:
        moves = tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from rod {source} to rod {target}")
        moves += 1
        moves += tower_of_hanoi(n - 1, auxiliary, target, source)
        return moves

# Example usage:
print(f"Total moves required: {tower_of_hanoi(3, 'A', 'C', 'B')}")