---
title: python函数注解
date: 2020.11.13
---

## 1. 函数文档

前面已经有说过了，在定义函数的时候，可以在函数的第一行输入一个字符串，这个字符串就代表了这个函数的注释。

这个对函数的描述被保存在函数的属性里，可以用**funcname.doc**调出来。

例：

```python 
print(sum.__doc__)

Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types

sum.__doc__
"Return the sum of a 'start' value (default: 0) plus an iterable of numbers\n\nWhen the iterable is empty, return the start value.\nThis function is intended specifically for use with numeric values and may\nreject non-numeric types."

```

sum函数是一个内建函数，我们可以直接调用出它的函数注解。

注意一般函数文档都是用**''' '''** ，三引号来括起来，因为可以随意换行，看起来更方便，所以print打印出函数注解会自动换行，直接输出的话，遇到换行符就不会生效。

我们自己也可以写函数文档：

```python
def funcname():
    """I miss a beautiful girl."""
    ...
    return ...

```

定义完成后，我们就可以调用这个函数的注解了：

```python
funcname.__doc__
```

**写代码定义函数的时候，最好有函数文档来描述函数的作用等，并且在重新更新函数的时候，一并更新函数文档。**

## 2. 参数、返回值注解

- python是一门强类型、动态语言，既同类型的变量才能一起运算、定义变量前不用事先声明变量类型。这样虽然带来了便利，但是也会带来弊端。（就俗话说的物极必反）
  - 弊端一：在定义函数时，如果运算的变量类型不对，是不会报错的。通常在这个函数运行时候才会报错。都开始运行了，才发现错误，蠢不蠢。
    所以需要写代码的时候做好测试，测试的状况得全面。
  - 弊端二：定义完函数直接调用，自己写的函数还行，要是用别人定义的函数，不知道要传什么类型的参数，也不知道函数内部的解构是什么样子的。
    可以用函数注解和参数注解来解决。

- 参数注解就是，在定义函数的时候，参数列表内部的参数后面，加上冒号和要传入的类型，例：

```python
def accumlate(x:int, y:int):
    return x*y
```

写了参数注解也无法强制限定变量的类型，只能作为提示，来告知使用者应该传入什么类型的参数。

- 返回值注解就是：

```python 
def accumlate(x:int, y:int) -> int:
    return x*y
```

在参数列表后面，冒号前面，增加一个 -> 后面接返回值的类型。

这些注解都会以字典的形式存在函数的**.annotations**属性中。

```python 
accumlate.__annotations__
{'x': int, 'y': int, 'return': int}

print(accumlate.__annotations__)
{'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
```

value里面存的数据是type，也就是是个类型。

## 3. 变量注解

在python3.6及更高的版本。支持为变量添加注解，来显示这个变量的类型。

同样也不是强制的规定，而是提醒。

例如：

```python
a：int = 100
```

不会影响变量a的正常使用，只是提醒一下a应该是什么类型的数据。