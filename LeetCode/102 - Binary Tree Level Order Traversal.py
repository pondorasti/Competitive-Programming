# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def bfs(node: Optional[TreeNode], depth = 0):
            if node is None:
                return 
            
            # append sub-array
            if len(ans) < depth + 1:
                ans.append([])
            
            # add new answer
            ans[depth].append(node.val)
            
            
            # traverse children
            bfs(node.left, depth + 1)
            bfs(node.right, depth + 1)
        
        bfs(root)
        return ans
                