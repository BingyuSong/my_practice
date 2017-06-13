class Solution(object):
    def distributeCandies(self, candies):
    	candiesSet=set(candies)
    	# return (candiesSet.length()>(candies.length()/2))? candies.length()/2 ! 
    	if len(candiesSet)>=(len(candies)/2):
    		return len(candies)/2
    	else:
    		return int(len(candiesSet))


if __name__=='__main__':
	ans = Solution()
	candies = [1,1,2,3,4,3]
	print(ans.distributeCandies(candies))