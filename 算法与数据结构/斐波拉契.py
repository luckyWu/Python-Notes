# def fib(num, temp={}):
# 	if num in (1, 2):
# 		return 1
# 	try:
# 		return temp[num]
# 	except:
# 		temp[num] =  fib(num-1) + fib(num-2)
# 		return temp[num]

# s = fib(8)

# print(s)


def fib(num, temp={}):
	if num in (1, 2):
		return 1
	try:
		return temp[num]
	except:
		temp[num] = fib(num-1) + fib(num-2)
		return temp[num]
print(fib(77))