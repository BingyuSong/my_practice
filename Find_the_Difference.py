from functools import reduce
from operator import *

class Solution(object):
    def findTheDifference(self, s, t):
    	return chr(reduce(xor,map(ord,s+t)))


if __name__=='__main__':
	ans=Solution()
	print(ans.findTheDifference('abcd','aabcd'))