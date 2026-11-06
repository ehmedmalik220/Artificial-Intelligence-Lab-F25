# Name: Malik M Ahmad
# Roll No: 395
# Class: BSAI/3A
# LAB: 5
#
# For Lab 5 I started by tracing the game tree by hand, because I wanted to
# see how MAX picks the biggest value and MIN picks the smallest one at each
# level, and then I wrote a simple minimax function that goes down to the
# leaves and comes back up with the best value. After that I wrote alpha-beta,
# and at first I did not understand when to stop a branch, so I kept mixing up
# alpha and beta, but when I put the break on alpha greater than or equal to
# beta, the code finally made sense. My counter also gave me trouble in the
# start, because a normal number did not change inside the function, so I used
# a list to keep the count, and then the numbers matched my hand trace. The
# most surprising part was that reordering the tree changed the alpha-beta
# leaves from 6 to 8, but the final value stayed 5 in every test, so I learned
# that pruning only saves work, it never changes the best move.

import math


def minimax(depth, node, is_max, scores, target, leaves):
    if depth == target:
        leaves[0] = leaves[0] + 1
        return scores[node]
    if is_max:
        return max(
            minimax(depth + 1, node * 2, False, scores, target, leaves),
            minimax(depth + 1, node * 2 + 1, False, scores, target, leaves),
        )
    return min(
        minimax(depth + 1, node * 2, True, scores, target, leaves),
        minimax(depth + 1, node * 2 + 1, True, scores, target, leaves),
    )


def alphabeta(depth, index, is_max, scores, target, alpha, beta, leaves):
    if depth == target:
        leaves[0] = leaves[0] + 1
        return scores[index]
    if is_max:
        value = float("-inf")
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta, leaves))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for i in range(2):
        value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta, leaves))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value


def check_tree(scores, depth, label):
    min_leaves = [0]
    ab_leaves = [0]
    min_value = minimax(0, 0, True, scores, depth, min_leaves)
    ab_value = alphabeta(0, 0, True, scores, depth, float("-inf"), float("inf"), ab_leaves)
    print(label)
    print("Minimax value:", min_value, "| Leaves evaluated:", min_leaves[0])
    print("Alpha-beta value:", ab_value, "| Leaves evaluated:", ab_leaves[0])
    print("Same result:", min_value == ab_value)


tree1 = [3, 5, 2, 9, 0, 7]
d1 = math.ceil(math.log2(len(tree1)))
tree1 = tree1 + [0] * (2**d1 - len(tree1))
check_tree(tree1, d1, "Tree 1 (manual Minimax tree, padded):")

tree2 = [3, 5, 2, 9, 3, 5, 2, 9]
d2 = int(math.log2(len(tree2)))
check_tree(tree2, d2, "Tree 2 (manual alpha-beta tree):")

tree3 = [2, 9, 3, 5, 2, 9, 3, 5]
check_tree(tree3, d2, "Tree 2 reordered (worst order):")

min_leaves = [0]
ab_leaves = [0]
print("Edge case, single leaf [7]:")
print("Minimax value:", minimax(0, 0, True, [7], 0, min_leaves), "| Leaves evaluated:", min_leaves[0])
print("Alpha-beta value:", alphabeta(0, 0, True, [7], 0, float("-inf"), float("inf"), ab_leaves), "| Leaves evaluated:", ab_leaves[0])
