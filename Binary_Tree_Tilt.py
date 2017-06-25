# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
    	self.val = x
    	self.left = None
    	self.right = None

class Solution(object):
	def findTilt(self,root):
		self.ans=0
		def tile_node(node):
			if not node: return 0
			left, right = tile_node(node.left),tile_node(node.right)
			# global variable self.ans
			self.ans+=abs(left-right)
			return node.val+left+right
		tile_node(root)
		return self.ans







if __name__=="__main__":
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	d=TreeNode(4)
	a.left=b
	a.right=d
	b.right=c
	ans = Solution()
	# print(a.val)
	print(ans.findTilt(a))
