class Solution(object):
    def longestCommonPrefix(self, strs):
    	import os
    	return os.path.commonprefix(strs)
s = Solution()
ans = s.longestCommonPrefix([[3,2,1], [3,2,1,4,5], [3,2,1,8,9], [3,2,1,5,7,8,9]])
print(ans)