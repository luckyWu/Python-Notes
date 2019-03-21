# Docker笔记

**Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口。它是目前最流行的 Linux 容器解决方案。Docker 将应用程序与该程序的依赖，打包在一个文件里面。运行这个文件，就会生成一个虚拟容器。 **

----

**Docker的一些核心组件**

*  Docker客户端和服务器 

  ```
  Docker客户端负责向Docker服务器发出请求，服务器完成所有工作并返回结果
  ```

* Docker镜像 

  ```
  镜像是只读的，镜像中包含有需要运行的文件。镜像用来创建容器，一个镜像可以运行多个容器；
  ```

* Docker hub/registry 

  ```
  用来共享和管理Docker镜像，用户可以上传或者下载上面的镜像，官方地址为https://registry.hub.docker.com/，也可以搭建自己私有的Docker registry。
  ```

* Docker容器 

  ```
  容器是一个隔离环境，多个容器之间不会相互影响，保证容器中的程序运行在一个相对安全的环境中。用户基于镜像来运行自己的容器。
  ```

### 使用Docker安装MySQL

**1.在CentOS下使用yum安装Docker并启动。**

```
yum -y install docker-io
systemctl start docker #启动后才能进行下面的操作
```

**2. 检视Docker的信息和版本。**

```
docker version
docker info
```

**3. 下载MySQL镜像。**

```
docker search mysql
docker pull mysql:5.7
docker images
```

**4. 本地建一个文件夹保存数据**

```
1.创建目录和配置文件my.cnf
[root@VM_0_3_centos ~]# mkdir docker
[root@VM_0_3_centos ~]# mkdir docker/mysql/conf
mkdir: cannot create directory ‘docker/mysql/conf’: No such file or directory
[root@VM_0_3_centos ~]# mkdir -p docker/mysql/conf
[root@VM_0_3_centos ~]# mkdir -p docker/mysql/data
[root@VM_0_3_centos ~]# touch docker/mysql/conf/my.cnf
[root@VM_0_3_centos ~]# vim docker/mysql/conf/cnf.d
# cnf.d中添加下面的内容
 [mysqld]
 pid-file=/var/run/mysqld/mysqld.pid
 socket=/var/run/mysqld/mysqld.sock
 datadir=/var/lib/mysql
 log-error=/var/log/mysql/error.log
 server-id=1
 log-bin=/var/log/mysql/mysql-bin.log
 expire_logs_days=30
 max_binlog_size=256M
 symbolic-links=0

```

**5.创建容器**

```
[root@VM_0_3_centos ~]# docker run -d -p 3306:3306 -v /root/docker/mysql/conf:/etc/mysql/mysql.conf.d -v /root/docker/mysql/data:/var/lib/mysql --name mysql-1 -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7
ee698cb71a8a4e046c08744ebb38b709a7356f9e692ad27e8395a8360b29233e

参数说明：

-e MYSQL_PASSWORD="123456"：设置添加的用户密码
-e MYSQL_ROOT_PASSWORD="123456"：设置root用户密码
-p 3307:3306：将容器的3306端口映射到主机的3307端口
-v /root/docker/mysql/conf/cnf.d:/etc/my.cnf.d：主机目录:容器目录

```

**6.进入MySQl**

```
root@VM_0_3_centos conf]# docker exec -it mysql-1  bash
root@075b763b9216:/# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.25-log MySQL Community Server (GPL)

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

**7.windows上传文件到linux**

```
# 安装lrzsz.x86_64包
[root@VM_0_3_centos conf]# yum -y install lrzsz.x86_64
#输入rz即可选择文件上传
```
**8.查看历史记录**

```
history命令：用于显示历史记录和执行过的指令命令。history命令读取历史命令文件中的目录到历史命令缓冲区和将历史命令缓冲区中的目录写入命令文件。该命令单独使用时，仅显示历史命令，在命令行中，可以使用符号!执行指定序号的历史命令。例如，要执行第2个历史命令，则输入!2
```

