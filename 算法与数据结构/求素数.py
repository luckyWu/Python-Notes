import math

print(math.sqrt(6))

def prime(m, n):
	for i in range(m, n):
		if i<=1:
			print("no")
			continue
		flag = True
		for j in range(2, int(math.sqrt(i)+1)):
			if i%j == 0:
				flag = False
		if flag:
			print("prime——>",i)

prime(1,100)







