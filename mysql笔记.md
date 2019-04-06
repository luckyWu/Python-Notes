# mysql

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

