# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        results= []
        res1 = []        
        self.inorder_traverse(root1, res1)
    
        res2 = []        
        self.inorder_traverse(root2, res2) 
        i = 0
        j = 0
        
        while i < len(res1) and j < len(res2):
            if res1[i] < res2[j]:
                results.append(res1[i])
                i += 1
            else:
                results.append(res2[j])
                j += 1
        
        while i < len(res1):
            results.append(res1[i])
            i += 1
                
        while j < len(res2):
            results.append(res2[j])
            j += 1

        return results
                
    def inorder_traverse(self, root, results):
        if not root:
            return
        
        self.inorder_traverse(root.left, results)
        results.append(root.val)
        self.inorder_traverse(root.right, results)
        