from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs_counter(root, node_max_length):
            if not root:
                return 0

            left_max_length = dfs_counter(root.left, node_max_length)
            right_max_length = dfs_counter(root.right, node_max_length)

            # Calculate the diameter and update node_max_length
            node_max_length[0] = max(
                node_max_length[0], left_max_length + right_max_length
            )

            # Return the maximum depth of the subtree rooted at 'root'
            return 1 + max(left_max_length, right_max_length)

        node_max_length = [0]  # To store the maximum diameter

        dfs_counter(root, node_max_length)

        return node_max_length[0]


# Test cases
if __name__ == "__main__":
    s = Solution()

    # Create the following tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert s.diameterOfBinaryTree(root) == 3  # Diameter is the path 4 -> 2 -> 1 -> 3

    # Create a single-node tree
    root = TreeNode(1)
    assert s.diameterOfBinaryTree(root) == 0  # Diameter of a single-node tree is 0

    # Create a tree with only left subtrees
    #     1
    #    /
    #   2
    #  /
    # 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert s.diameterOfBinaryTree(root) == 2  # Diameter is the path 3 -> 2 -> 1

    # Create a tree with only right subtrees
    #   1
    #    \
    #     2
    #      \
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert s.diameterOfBinaryTree(root) == 2  # Diameter is the path 1 -> 2 -> 3

    print("All test cases passed!")
