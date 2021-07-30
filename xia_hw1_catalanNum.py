def getCatalanNum(n):
	if n==0:
		return 1 #base case, when n=0, return 0
	else:
		return (4*n-2)/(n+1)*getCatalanNum(n-1) # recursion call on n-1, getting closer to base case

print("C100 is %1.5E " % getCatalanNum(100)) #catalan number for n =100