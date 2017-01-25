def string_compression(input_str):
	k = list(input_str)
	i = 0
	count = 1
	for j in range(i+1,len(k)):
		if j == (len(k)-1) and count !=1 and k[i]==k[j]:
			count+=1
			k[j] = str(count)
			k[i+1:j-1] = ''
		elif k[i] == k[j]:
			count = count+1
		elif count !=1:
			k[j-1] = str(count)
			k[i+1:j-2] = ''
			count = 1
			i = j
	print(k)
	ans = "".join(k)
	print(ans)
	return ans
	

k = 'aabbccc'
ans = string_compression(k)
print(ans)


