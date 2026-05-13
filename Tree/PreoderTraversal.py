#Leetcode 144. Binary Tree Preorder Traversal

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.traversal(root,l)
        return l

    def traversal(self,root,l):
        if(root==None):
            return
        l.append(root.val)
        self.traversal(root.left,l)
        self.traversal(root.right,l)