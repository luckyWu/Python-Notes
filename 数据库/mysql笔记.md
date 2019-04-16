# MySQL

MySQL 是一个关系型数据库管理系统，由瑞典 MySQL AB 公司开发，目前属于 Oracle 公司,MySQL 是一种关联数据库管理系统 ,关系型数据库管理系统（RDBMS）来存储和管理的大数据量。所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。

RDBMS 即关系数据库管理系统(Relational Database Management System)的特点：

- 1.数据以表格的形式出现
- 2.每行为各种记录名称
- 3.每列为记录名称所对应的数据域
- 4.许多的行和列组成一张表单
- 5.若干的表单组成database

#### 事务

事务是一条或多条数据库操作的集合，在事务中的操作，要么都执行修改，要么都不执行 

**事务的特性**

- **原子性：**一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

- **一致性：**在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

- **隔离性：**数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

- **持久性：**事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

  

**事务隔离级别**

mysql默认的事务隔离级别为repeatable-read 

```
mysql> select @@transaction_isolation;
+-------------------------+
| @@transaction_isolation |
+-------------------------+
| REPEATABLE-READ         |
+-------------------------+
1 row in set (0.00 sec)
```

修改事务隔离级别

```
mysql> set session transaction isolation level read uncommitted;
Query OK, 0 rows affected (0.02 sec)

mysql> select @@transaction_isolation;
+-------------------------+
| @@transaction_isolation |
+-------------------------+
| READ-UNCOMMITTED        |
+-------------------------+
1 row in set (0.00 sec)
```

 

**查看mysql默认引擎和mysql版本**

```

mysql> show variables like '%storage_engine%';
+----------------------------------+-----------+
| Variable_name                    | Value     |
+----------------------------------+-----------+
| default_storage_engine           | InnoDB    |
| default_tmp_storage_engine       | InnoDB    |
| disabled_storage_engines         |           |
| internal_tmp_disk_storage_engine | InnoDB    |
| internal_tmp_mem_storage_engine  | TempTable |
+----------------------------------+-----------+
5 rows in set, 1 warning (0.01 sec)

mysql> select version();
+-----------+
| version() |
+-----------+
| 8.0.12    |
+-----------+
1 row in set (0.00 sec)
```



**mysql授权**

```
grant select on day8.* to 'jun1'@'%'  # 授予读权限
```

```
第一个*是数据库，可以改成允许访问的数据库名称
第二个 是数据库的表名称，代表允许访问任意的表
root代表远程登录使用的用户名，可以自定义
%代表允许任意ip登录，如果你想指定特定的IP，可以把%替换掉就可以了
flush privileges;让权限立即生效
```



####SQL练习

**创建部门和员工表并插入数据**

```
drop database if exists temp;

-- 创建数据库并设置默认字符
create database temp default charset 'utf8';

-- 使用数据库
use temp;

-- 部门表
create table TbDept
(
	dno tinyint not null comment "部门编号",
	dname varchar(20) not null comment "部门名称",
	dloc varchar(20) not null comment "部门所在地",
	primary key(dno)
);

-- 员工表
create table TbEmp
(
	eno int not null comment '员工编号',
	ename varchar(20) not null comment '员工姓名',
	job varchar(20) not null comment '员工职位',
	mgr int comment '主管编号',
	sal int not null comment '月薪',
	comm int comment '月补贴',
	dno tinyint comment '所在部门编号',
	foreign key(dno) references TbDept(dno),
	primary key (eno)
);

-- 使用alter添加外键约束
-- alter table TbEmp add constraint f_dno foreign key(dno) references TbDept(dno);

-- 添加部门数据
insert into TbDept (dno, dname, dloc) values 
(10, '总部', '北京'),
(11, '指挥部', '重庆'),
(12, '战斗部', '成都');

-- 添加部门人员
insert into TbEmp values (7800, '刘备', '总裁', null, 9000, 1200, 10);
insert into TbEmp values (2056, '张飞', '将军', 7800, 5000, 1500, 12);
insert into TbEmp values (3088, '诸葛亮', '军师', 7800, 3500, 800, 11);
insert into TbEmp values (7801, '曹操', '副总裁', 7800, 8000, 1200, 10);
insert into TbEmp values (2056, '夏侯谆', '将军', 7801, 5000, 1500, 12);
insert into TbEmp values (3088, '许攸', '军师', 7801, 3500, 800, 11);

```



* 查询薪资最高的员工姓名和工资

  ```
  mysql> select ename, sal from Tbemp where sal = (select max(sal) from Tbemp);
  +--------+------+
  | ename  | sal  |
  +--------+------+
  | 刘备   | 9000 |
  +--------+------+
  1 row in set (0.00 sec)
  ```

* 查询员工的姓名和年薪((月薪+补贴)*12)*

  ```
  mysql> select ename, (sal+comm)*12 as salary from Tbemp;
  +-----------+--------+
  | ename     | salary |
  +-----------+--------+
  | 张飞      |  78000 |
  | 夏侯谆    |  78000 |
  | 诸葛亮    |  51600 |
  | 许攸      |  51600 |
  | 刘备      | 122400 |
  | 曹操      | 110400 |
  +-----------+--------+
  6 rows in set (0.00 sec)
  ```



* 查询所有员工的部门的编号、名称和人数

  ```
  mysql> select t2.dno, dname, total from tbdept t2 inner join 
  (select dno, count(dno) as total from TbEmp group by dno) t1 on t1.dno=t2.dno;
  +-----+-----------+-------+
  | dno | dname     | total |
  +-----+-----------+-------+
  |  10 | 总部      |     2 |
  |  11 | 指挥部    |     2 |
  |  12 | 战斗部    |     2 |
  +-----+-----------+-------+
  3 rows in set (0.00 sec)
  
  ```

  

* 查询薪资最高的姓名和工资（除开老板）

  ```
  
  mysql> select ename, sal from tbemp
  where sal=(select max(sal) from tbemp where mgr is not null);
  
  +--------+------+
  | ename  | sal  |
  +--------+------+
  | 曹操   | 8000 |
  +--------+------+
  1 row in set (0.09 sec)
  ```

  

* 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资

  ```
  mysql> select ename, t1.dno, sal from tbemp t1 inner join 
  (select dno, avg(sal) as ave from TbEmp group by dno) t2 
  on t1.dno=t2.dno and t1.sal>ave;
  +--------+------+------+
  | ename  | dno  | sal  |
  +--------+------+------+
  | 刘备   |   10 | 9000 |
  +--------+------+------+
  1 row in set (0.00 sec)
  ```

  

* 查询薪水超过其所在部门平均薪水的员工的姓名、部门名称和工资

  ```
  mysql> select ename, t2.dname,sal from tbemp t1
  inner join tbdept t2 on t2.dno=t1.dno
  inner join (select dno, avg(sal) as ave from TbEmp group by dno) t3 on
  t3.dno=t2.dno and t1.sal>t3.ave;
  +--------+--------+------+
  | ename  | dname  | sal  |
  +--------+--------+------+
  | 刘备   | 总部   | 9000 |
  +--------+--------+------+
  1 row in set (0.00 sec)
  ```

  

* 查询部门中薪水最高的人姓名、工资和所在部门名称

  ```
  
  mysql> select ename, dname, sal from tbemp t1 
  inner join tbdept t2 on t1.dno=t2.dno 
  inner join (select dno, max(sal) as maxs from TbEmp group by dno) t3 
  on t3.dno=t2.dno and t1.sal=t3.maxs;
  +-----------+-----------+------+
  | ename     | dname     | sal  |
  +-----------+-----------+------+
  | 张飞      | 战斗部    | 5000 |
  | 夏侯谆    | 战斗部    | 5000 |
  | 诸葛亮    | 指挥部    | 3500 |
  | 许攸      | 指挥部    | 3500 |
  | 刘备      | 总部      | 9000 |
  +-----------+-----------+------+
  5 rows in set (0.00 sec)
  ```

  