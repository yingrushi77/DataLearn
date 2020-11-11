---
title: global与nonlocal
date: 2020.11.10
---

## 关键字global与nonlocal的区别

**global**关键字用来在函数或其他局部作用域中使用全局变量， **nonlocal**声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。

### global

- 总述

总之一句话，作用域是全局的，就是会修改这个变量对应地址的值。

global 语句是一个声明，它适用于整个当前代码块。 这意味着列出的标识符将被解释为全局变量。 尽管自由变量可能指的是全局变量而不被声明为全局变量。

global 语句中列出的名称不得用于该全局语句之前的文本代码块中。

global 语句中列出的名称不能定义为形式参数，也不能在 for 循环控制目标、 class 定义、函数定义、 import 语句或变量注释中定义。

当前的实现并不强制执行这些限制，但是程序不应该滥用这种自由，因为未来的实现可能会强制执行这些限制，或者悄悄地改变程序的含义。

程序员注意: global 是指向解析器的指令。 它仅适用于与全局语句同时解析的代码。 特别是，包含在提供给内置 exec() 函数的字符串或代码对象中的全局语句不会影响包含函数调用的代码块，而且这种字符串中包含的代码不会受包含函数调用的代码中的全局语句的影响。 eval() 和 compile() 函数也是如此。

![](https://gitee.com/smithbee/image_bed/raw/master/202012090302626.jpg)

1. global关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。

```python
gcount = 0
def global_test():
	gcount+=1
	print (gcount)
global_test()
```

以上代码会报错：第一行定义了全局变量，在内部函数中又对外部函数进行了引用并修改，那么python会认为它是一个局部变量，有因为内部函数没有对其gcount进行定义和赋值，所以报错。

2. 如果局部要对全局变量修改，则在局部声明该全局变量

```python
gcount = 0
def global_test():
	global gcount
	gcount+=1
	print (gcount)
global_test()
```

以上输出为：1

3. 如果局部不声明全局变量，并且不修改全局变量，则可以正常使用

```python
gcount = 0
def global_test():
	print (gcount)
global_test()
```

以上输出为：0



### nonlocal

- 总述

只在闭包里面生效，作用域就是闭包里面的，外函数和内函数都影响，但是闭包外面不影响。

**nonlocal** 语句使列出的标识符引用除 **global** 变量外最近的封闭范围中的以前绑定的变量。 这很重要，因为绑定的默认行为是首先搜索本地名称空间。 该语句允许封装的代码将变量重新绑定到除全局(模块)作用域之外的本地作用域之外。

**nonlocal** 语句中列出的名称与 **global** 语句中列出的名称不同，它们必须引用封闭范围中已经存在的绑定(无法明确确定应在其中创建新绑定的范围)。

1. nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。

```python
def make_counter():
	count = 0
	def counter():
    	nonlocal count
    	count += 1
    	return count
	return counter()   
def make_counter_test():
	mc = make_counter()
	print(mc())
	print(mc())
	print(mc())
make_counter_test()
```

以上输出为：

> 1
>
> 2
>
> 3

### 混合使用

```python
def scope_test():
	def do_local():
    	spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
	def do_nonlocal():
    	nonlocal spam    #使用外层的spam变量
    	spam = "nonlocal spam"
	def do_global():
    	global spam
    	spam = "global spam"
	spam = "test spam"
	do_local()
	print("After local assignmane:", spam)
	do_nonlocal()
  	print("After nonlocal assignment:",spam)
  	do_global()
  	print("After global assignment:",spam)
 
scope_test()
print("In global scope:",spam)
```

以上输出为：

> After local assignmane: test spam
> After nonlocal assignment: nonlocal spam
> After global assignment: nonlocal spam
> In global scope: global spam