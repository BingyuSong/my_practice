class Solution(object):
    def isPalindrome(self, x):
    	if abs(x) == int(str(abs(x))[::-1]):
    		return True
    	else:
    		return False

    	# x == int(str(x)[::-1]):
    	# 	return True
    	# else:
    	# 	return False
s = Solution()
ans = s.isPalindrome(12321)