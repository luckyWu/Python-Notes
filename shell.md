# shell

1.\#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell

2.echo 命令用于向窗口输出文本

3.定义变量时，变量名不加美元符号（$，PHP语言中变量需要） 

注意，变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样。同时，变量名的命名须遵循如下规则：

- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）

4.使用一个定义过的变量，只要在变量名前面加美元符号即可 



**实例if.sh**

```
#!/bin/bash

a=10
b=20
if [ $a == $b ]
then
    echo 'a 等于 b'
elif [ $a -gt $b ]
then
    echo 'a 大于 b'
elif [ $a -lt $b ]
then
    echo 'a 小于 b'
else
    echo 'nothing'
fi


for i in 1 2 3
do
    echo "this is : $i"
done

i=4
while(( $i<=6 ))
do
    echo "$i"
    let i++
done
```

```
root@instance-5538u54p:~/work# ./if.sh
a 小于 b
this is : 1
this is : 2
this is : 3
4
5
6
input >>
4
no select
root@instance-5538u54p:~/work# 
```

