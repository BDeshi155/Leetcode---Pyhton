# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.matchingSubtree = 0  # Initialize the count of subtrees with matching averages.

    def calculateSubtreeValues(self, currentNode):
        if currentNode is None:
            return 0, 0

        leftSubtree = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)

        sumOfValues = leftSubtree[0] + rightSubtree[0] + currentNode.val
        numberOfNodes = leftSubtree[1] + rightSubtree[1] + 1

        if sumOfValues // numberOfNodes == currentNode.val:
            self.matchingSubtree += 1

        return sumOfValues, numberOfNodes

    def averageOfSubtree(self, root_list):
        # Create the binary tree using TreeNode instances
        root = self.buildTree(root_list)

        self.calculateSubtreeValues(root)
        return self.matchingSubtree

    def buildTree(self, values):
        if not values:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while i < len(values):
            current = queue.pop(0)

            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)

            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)

            i += 1

        return root

sol = Solution()
res = sol.averageOfSubtree([4, 8, 5, 0, 1, None, 6])  # Correct the use of None
print(res)