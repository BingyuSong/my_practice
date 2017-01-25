class Solution(object):
    def reverse(self, x):
    	s = str(x)
    	m = []
    	if s[0] == "-":
    		m +=s[0]
    		s = s[1:]
    	m .append(s[::-1]) 
    	return int("".join(m))
    	#print int(m)
s  = Solution()
ans = s.reverse(-123) 