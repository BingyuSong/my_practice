class Solution(object):
	# def check(x,y):
	# 	if (x=='(' and y==')')or (x=='[' and y==']')or (x=='{' and y=='}'):
	# 		print(1111111)
	# 		return True
	# 	else:
	# 		return False
	def isValid(self, s):
		 #   def isValid(self, s):
        stack = []
        for i in range(len(s)):
        	if s[i] == '(' or s[i] == '[' or s[i] == '{':
        		stack.append(s[i])
        	if s[i] == ')':
        		if stack == [] or stack.pop() != '(':
        			return False
        	if s[i] == ']':
        		if stack == [] or stack.pop() != '[':
        			return False
        	if s[i] == '}':
        		if stack == [] or stack.pop() != '{':
        			return False
        if stack:
        	return False
        else:
        	return True
    # def check(x,y):
    # 	if (x=='(' and y==')')or (x=='[' and y==']')or (x=='{' and y=='}'):
    # 		print(1111111)
    # 		return True
    # 	else: 
    # 		return False


s=Solution()
# k='(){}[]'
# print(len(k))
ans=s.isValid('(){}[]')
print(ans)