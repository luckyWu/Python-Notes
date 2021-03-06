"""
一趟快速排序的算法是：
1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）
"""

l = [15, 21, 3, 41, 5, 9, 122, 22, 22, 100, 10, 123, 222, 33, 22,33,44,53]


def quick_sort(l, start, end):
	s = start
	e = end
	# 结束条件
	if s < e:
		key = l[s]
		while(s < e):
			#如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
			while(s < e and key <= l[e]):
				e -= 1
			#如找到,则把第e个元素赋值给第个元素s
			l[s], l[e] = l[e], l[s]
			#同样的方式比较前半区
			while(s < e and key >= l[s]):
				s += 1
			l[s], l[e] = l[e], l[s]
		#递归前后半区
		quick_sort(l, start, s-1)
		quick_sort(l, e+1, end)
	return l


# print(quick_sort(l, 0, len(l)-1))

def qp(items, start, end):
	s, e = start, end
	if s < e:
		key = items[s]
		while(s<e):
			while (s<e and key<=items[e]):
				e -= 1
			items[s], items[e] = items[e], items[s]
			while (s<e and key>=items[s]):
				s += 1
			items[s], items[e] = items[e], items[s]
		qp(items, start, s-1)
		qp(items, s+1, end)

	return items

print(qp([1,1,10,2,4],0,4))



