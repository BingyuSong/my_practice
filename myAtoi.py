class Solution(object):
    def myAtoi(self, str):
    	tmp = '0'
    	index = 0
    	result = 0
    	int_max, int_min = 2147483647,-2147483647
    	if str == '':
    		return 0
    	while str[index].isspace():
    		str = str[1:]
    	if str[index] in '+-':
    		tmp =str[index]
    		index = 1
    	for i in range(index,len(str)):
    		# if str[i].isspace():
    			# continue
    		if str[i].isdigit():
    			tmp += str[i]
    			print(tmp)
    		else:
    			break
    	if len(tmp)>1:
    		result = int(tmp)
    	if result>int_max>0:
    		return int_max
    	elif result<int_min<0:
    		return int_min
    	else:
    		return result
    

s = Solution()
ans = s.myAtoi('            1')
print(ans)