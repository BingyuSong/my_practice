class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
	def mergeTrees(self, t1, t2):
		if t1 and t2:
			ans1 = TreeNode(t1.val+t2.val)
			ans1.left= self.mergeTrees(t1.left,t2.left)
			ans1.right= self.mergeTrees(t1.right,t2.right)
			return ans1
		else:
			return t1 or t2

if __name__=='__main__':
	t1 = TreeNode(1)
	t11=TreeNode(3)
	t12=TreeNode(2)
	t13=TreeNode(5)
	t1.left=t11
	t1.right=t12
	t11.left=t13
	t2 = TreeNode(2)
	t21=TreeNode(1)
	t22=TreeNode(3)
	t23=TreeNode(4)
	t24 = TreeNode(7)
	t2.left=t21
	t2.right=t22
	t21.right=t23
	t22.right = t24
	ans = Solution()
	print((ans.mergeTrees(t1,t2)).val)