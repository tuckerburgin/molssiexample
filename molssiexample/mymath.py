"""
A file for executing math functions.
"""
import random
import math

def fact(x):
	tot = x
	if x == 0:
		return 1
	for i in range(x):
		if i > 0:
			tot = tot*i
	return tot

def euler(n=10):
	if n < 0:
		raise ValueError("n must be >= 0")
	sum = 0
	for i in range(n+1):
		sum += 1**i/fact(i)
	return sum

def pi(n=100):
	count = 0
	for i in range(n):
		if math.sqrt(random.random()**2 + random.random()**2) < 1:
			count += 1
	ratio = count/n		# ratio of in circle to outside circle
	pi = ratio*4
	return(pi)

print(pi(100000))
