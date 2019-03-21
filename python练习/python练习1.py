


#python 注释

"""
这是多重注释
注释1
注释2
"""
print('ok')
doc = "doc"
# print(doc.__doc__)
# num = 1
# fnum = float(num)
# print(fnum, type(fnum))
# d = {'':""}
# print(bool(d))
# l = [1,2,3,4]
# l1 = l[:]
# l1[2] = 8
# print(l,l1,id(l),id(l1))
# l[2] = 100
# print(l, l1)
import copy
# c1 = [1,2,3,4,[12,33]]
# c2 = copy.copy(c1)
# # c3 = [1,2,4,[33,44]]
# c3 = copy.deepcopy(c1)
# # c3[3][1] = "wu"
# c1[4][0] = "jun" 
# # print(c2,c3)

# l = [1,2,3,4,[11, 22, 33]]
# l2 = l[:]
# l2[4][0] = "wu"
# print(l)
# print(l2)

l = {"1":[1, 2, 3, [11, 22]]}
l1 = list(l)
l3 = tuple(l)
l4 = str(l)
l["1"][3][1] = 'jun'
# print(l4,'\n',l3,'\n',l1)

# k1 = "12"
# print(tuple(l))

# s = {'a':1,"b":2}
# jj = s.update({'c':1})
# print(s)

# def reverse(chs):
# 	if len(chs) == 1:
# 		return chs[0]
# 	return chs[-1] + reverse(chs[:-1])


# a = reverse("abcdefgh")
# print(a)

import re
# b = 'ww|aa'
# m1 = re.match(b, 'ww1')
# m2 = re.match(b, 'aa1')
# m3 = re.search(b, 'wwaa')
# print(m1.group())
# print(m2.group())
# print(m3.group())
m = re.findall(r'car', 'car1car2car3')
print(m)

# print(m.g)

