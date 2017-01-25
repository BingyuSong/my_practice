def oneWay(str1,str2):
	if abs(len(str1)-len(str2))>1:
		return False
	else:
		if len(str1)>=len(str2):
			strA = str1
			strB = str2
		else:
			strA = str2
			strB = str1
		if strB == strA[:-1]:
			return True
		else:
			for i in range(len(strB)):
				if ((strA[i]!=strB[i])&(strA[i+1:]==strB[i:]))|((strA[i]!=strB[i])&(strB[i:]==strA[i+1:])):
					return True
				elif (strA[i]!=strB[i]) & (strA[i+1:]==strB[i+1:]):
					return True
				elif (strA[i]!=strB[i]) & (strA[i+1:]!=strB[i+1:]):
					return False
				else:
					continue
			return False
str1= 'abd'
str2= 'abdd'
ans =oneWay(str1,str2)
print(ans)