class Solution(object):
    def canWinNim(self, n):
    	if n%4: return False
    	else: return True


if __name__=="__main__":
	ans=Solution()
	print(ans.canWinNim(5))