# 喝汽水问题，两个空瓶换一瓶


def drink(n):
	sum = 0
	while n:
		if n%2 == 1 and n!=1:
			sum += 1
		sum += n
		n //= 2
	return sum

result = drink(270)
print(result)
