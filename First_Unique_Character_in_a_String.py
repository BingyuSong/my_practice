from collections import *

class Solution(object):
    def firstUniqChar(self, s):
    	minI=99999
    	dic=Counter(s)
    	for index, test in enumerate(s):
    		if dic[test]==1: minI=min(minI,index)
    	return minI ==99999 and -1 or minI



if __name__=='__main__':
	ans=Solution()
	print(ans.firstUniqChar("aadadaad"))