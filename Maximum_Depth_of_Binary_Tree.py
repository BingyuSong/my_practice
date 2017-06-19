class TreeNode(object):
    def __init__(self, x):
    	self.val = x
    	self.left = None
    	self.right = None

class Solution(object):
    def maxDepth(self, root):
    	if not root:
    		return 0
    	return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

if __name__=="__main__":
	a=TreeNode('1')
	b=TreeNode('2')
	c=TreeNode('3')
	d=TreeNode('4')
	a.left=b
	a.right=d
	b.right=c
	ans = Solution()
	# print(a.val)
	print(ans.maxDepth(a))