class Solution(object):
    def romanToInt(self, s):
    	Roman_to_int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    	index = -1
    	m = []
    	for c in s:
    		value = Roman_to_int.get(c)
    		#print(c)
    		if index == -1 :
    			m.append(value)
    		elif(m[index]<value):
    			m[index] = m[index]*-1
    		m.append(value)
    		index += 1
    	print(sum(m))
    	print(m)
    	return sum(m)

s = Solution()
ans = s.romanToInt("DCXXI")
