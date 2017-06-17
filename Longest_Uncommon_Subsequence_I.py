class Solution(object):
    def findLUSlength(self, a, b):
    	return a!=b and max(len(a),len(b)) or -1


if __name__=="__main__":
	ans=Solution()
	a='aba'
	b='bcb'
	print(ans.findLUSlength(a,b))