import math
class Solution(object):
    def constructRectangle(self, area):
    	# i=math.sqrt(area)
    	# if int(i)==i: 
    	# 	return [i,i]
    	# else:
	    # 	for x in range(int(i),area+1):
	    # 		y=area/x
	    # 		if int(y)==y: return [max(int(x),int(y)),min(int(x),int(y))]
	    mid=int(math.sqrt(area))
	    while (mid>0):
	    	if area%mid==0:
	    		return [int(area/mid),mid]
	    	mid-=1

if __name__=="__main__":
	ans=Solution()
	print(ans.constructRectangle(5))



