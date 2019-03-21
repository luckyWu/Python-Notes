# Python 笔记

* 浅拷贝：只拷贝父对象，不会拷贝对象的内部的子对象 

* 深拷贝：拷贝对象及其子对象 

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

  



* 列表相关操作

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

#### 生成器与迭代器

* 可迭代对象

  只要实现了\__iter__方法的对象就是可迭代的 

* 使用isinstance()判断对象是否为可迭代对象（字符串、列表、集合等都是可迭代的） 

* 可迭代对象均可以通过内置函数iter()来转变为迭代器

迭代器

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

生成器

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

协程
关于协程在一片博客上有讲到https://www.cnblogs.com/zhangxinqi/p/8337207.html

```
协程，又称微线程，纤程。英文名Coroutine。

线程是系统级别的它们由操作系统调度，而协程则是程序级别的由程序根据需要自己调度。在一个线程中会有很多函数，我们把这些函数称为子程序，在子程序执行过程中可以中断去执行别的子程序，而别的子程序也可以中断回来继续执行之前的子程序，这个过程就称为协程。也就是说在同一线程内一段代码在执行过程中会中断然后跳转执行别的代码，接着在之前中断的地方继续开始执行，类似与yield操作。
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
Thread-1 : -----还书----- 6
```

**异步处理：**

* Event Loop 事件循环：程序开启一个 While True 循环，用户将一些函数注册到事件循环上，当满足事件执行条件时，调用的协程函数；
* Task：对协程对象的进一步封装，包括任务的各种状态；
* Future：代表将来执行或没有执行的任务的结果，和 Task 没有本质的区别；
* await：挂起阻塞的异步调用接口；

 

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

