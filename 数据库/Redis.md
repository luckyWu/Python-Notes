# Redis

REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。

Redis是一个开源的使用ANSI C语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。

它通常被称为数据结构服务器，因为值（value）可以是 字符串(String), 哈希(Hash), 列表(list), 集合(sets) 和 有序集合(sorted sets)等类型。

**有序集合**

* 不允许重复 
* 每个元素都会关联一个double类型的分数, 通过分数来为集合中的成员进行从小到大的排序 
* 有序集合的成员是唯一的,但分数(score)却可以重复 
* 集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1) 

```

127.0.0.1:6379> zadd wu 2 'dog'
(integer) 1
127.0.0.1:6379> zadd wu 2.4 'cat'
(integer) 1
127.0.0.1:6379> zrange wu 0 5 # 通过索引区间返回有序集合成指定区间内的成员
1) "dog"
2) "cat"
127.0.0.1:6379> zscore wu "dog" #返回有序集中，成员的分数值
"2"
127.0.0.1:6379> zrevrange wu 0 5 # 返回有序集中指定区间内的成员，通过索引，分数从高到底
1) "cat"
2) "dog"
127.0.0.1:6379> zrangebyscore wu 0 10 # 通过分数返回有序集合指定区间内的成员
1) "dog"
2) "cat"
127.0.0.1:6379> 
```
ZCARD命令返回在指定的键存储在集合中的元素的数量 

```
127.0.0.1:6379> zcard wu
(integer) 5
127.0.0.1:6379> 
```



**列表**

