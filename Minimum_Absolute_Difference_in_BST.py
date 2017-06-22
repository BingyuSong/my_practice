# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
    	self.val = x
    	self.left = None
    	self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        def bst(node,l=[]):
            # l.append(node.val)
            if node.left: bst(node.left,l)
            l.append(node.val)
            if node.right:bst(node.right,l)
            return l
        ans=bst(root)
        return min([abs(a-b) for a,b in zip(ans, ans[1:])])


