class Solution(object):
	def singleNumber(self, nums):
		return 2*sum(set(nums))-sum(nums)




if __name__=="__main__":
	ans=Solution()
	grid = [1,1,2,2,3]
	print(ans.singleNumber(grid))