class TreeNode(object):
    def __init__(self, x):
    	self.val = x
    	self.left = None
    	self.right = None

class Solution(object):
    def isSameTree(self, p, q):
    	# A and B and C 只有全是True 才是 True 
    	if p and q: 
    		return p.val==q.val and  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    	return p is q