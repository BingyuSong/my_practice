import numpy as np
class Solution(object):
    def convert(self, s, numRows):
    	if numRows == 1 or numRows >= len(s): 
            return s
    	m = [[] for _ in range(numRows)]
    	for i in range(len(s)):
    		m[numRows-1-abs(numRows-1-i%(2*numRows-2))].append(s[i])
    	# for i in range(numRows):
    	# 	l = "".join(m[i]) 
    	# 	print(l)
    	return "".join(["".join(m[i]) for i in range(numRows)])



s = Solution()
ans = s.convert('PAYPALISHIRING', 3)
print(ans)



