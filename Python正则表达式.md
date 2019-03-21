# Python正则表达式

**Python 当前如何通过使用 re 模块来支持正则表达式**

**re模块函数有compile()、match()、search()、findall()、sub()等等**

**1.使用 compile()函数编译正则表达式**

```
在模式匹配发生之前，正则表达式模式必须编译成正则表达式对象
在直接使用字符串表示的正则表达式进行search,match和findall操作时，python会将字符串转换为正则表达式对象。而使用compile完成一次转换之后，在每次使用模式的时候就不用重复转换
```



**2.  group()和 groups()方法**

* group()和groups()能够对对象进行匹配，这些是成功调用 match()或者 search()返回的对象
* group()要么返回整个匹配对象，要么根据要求返回特定子组。groups()则仅返回一个包含
  唯一或者全部子组的元组。如果没有子组的要求，那么当group()仍然返回整个匹配时，groups()
  返回一个空元组。

```
1.使用 match()方法匹配字符串
match()是从字符串的起始部分对模式进行匹配，如果匹配成功，就返回一个匹配对象；如果匹配失败，就返回 None
# example
import re
str1 = 'wwwwww121312'
m = re.match('wwww(w)',str1) #圆括号指定分组
print(m)
print(m.group(), type(m.group()))
print(m.group(0)) #group(0)和group(0)效果是一样的都是返回整个匹配对象
print(m.group(1)) #返回分组中的对象

#结果
<re.Match object; span=(0, 5), match='wwwww'>
wwwww <class 'str'>
wwwww
w
-----------------------------------------------------------------------------------------------
2.使用search()匹配
在任意位置对给定正则表达式模式搜索第一次出现的匹配情况。如果搜索到成功的匹配，就会返回一个匹配对象；否则，返回 None
# examole
m = re.search('12',str1)
print(m)
print(m.group())

# 结果
<re.Match object; span=(6, 8), match='12'>
12
```

**3.匹配多个字符串**

使用择一匹配（|）符号

```
import re
b = 'ww|aa' #要么匹配ww要么匹配aa
m1 = re.match(b, 'ww1') 
m2 = re.match(b, 'aa1')
m3 = re.search(b, 'wwaa') 
print(m1.group())
print(m2.group())
print(m3.group())

# 结果
ww
aa
ww
```



**4.使用 findall()查找**

findall()返回字符串所有符合中某个正则表达式的结果，返回的对象是一个列表

```
m = re.findall(r'car', 'car1car2car3')
print(m)
#结果
['car', 'car', 'car']

```

