from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node:

            def deep_copy(new_node, node, node_reference):
                node_reference[node.val] = new_node
                for neighbor in node.neighbors:
                    if neighbor.val in node_reference:
                        new_node.neighbors.append(node_reference[neighbor.val])
                    else:
                        new_neighbor = Node(neighbor.val)
                        deep_copy(new_neighbor, neighbor, node_reference)
                        new_node.neighbors.append(new_neighbor)
                return new_node

            node_reference = {}
            new_node = Node(node.val)
            return deep_copy(new_node, node, node_reference)
        else:
            return node


# Test cases
def test_clone_graph():
    # Example 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned_node1 = solution.cloneGraph(node1)

    # Check if the cloned graph is correct
    assert cloned_node1.val == node1.val
    assert cloned_node1.neighbors[0].val == node2.val
    assert cloned_node1.neighbors[1].val == node4.val

    # Example 2
    node1 = Node(1)
    solution = Solution()
    cloned_node1 = solution.cloneGraph(node1)

    # Check if the cloned graph is correct
    assert cloned_node1.val == node1.val
    assert not cloned_node1.neighbors  # No neighbors

    print("All test cases passed!")


# Run the test cases
test_clone_graph()
