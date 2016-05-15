def factor_primes(n):
	#keep a list of factors, start empty
	factors =[]
	#start an index at 2
	i = 2
	#loop while i^2 <= n
	while (i * i <= n):
		#Debug
		#print "n:"+str(n)+"i:"+str(i)+"f:"+str(factors)
		#if n mod i is not 0
		if (n % i != 0):
			#increment i
			i += 1
		#otherwise
		else:	
			#n is n/i
			n = n / i
			#add factor to the list
			factors.append(i)
		#Debug
		print "n:"+str(n)+"i:"+str(i)+"f:"+str(factors)
	#if n is not 1, add n as a factor
	if n > 1:
		#add factor to the list
		factors.append(n)
	return factors
	#product of all the factors should equal the 

print factor_primes(237)
