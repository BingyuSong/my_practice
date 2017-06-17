class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
    def tree2str(self, t):
    	def preorder(root):
    		if root is None:return ''
    		s=str(root.val)
    		l=preorder(root.left)
    		r=preorder(root.right)
    		if r=='' and l=='': return s
	    	elif l=='':s+="()"+'('+r+')'
	    	elif r=='': s+='('+l+')'+'()'
	    	else: s+='('+l+')'+'('+r+')'
	    	return s
	    return preorder(t)




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
	print(ans.tree2str(a))