class Solution(object):
    def removeDuplicates(self, nums):
    	#print((list(nums))[:])
    	s=list(set(nums))
    	return len(s)



s = Solution()
k=[1,1,2]
ans = s.removeDuplicates(k)
print(ans)