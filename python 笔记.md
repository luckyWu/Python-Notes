# Python 笔记



**可变/不可变对象**

`不可变对象`，该对象所指向的内存中的值不能被改变，对象的值改变后对象的地址也改变

`可变对象`，该对象所指向的内存中的值可以被改变，但对象的地址始终不变

Python中，数值类型、字符串、元组都是不可变类型。而列表list、字典dict、集合set是可变类型。

以列表(可变对象)为例

```
l = [1,2]
print(id(l)) # 30237256
l[0] = 11
print(id(l)) # 30237256

# 对象的值改变了，对象的地址并未改变
```



以元祖(不可变对象)为例

```
t = ('a', 'b', ['c','d'])

print(id(t[2]),t) # 1925640 ('a', 'b', ['c', 'd'])
t[2][0] = 'e'
print(id(t[2]),t) # 1925640 ('a', 'b', ['e', 'd'])

# 这里的不变指的是指向不变，并不是内容不变
```

----

#### 切片

**为什么切片和区间会忽略最后一个元素(参考《流畅的python》)**

```
	在切片和区间操作里不包含区间范围的最后一个元素是 Python 的风格，这个习惯符合 Python、C 和其他语言里以 0 作为起始下标的传统。这样做带来的好处如下。
1.当只有最后一个位置信息时，我们也可以快速看出切片和区间里有几个元素：range(3) 和 my_list[:3] 都返回 3 个元素。
2.当起止位置信息都可见时，我们可以快速计算出切片和区间的长度，用后一个数减去第一个下标（stop - start）即可。
3.这样做也让我们可以利用任意一个下标来把序列分割成不重叠的两部分，只要写成 my_list[:x] 和 my_list[x:] 就可以了
```

**给切片赋值**

```
l = list(range(10))
print(l)
l[1:3] = [20, 30]
print(l)
del l[3:5]
print(l)
# 输出结果
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 20, 30, 3, 4, 5, 6, 7, 8, 9]
[0, 20, 30, 5, 6, 7, 8, 9]
# 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。即便只有单独一个值，也要把它转换成可迭代的序列
```

**对序列使用+和***

慎用*

```
y = [['*'] * 3] * 3
print(y)
y[0][1] = '#'
print(y)

y1 = [['x'] * 3 for _ in range(3)]
print(y)
y1[0][1] = 'y'
print(y1)

# 输出
[['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
[['*', '#', '*'], ['*', '#', '*'], ['*', '#', '*']]
[['*', '#', '*'], ['*', '#', '*'], ['*', '#', '*']]
[['x', 'y', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

#  第一个例子3个引用指向的都是同一个列表，改变其中一个另外几个都会发生改变，若不期望出现这种情况，应该用第二个例子的方法
```





**浅拷贝与深拷贝**

`浅拷贝`：只拷贝父对象，不会拷贝对象的内部的子对象 

`深拷贝`：拷贝对象及其子对象 

```
# 深拷贝（str()方法也是完全拷贝）
import copy
c1 = [1,2,3,4,[12,33]]
c2 = copy.copy(c1)
c3 = copy.deepcopy(c2)
c1[4][0] = "jun" 
print(c2,c3)
>>>[1, 2, 3, 4, ['jun', 33]] [1, 2, 3, 4, [12, 33]]
# 浅拷贝(切片为浅拷贝)
l = [1,2,3,4,[11, 22, 33]]
l2 = l[:]
l2[4][0] = "wu"
print(l)
print(l2)
>>>[1, 2, 3, 4, ['wu', 22, 33]]
   [1, 2, 3, 4, ['wu', 22, 33]]
   
```

---------------



**列表相关操作**

```
#列表间支持'+'运算
s = [1, 2, 3] + [4, 5, 6, [11, 22]]
print(s) #[1, 2, 3, 4, 5, 6, [11, 22]]

# 列表extend方法，将一个序列中的每个元素添加到列表
s = []
s.extend('12345') #['1', '2', '3', '4', '5']

# 如果是字典则只填加字典的键
s.extend({'a':1,'b':2}) #['1', '2', '3', '4', '5', 'a', 'b']


```
----------

#### 面向对象

类：就是拥有相同功能和相同属性的对象的集合（类是抽象）
对象：类的实例（对象是具体的）

**多重继承**

python多重继承的MRO算法选择： 经典方式、Python2.2 新式算法、Python2.3 新式算法(C3)。Python 3中只保留了最后一种，即C3算法 

```
class A(object):
	def dog(self):
		print('dogA')

	def ping(self):
		print('pingE')
		

class B(A):
	def dog(self):
		print('dogb')


class C(A):
	def dog(self):
		print('dogc')


class E(B, C):
	def ping(self):
		print('doge')


e = E()
print(E.__mro__)
e.dog()
结果：
(<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
dogb

```



#### 生成器与迭代器

* 可迭代对象

  只要实现了\__iter__方法的对象就是可迭代的 

* 使用isinstance()判断对象是否为可迭代对象（字符串、列表、集合等都是可迭代的） 

* 可迭代对象均可以通过内置函数iter()来转变为迭代器

**迭代器**

迭代是访问集合元素的一种方式，迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束 

 只要定义了\__next ()__ 方法就是一个迭代器

```
""" 
class Fib():
	"""迭代器"""
    def __init__(self, num):
        self.a = 1
        self.b = 0
        self.index = 0
        self.num = num

    def __iter__(self):
        return self #返回自身

    def __next__(self):
        if self.index < self.num:
            self.a, self.b = self.a + self.b, self.a
            self.index += 1
            return self.b
        else:
            raise StopIteration()
```

**生成器**

生成器也是一中迭代器，它按照顺序返回一个或多个值直到完成函数的迭代而终止，大多数时候生成成器是以函数来实现的，使用yield返回值，每次调用yield会暂停直到调用代码恢复生成器。 

```
# 简单生成器
x = (i for i in range(1))
print(x) # <generator object <genexpr> at 0x0000000002D548B8>

# 生成器函数
def test():
	for i in range(10):
		yield i
```

**协程**

协程，又称微线程，纤程。英文名Coroutine，**是一种用户态的轻量级线程**。

​	协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方（线程调度时候寄存器上下文及栈等保存在内存中），在切回来的时候，恢复先前保存的寄存器上下文和栈。

关于协程在一片博客上有讲到https://www.cnblogs.com/zhangxinqi/p/8337207.html

```
协程，又称微线程，纤程。英文名Coroutine。
	线程是系统级别的它们由操作系统调度，而协程则是程序级别的由程序根据需要自己调度。在一个线程中会有很多函数，我们把这些函数称为子程序，在子程序执行过程中可以中断去执行别的子程序，而别的子程序也可以中断回来继续执行之前的子程序，这个过程就称为协程。也就是说在同一线程内一段代码在执行过程中会中断然后跳转执行别的代码，接着在之前中断的地方继续开始执行，类似与yield操作。
```

**产出两个值的协程**

```
def cor2(a):
		print('start! a=',a)
		b = yield a
		print('this is b :',b)
		c = yield a + b
		print('this is c:',c)
		
try:
	s = cor2(1)
	print(next(s))
	print(s.send(2))
	s.send(3)
except StopIteration:
	pass
# 执行结果
start! a= 1
1
this is b : 2
3
this is c: 3
# 调用next()函数进入生产器
# 把2发给协程，产出a+b
# 把3发给协程，输出c的值
# 执行结束产生StopIteration异常
# 注意：协程在 yield 关键字所在的位置暂停执行,在赋值语句中，= 右边的代码在赋值之前执行
```

**异步IO：**

Python 3.4版本引入`asyncio` 标准库，直接内置了对异步IO的支持 ,Python 3.5开始引入了新的语法`async`和`await` 

- Event Loop 事件循环：程序开启一个 While True 循环，用户将一些函数注册到事件循环上，当满足事件执行条件时，调用的协程函数；
- Task：对协程对象的进一步封装，包括任务的各种状态；
- Future：代表将来执行或没有执行的任务的结果，和 Task 没有本质的区别；
- await：挂起阻塞的异步调用接口；

```
import asyncio

async def show1():
    """输出0-4"""
    for i in range(5):
        print('show1',i)
        await asyncio.sleep(1) #等待2s
async def show2():
    """输出5-9"""
    for i in range(5,10):
        print('show2',i)
        await asyncio.sleep(1) #等待2s

def main():
    """主函数"""
    loop = asyncio.get_event_loop() #获得系统默认的事件循环
    future = asyncio.gather(show1(),show2()) #通过gather函数可以获得一个future对象
    loop.run_until_complete(future) #等待通过future对象获得协程执行结果。
    loop.close()


if __name__ == '__main__':
    main()

```

输出结果：

```
show1 0
show2 5
show1 1
show2 6
show1 2
show2 7
show1 3
show2 8
show1 4
show2 9
```




#### 进程和线程

* 进程是资源（CPU、内存等）分配的基本单位 
* 线程是程序执行时的最小单位 

**全局解释器锁（GIL)**

对于GIL，在《Python 核心编程》有这样一段描述

```
Python 代码的执行是由 Python 虚拟机（又名解释器主循环）进行控制的。Python 在
设计时是这样考虑的，在主循环中同时只能有一个控制线程在执行，就像单核 CPU 系统
中的多进程一样。内存中可以有许多程序，但是在任意给定时刻只能有一个程序在运行。
同理，尽管 Python 解释器中可以运行多个线程，但是在任意给定时刻只有一个线程会被
解释器执行。
对 Python 虚拟机的访问是由全局解释器锁（GIL）控制的。这个锁就是用来保证同时只
能有一个线程运行的
```





**多线程**

 Python提供了threading 模块来支持多线程

创建线程有3种方式

* 通过Thread类来实现
* 通过之定义类，并继承Thread实现
* 使用线程池实现

```
"""模拟100个人同时还书"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor

class Library():
    """图书馆借书系统"""

    def __init__(self):
        self.books = 0

    def re_book(self, book):
        """还书"""

        new_nums = self.books + book
        time.sleep(0.01)
        self.books = new_nums

class AddBookThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, account, book):
        self.account = account
        self.book = book
        # 自定义线程的初始化方法中必须调用父类的初始化方法
        super().__init__()

    def run(self):
        # 线程启动之后要执行的操作
        self.account.re_book(self.book)


def main():
    # 创建线程池
    pool = ThreadPoolExecutor(10)
    futures = []
    library = Library()
    ts = []
    for _ in range(100):
        # 创建线程的第1种方式
        t = threading.Thread(target=library.re_book, args=(1, ) )
        ts.append(t)
        # 创建线程的第2种方式
        # AddBookThread(library, 1).start()

    for t in ts:
        t.start()
    # 等待子进程全部结束
    for t in ts:
        t.join()
        
   # 创建线程的第3种方式 
   #  for _ in range(100):
       # 调用线程池中的线程来执行特定的任务
       # 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
       # future = pool.submit(library.re_book, 1)
       # futures.append(future)
       #future的result()方法可以获取到函数的执行结果, 这个方法是阻塞的
       # for li in futures:
       #     print(li.result())

    # 关闭线程池
    pool.shutdown()
    print(library.books)

if __name__ == '__main__':
    main()
# 输出结果：6 这是因为多个进程在同一时刻可能取到相同的数据，GIL保护的是解释器级的数据，保护用户自己的数据则需要自己加锁处理
# 使用Lock()来保护资源，对Library类进行修改
class Library():
    """图书馆借书系统"""

    def __init__(self):
        self.books = 0
        self.lock = threading.Lock()

    def re_book(self, book):
        """还书"""
        with self.lock:
            new_nums = self.books + book
            time.sleep(0.001)
            self.books = new_nums
# 修改后再运行结果为100
```
对上面程序进行修改，实现5个人借书，5个人还书，图书馆书不够时就暂停等待有书为止

使用`threading`模块的Condition来实现线程调度 ，实现在某个事件触发后才处理数据 

- wait:线程挂起收到notify通知后继续运行  
-  notify:通知其他线程, 解除其它线程的wai状态  -
- notify_All(): 通知所有线程  
-  acquire和release: 获得[锁和](https://www.baidu.com/s?wd=%E9%94%81%E5%92%8C&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)解除锁, 与lock类似,



```
"""多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition"""

from random import randint
import time
import threading

class Library():
    """图书馆系统"""

    def __init__(self):
        self.books = 0
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def re_book(self, book):
        """还书"""
        with self.condition:
            new_nums = self.books + book
            time.sleep(0.01)
            self.books = new_nums
            self.condition.notify_all() #
            
    def bo_book(self, book):
        """借书"""
        with self.condition:
            while book > self.books:
                self.condition.wait() # 等待
            new_nums = self.books - book
            time.sleep(0.01)
            self.books = new_nums

def add_book(account):
    while True:
        book = randint(5, 10)
        account.re_book(book)
        print(threading.current_thread().name, 
              ':', '-----还书-----',book)
        time.sleep(0.5)


def sub_book(account):
    while True:
        book = randint(10, 30)
        account.bo_book(book)
        print(threading.current_thread().name, 
              ':', '图书馆总数-------------', account.books, '借书',book)
        time.sleep(1)


def main():
    """创建线程"""

    account = Library()
    for _ in range(5):
        threading.Thread(target=add_book, args=(account,)).start()
        threading.Thread(target=sub_book, args=(account,)).start()



if __name__ == '__main__':
    main()
```

运行结果：

```
Thread-3 : -----还书----- 5
Thread-9 : -----还书----- 8
Thread-7 : -----还书----- 9
Thread-10 : 图书馆总数------------- 14 借书 13
Thread-1 : -----还书----- 7
Thread-8 : 图书馆总数------------- 0 借书 21
Thread-5 : -----还书----- 8
Thread-3 : -----还书----- 10
Thread-9 : -----还书----- 7
Thread-7 : -----还书----- 5
Thread-2 : 图书馆总数------------- 0 借书 30
Thread-1 : -----还书----- 
```

