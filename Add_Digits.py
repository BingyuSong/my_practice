class Solution(object):
    def addDigits(self, num):
    	if num==0: 
    		return 0
    	elif num%9==0:
    		return 9
    	else: return num%9

if __name__=="__main__":
	ans=Solution()
	print(ans.addDigits(8))