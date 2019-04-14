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



**mysql 不区分大小写**

```
create database temp default charset 'utf8'; --设置默认字符

create table TbDept

(

	dno int not null, --"部门编号"

	dname varchar(20) not null， -- "部门名称"

	dloc varchar(20) not null --"部门所在地"

	primary key(dno)

);

```

**创建员工表**

```
create table TbEmp

(
	eno int not null ,-- '员工编号',
	ename varchar(20) not null ,-- '员工姓名',
	job varchar(20) not null,-- '员工职位',
	mgr int ,--'主管编号',
	sal int not null ,-- '月薪',
	comm int ,-- '月补贴',
	dno tinyint ,-- '所在部门编号',
	primary key (eno)

);

```



**添加外键约束**

```
alter table TbEmp add constraint fk_dno foreign key(eno) references TbDept(dno) ；
```



**添加员工**

```
insert into TbEmp values (7800, '张三丰', '总裁', null, 9000, 1200, 20);
insert into TbEmp values (2056, '乔峰', '分析师', 7800, 5000, 1500, 20);
insert into TbEmp values (3088, '李莫愁', '设计师', 2056, 3500, 800, 20);
```



**添加部门**

```
insert into TbDept values (10, '会计部', '北京');
insert into TbDept values (20, '研发部', '成都');
insert into TbDept values (30, '销售部', '重庆');
```





-- 查询薪资最高的员工姓名和工资

select ename, sal from Tbemp where sal = (select max(sal) from Tbemp);

------------



-- 查询员工的姓名和年薪((月薪+补贴)*12)*

*select ename, (sal+comm)*12 from Tbemp;



![12](img/20190224180004.png)

![12](img/20190224180631.png)

----------





-- 查询所有员工的部门的编号和人数
select dno, count(dno) as total  from TbEmp group by dno;

![12](img/20190224181333.png)

------------





-- 查询所有部门的名称和人数
select dname, total from tbdept t2, (select dno, count(dno) as total  from TbEmp group by dno) t1 where t2.dno=t1.dno ;
select dname, total from tbdept t2 inner join (select dno, count(dno) as total  from TbEmp group by dno) t1 on t2.dno=t1.dno;

![12](img/20190224191303.png)

-----------------



---- 查询薪资最高的姓名和工资
select ename, sal from tbemp
where sal=(select max(sal) from tbemp where mgr is not null);

![12](img/20190224192022.png)

--------------



-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
select ename, t1.dno, sal from tbemp t1,
(select dno, avg(sal) as ave from TbEmp group by dno) t2 where t1.dno=t2.dno and t1.sal>t2.ave;

select ename, t1.dno,sal from tbemp t1 inner join 
(select dno, avg(sal) as ave from TbEmp group by dno) t2 on t1.dno=t2.dno and t1.sal>t2.ave;



![12](img/20190224194052.png)

-----------------



-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门名称和工资
select ename, t2.dname,sal from tbemp t1, tbdept t2,
(select dno, avg(sal) as ave from TbEmp group by dno) t3
where t3.dno=t2.dno and t1.sal>t3.ave and t1.dno=t2.dno;

select ename, t2.dname,sal from tbemp t1 inner join  tbdept t2 on t2.dno=t1.dno
inner join (select dno, avg(sal) as ave from TbEmp group by dno) t3 on
t3.dno=t2.dno and t1.sal>t3.ave;

![12](img/20190224195303.png)

---------------



-- 查询部门中薪水最高的人姓名、工资和所在部门名称
select ename, t2.dname,sal from tbemp t1 inner join tbdept t2 on t2.dno=t1.dno
inner join (select dno, max(sal) as maxs from TbEmp group by dno) t3 on t3.dno=t2.dno and t1.sal=t3.maxs;

![12](img/20190224195823.png)

