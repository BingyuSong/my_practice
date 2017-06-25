class Solution(object):
    def findRelativeRanks(self, nums):
    	if len(nums)==1: return ["Gold Medal"]
    	dict={}
    	g=["Gold Medal","Silver Medal","Bronze Medal"]
    	for i in range(len(nums)):
    		dict[nums[i]]=i
    	print(dict)
    	key=[i for i in dict.keys()]
    	re_keys=[i for i in reversed(sorted(key))]
    	if len(nums)==2:
    		nums[dict[re_keys[0]]]="Gold Medal"
    		nums[dict[re_keys[1]]]="Silver Medal"
    		return nums
    	else:
	    	nums[dict[re_keys[0]]]="Gold Medal"
	    	nums[dict[re_keys[1]]]="Silver Medal"
	    	nums[dict[re_keys[2]]]="Bronze Medal"
	    	for j in range(3,len(nums)):
	    		nums[dict[re_keys[j]]]=str(j+1)
	    	return nums


if __name__=='__main__':
	ans=Solution()
	nums=[10,3,8,9,4]
	print(ans.findRelativeRanks(nums))



