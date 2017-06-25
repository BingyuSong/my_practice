class TreeNode(object):
    def __init__(self, x):
    	self.val = x
    	self.left = None
    	self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
    	if not root: return 0
    	if root.left and  not root.left.left and not root.left.right:
    		return root.left.val+self.sumOfLeftLeaves(root.right)
    	return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)




if __name__=="__main__":
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	d=TreeNode(4)
	a.left=b
	a.right=d
	b.left=c
	ans = Solution()
	# print(a.val)
	print(ans.sumOfLeftLeaves(a))



