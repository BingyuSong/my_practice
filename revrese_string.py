class Solution(object):
    def reverseString(self, s):
    	return(s[::-1])
if __name__=='__main__':
	ans=Solution()
	print(ans.reverseString('hello'))