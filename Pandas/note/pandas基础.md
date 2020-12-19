## pandas基础

![image-20201219154738860](https://gitee.com/smithbee/image_bed/raw/master/image-20201219154738860.png)

学习之前，要 **import** 的库

```python
import numpy as np 
import pandas as pd 
```

请保证 `pandas` 的版本号不低于 **1.1.5** ，否则请务必升级！

- 查看已安装库的版本和当前最新的版本

`pip list --outdated`

![image-20201217220910391](https://gitee.com/smithbee/image_bed/raw/master/image-20201217220910391.png)

- 更新已安装库

`pip install --upgrade 库名`

![image-20201217221222237](https://gitee.com/smithbee/image_bed/raw/master/image-20201217221222237.png)

也可用 `pip install -U 库名`



### 一、文件的读取和写入

#### 1. 文件读取

- `pandas` 可以读取的文件格式有很多，这里主要介绍读取 `csv, excel, txt` 文件

```python 
# 导入库 读取文件
import numpy as np 
import pandas as pd 

df_csv = pd.read_csv('data/my_csv.csv') # 读取csv文件
print(df_csv)
print("===================================")
df_txt = pd.read_table('data/my_table.txt') # 读取txt文件
print(df_txt)
print("===================================")
df_excel = pd.read_excel('data/my_excel.xlsx')
print(df_excel)

'''
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
2     6    c   2.5  orange  2020/1/5
3     5    d   3.2   lemon  2020/1/7
===================================
   col1 col2  col3             col4
0     2    a   1.4   apple 2020/1/1
1     3    b   3.4  banana 2020/1/2
2     6    c   2.5  orange 2020/1/5
3     5    d   3.2   lemon 2020/1/7
===================================
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
2     6    c   2.5  orange  2020/1/5
3     5    d   3.2   lemon  2020/1/7
'''
```

- 这里有一些常用的公共参数， `header=None` 表示第一行不作为列名， `index_col` 表示把某一列或几列作为索引，索引的内容将会在第三章进行详述， `usecols` 表示读取列的集合，默认读取所有的列， `parse_dates` 表示需要转化为时间的列，关于时间序列的有关内容将在第十章讲解， `nrows` 表示读取的数据行数。上面这些参数在上述的三个函数里都可以使用

```python 
# 设置参数
import numpy as np 
import pandas as pd 

df_txt1 = pd.read_table('data/my_table.txt',header = None)
print(df_txt1)
print("======================================")
df_csv1 = pd.read_csv('data/my_csv.csv',index_col = ['col1','col2'])
print(df_csv1)
print("======================================")
df_txt2 = pd.read_table('data/my_table.txt',usecols = ['col1','col2'])
print(df_txt2)
print("======================================")
df_csv2 = pd.read_csv('data/my_csv.csv',parse_dates = ['col5'])
print(df_csv2)
print("======================================")
df_excel1 = pd.read_excel('data/my_excel.xlsx',nrows = 2)
print(df_excel1)

'''
      0     1     2                3
0  col1  col2  col3             col4
1     2     a   1.4   apple 2020/1/1
2     3     b   3.4  banana 2020/1/2
3     6     c   2.5  orange 2020/1/5
4     5     d   3.2   lemon 2020/1/7
======================================
           col3    col4      col5
col1 col2                        
2    a      1.4   apple  2020/1/1
3    b      3.4  banana  2020/1/2
6    c      2.5  orange  2020/1/5
5    d      3.2   lemon  2020/1/7
======================================
   col1 col2
0     2    a
1     3    b
2     6    c
3     5    d
======================================
   col1 col2  col3    col4       col5
0     2    a   1.4   apple 2020-01-01
1     3    b   3.4  banana 2020-01-02
2     6    c   2.5  orange 2020-01-05
3     5    d   3.2   lemon 2020-01-07
======================================
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
'''
```

- 在读取 `txt` 文件时，经常遇到分隔符非空格的情况， `read_table` 有一个分割参数 `sep` ，它使得用户可以自定义分割符号，进行 `txt` 数据的读取。例如，下面的读取的表以 `||||` 为分割

```python
# 设置参数 sep
import numpy as np 
import pandas as pd 

df_txt = pd.read_table('data/my_table_special_sep.txt') # 不带sep参数
print(df_txt)

'''
              col1 |||| col2
0  TS |||| This is an apple.
1    GQ |||| My name is Bob.
2         WT |||| Well done!
3    PT |||| May I help you?
'''
```

上面的结果显然不是理想的，这时可以使用 `sep` ，同时需要指定引擎为 `python`

```python
# 使用sep 参数
import numpy as np 
import pandas as pd 

df_txt_sep =  pd.read_table('data/my_table_special_sep.txt',sep = ' \|\|\|\| ', engine = 'python') # 使用sep参数
print(df_txt_sep)

'''
  col1               col2
0   TS  This is an apple.
1   GQ    My name is Bob.
2   WT         Well done!
3   PT    May I help you?
'''
```

注意：`sep` 是正则参数

在使用 `read_table` 的时候需要注意，参数 `sep` 中使用的是正则表达式，因此需要对 `|` 进行转义变成 `\|` ，否则无法读取到正确的结果。有关正则表达式的基本内容可以参考第八章或者其他相关资料

#### 2. 数据写入

- 一般在数据写入中，最常用的操作是把 `index` 设置为 `False` ，特别当索引没有特殊意义的时候，这样的行为能把索引在保存的时候去除

```python 
# 数据写入
import numpy as np 
import pandas as pd 

df_csv = pd.read_csv('data/my_csv.csv')
print(df_csv)
df_csv.to_csv('data/yingrushi_csv.csv',index = False)
print("=======================================")
df_excel = pd.read_excel('data/my_excel.xlsx')
print(df_excel)
df_excel.to_excel('data/yingrushi_excel.xlsx',index = False)

'''
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
2     6    c   2.5  orange  2020/1/5
3     5    d   3.2   lemon  2020/1/7
=======================================
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
2     6    c   2.5  orange  2020/1/5
3     5    d   3.2   lemon  2020/1/7
'''
```

![image-20201217231843512](https://gitee.com/smithbee/image_bed/raw/master/image-20201217231843512.png)

- `pandas` 中没有定义 `to_table` 函数，但是 `to_csv` 可以保存为 `txt` 文件，并且允许自定义分隔符，常用制表符 `\t` 分割

```python 
# 写入txt文件
import numpy as np 
import pandas as pd 

df_txt = pd.read_table('data/my_table.txt')
print(df_txt)
df_txt.to_csv('data/yingrushi_txt.txt',sep = '\t',index = False)

'''
   col1 col2  col3             col4
0     2    a   1.4   apple 2020/1/1
1     3    b   3.4  banana 2020/1/2
2     6    c   2.5  orange 2020/1/5
3     5    d   3.2   lemon 2020/1/7
'''
```

![image-20201217232537158](https://gitee.com/smithbee/image_bed/raw/master/image-20201217232537158.png)

- 如果想要把表格快速转换为 `markdown` 和 `latex` 语言，可以使用 `to_markdown` 和 `to_latex` 函数，此处需要安装 `tabulate` 包

```python 
# 转换为markdown和latex
import numpy as np 
import pandas as pd 
import tabulate

df_csv = pd.read_csv('data/my_csv.csv')
print(df_csv)
print("=======================")
print(df_csv.to_markdown())
print("=======================")
print(df_csv.to_latex())

'''
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
2     6    c   2.5  orange  2020/1/5
3     5    d   3.2   lemon  2020/1/7
=======================
|    |   col1 | col2   |   col3 | col4   | col5     |
|---:|-------:|:-------|-------:|:-------|:---------|
|  0 |      2 | a      |    1.4 | apple  | 2020/1/1 |
|  1 |      3 | b      |    3.4 | banana | 2020/1/2 |
|  2 |      6 | c      |    2.5 | orange | 2020/1/5 |
|  3 |      5 | d      |    3.2 | lemon  | 2020/1/7 |
=======================
\begin{tabular}{lrlrll}
\toprule
{} &  col1 & col2 &  col3 &    col4 &      col5 \\
\midrule
0 &     2 &    a &   1.4 &   apple &  2020/1/1 \\
1 &     3 &    b &   3.4 &  banana &  2020/1/2 \\
2 &     6 &    c &   2.5 &  orange &  2020/1/5 \\
3 &     5 &    d &   3.2 &   lemon &  2020/1/7 \\
\bottomrule
\end{tabular}
'''
```

`to_markdown` 和 `to_latex` 函数 不能保存为文件，只能输出为代码，可以复制到markdown文件中

```
|    |   col1 | col2   |   col3 | col4   | col5     |
|---:|-------:|:-------|-------:|:-------|:---------|
|  0 |      2 | a      |    1.4 | apple  | 2020/1/1 |
|  1 |      3 | b      |    3.4 | banana | 2020/1/2 |
|  2 |      6 | c      |    2.5 | orange | 2020/1/5 |
|  3 |      5 | d      |    3.2 | lemon  | 2020/1/7 |
```

把上面的复制到markdown中，如下，上面是markdown语法。

|      | col1 | col2 | col3 | col4   | col5     |
| ---: | ---: | :--- | ---: | :----- | :------- |
|    0 |    2 | a    |  1.4 | apple  | 2020/1/1 |
|    1 |    3 | b    |  3.4 | banana | 2020/1/2 |
|    2 |    6 | c    |  2.5 | orange | 2020/1/5 |
|    3 |    5 | d    |  3.2 | lemon  | 2020/1/7 |

**latex** 类似



### 二、基本数据结构

`pandas` 中具有两种基本的数据存储结构，存储一维 `values` 的 `Series` 和存储二维 `values` 的 `DataFrame` ，在这两种结构上定义了很多的属性和方法

#### 1. Series

- `Series` 一般由四个部分组成，分别是序列的值 `data` 、索引 `index` 、存储类型 `dtype` 、序列的名字 `name` 。其中，索引也可以指定它的名字，默认为空

```python 
# Series 
import numpy as np 
import pandas as pd 

pd_series = pd.Series(data = [100,'a',{'dic1':5}],index = pd.Index(['id1',20,'third'],name = 'my_idx'),dtype = 'object',name = 'my_name')
print(pd_series)

'''
my_idx
id1              100
20                 a
third    {'dic1': 5}
Name: my_name, dtype: object
'''
```

注意：

`object` 代表了一种混合类型，正如上面的例子中存储了整数、字符串以及 `Python` 的字典数据结构。此外，目前 `pandas` 把纯字符串序列也默认认为是一种 `object` 类型的序列，但它也可以用 `string` 类型存储，文本序列的内容会在第八章中讨论

- 对于这些属性，可以通过 `.` 的方式来获取

```python
import numpy as np 
import pandas as pd 

pd_series = pd.Series(data = [100,'a',{'dic1':5}],index = pd.Index(['id1',20,'third'],name = 'my_idx'),dtype = 'object',name = 'my_name')
print(pd_series)
print("=====================")
print(pd_series.values)
print(pd_series.index)
print(pd_series.dtype)
print(pd_series.name)

'''
my_idx
id1              100
20                 a
third    {'dic1': 5}
Name: my_name, dtype: object
=====================
[100 'a' {'dic1': 5}]
Index(['id1', 20, 'third'], dtype='object', name='my_idx')
object
my_name

'''
```

- 利用 `.shape` 可以获取序列的长度 , 如果想要取出单个索引对应的值，可以通过 `Series[index_item]` 可以取出

```python 
# .shape
import numpy as np 
import pandas as pd 

pd_series = pd.Series(data = [100,'a',{'dic1':5}],index = pd.Index(['id1',20,'third'],name = 'my_idx'),dtype = 'object',name = 'my_name')
print(pd_series)
print("=====================")
print(pd_series.shape)

# 索引
print(pd_series[20])

'''
my_idx
id1              100
20                 a
third    {'dic1': 5}
Name: my_name, dtype: object
=====================
(3,)
a
'''
```

#### 2. DataFrame

`DataFrame` 在 `Series` 的基础上增加了列索引，一个数据框可以由二维的 `data` 与行列索引来构造

数据帧(**DataFrame**)是二维数据结构，即数据以行和列的表格方式排列

数据帧(DataFrame)的功能特点：

**(1) 潜在的列是不同的类型**

**(2) 大小可变**

**(3) 标记轴(行和列)**

**(4) 可以对行和列执行算术运算**

![image-20201218132403953](https://gitee.com/smithbee/image_bed/raw/master/image-20201218132403953.png)

- *pandas*中的`DataFrame`可以使用以下构造函数创建

`pandas.DataFrame( data, index, columns, dtype, copy) `

构造函数的参数如下:

![image-20201218132816904](https://gitee.com/smithbee/image_bed/raw/master/image-20201218132816904.png)

```python 
# dataframe
import numpy as np 
import pandas as pd 

data = [[1,'a',1.2],[2,'b',2.2],[3,'c',3.2]]
df = pd.DataFrame(data = data,index = ['row_%d' % i for i in range(3)],columns = ['col_0','col_1','col_2'])
print(df)

'''
       col_0 col_1  col_2
row_0      1     a    1.2
row_1      2     b    2.2
row_2      3     c    3.2
'''
```

但一般而言，更多的时候会采用从列索引名到数据的映射来构造数据框，同时再加上行索引

```python 
# 构造dataframe
import numpy as np 
import pandas as pd 

df = pd.DataFrame(data = {'col_0':[1,2,3],'col_1':list('abc'),'col2':[1.2,2.2,3.2]},index = ['row_%d' % i for i in range(3)])
print(df)

'''
       col_0 col_1  col2
row_0      1     a   1.2
row_1      2     b   2.2
row_2      3     c   3.2
'''
```

- 由于这种映射关系，在 `DataFrame` 中可以用 `[col_name]` 与 `[col_list]` 来取出相应的列与由多个列组成的表，结果分别为 `Series` 和 `DataFrame`

```python 
# 索引
import numpy as np 
import pandas as pd 

df = pd.DataFrame(data = {'col_0':[1,2,3],'col_1':list('abc'),'col2':[1.2,2.2,3.2]},index = ['row_%d' % i for i in range(3)])
print(df)
print("===============================")
print(df['col_0'])
print("===============================")
print(df[['col_0','col_1']])
print(type(df[['col_0','col_1']]))

'''
       col_0 col_1  col2
row_0      1     a   1.2
row_1      2     b   2.2
row_2      3     c   3.2
===============================
row_0    1
row_1    2
row_2    3
Name: col_0, dtype: int64
===============================
       col_0 col_1
row_0      1     a
row_1      2     b
row_2      3     c
<class 'pandas.core.frame.DataFrame'>
'''
```

与 `Series` 类似，在数据框中同样可以取出相应的属性

```python
# 索引
import numpy as np 
import pandas as pd 

df = pd.DataFrame(data = {'col_0':[1,2,3],'col_1':list('abc'),'col2':[1.2,2.2,3.2]},index = ['row_%d' % i for i in range(3)])
print(df)
print("===============================")
print(df.values)
print("===============================")
print(df.index)
print("===============================")
print(df.columns)
print("===============================")
print(df.dtypes)
print("===============================")
print(df.shape)

'''
       col_0 col_1  col2
row_0      1     a   1.2
row_1      2     b   2.2
row_2      3     c   3.2
===============================
[[1 'a' 1.2]
 [2 'b' 2.2]
 [3 'c' 3.2]]
===============================
Index(['row_0', 'row_1', 'row_2'], dtype='object')
===============================
Index(['col_0', 'col_1', 'col2'], dtype='object')
===============================
col_0      int64
col_1     object
col2     float64
dtype: object
===============================
(3, 3)
'''
```

- 通过 `.T` 可以把 `DataFrame` 进行转置

```python
# 转置
import numpy as np 
import pandas as pd 

df = pd.DataFrame(data = {'col_0':[1,2,3],'col_1':list('abc'),'col2':[1.2,2.2,3.2]},index = ['row_%d' % i for i in range(3)])
print(df)
print("===============================")
print(df.T)

'''
       col_0 col_1  col2
row_0      1     a   1.2
row_1      2     b   2.2
row_2      3     c   3.2
===============================
      row_0 row_1 row_2
col_0     1     2     3
col_1     a     b     c
col2    1.2   2.2   3.2
'''
```

#### 3. Panel（面板）(python3中已弃用)

**Pandas 面板**(**Panel**)是3维数据的存储结构，

`Panel` 相当于一个存储 `DataFrame` 的字典，3个轴（`axis`）分别代表意义如下:

|          |                |                                      |
| :------: | :------------: | :----------------------------------: |
| `axis 0` |   **items**    | item 对应一个内部的数据帧(DataFrame) |
| `axis 1` | **major_axis** |    每个数据帧(DataFrame)的索引行     |
| `axis 2` | **minor_axis** |    每个数据帧(DataFrame)的索引列     |

![image-20201218141337857](https://gitee.com/smithbee/image_bed/raw/master/image-20201218141337857.png)

- 可以使用以下构造函数创建 `Panel`

`pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)`

构造函数的参数如下：

|     参数     |                             说明                             |
| :----------: | :----------------------------------------------------------: |
|    `data`    | 支持多种数据类型，如：`ndarray`，`series`，`map`，`lists`，`dict`，`constant`和其他数据帧(`DataFrame`) |
|   `items`    |                           `axis=0`                           |
| `major_axis` |                           `axis=1`                           |
| `minor_axis` |                           `axis=2`                           |
|   `dtype`    |                        每列的数据类型                        |
|    `copy`    |                 是否复制数据，默认为`false`                  |

```python
# 创建Panel
import numpy as np 
import pandas as pd 

# 创建 空Panel
p = pd.Panel()
print(p)
print("========================")

# 从 3Dndarray 创建Panel
np.random.seed(20201218)
data = np.random.rand(2,4,5)
print(data)
print("========================")
p = pd.Panel()
print(p)

'''
<pandas.__getattr__.<locals>.Panel object at 0x0000019092A60320>
========================
[[[0.82053113 0.40822766 0.0043119  0.59250126 0.68065678]
  [0.41462002 0.63850114 0.84972809 0.83815841 0.49665225]
  [0.69873626 0.3915328  0.96118411 0.28867098 0.16603775]
  [0.18647815 0.21783024 0.223223   0.87727195 0.5078422 ]]

 [[0.72346079 0.72471709 0.62397643 0.60783676 0.17108011]
  [0.35284973 0.95773571 0.02642248 0.66253958 0.73585733]
  [0.94741633 0.38742025 0.00119016 0.95563109 0.05178133]
  [0.05578195 0.05838634 0.04496512 0.66466131 0.92483172]]]
========================
<pandas.__getattr__.<locals>.Panel object at 0x0000019092A608D0>
'''
```

### 三、常用基本函数

为了进行举例说明，在接下来的部分和其余章节都将会使用一份 `learn_pandas.csv` 的虚拟数据集，它记录了四所学校学生的体测个人信息

```python
# 常用函数
import numpy as np 
import pandas as pd

df = pd.read_csv('data/learn_pandas.csv')
print(df.columns)

'''
Index(['School', 'Grade', 'Name', 'Gender', 'Height', 'Weight', 'Transfer','Test_Number', 'Test_Date', 'Time_Record'],
dtype='object')
'''
```

上述列名依次代表学校、年级、姓名、性别、身高、体重、是否为转系生、体测场次、测试时间、1000米成绩，本章只需使用其中的前七列

```python 
# 使用数据
import numpy as np 
import pandas as pd

df = pd.read_csv('data/learn_pandas.csv')
df = df[df.columns[:7]]
print(df)

'''
                            School      Grade            Name  Gender  Height  \
0    Shanghai Jiao Tong University   Freshman    Gaopeng Yang  Female   158.9   
1                Peking University   Freshman  Changqiang You    Male   166.5   
2    Shanghai Jiao Tong University     Senior         Mei Sun    Male   188.9   
3                 Fudan University  Sophomore    Xiaojuan Sun  Female     NaN   
4                 Fudan University  Sophomore     Gaojuan You    Male   174.0   
..                             ...        ...             ...     ...     ...   
195               Fudan University     Junior    Xiaojuan Sun  Female   153.9   
196            Tsinghua University     Senior         Li Zhao  Female   160.9   
197  Shanghai Jiao Tong University     Senior  Chengqiang Chu  Female   153.9   
198  Shanghai Jiao Tong University     Senior   Chengmei Shen    Male   175.3   
199            Tsinghua University  Sophomore     Chunpeng Lv    Male   155.7   

     Weight Transfer  
0      46.0        N  
1      70.0        N  
2      89.0        N  
3      41.0        N  
4      74.0        N  
..      ...      ...  
195    46.0        N  
196    50.0        N  
197    45.0        N  
198    71.0        N  
199    51.0        N  

[200 rows x 7 columns]
'''
```

#### 1. 汇总函数

- `head, tail` 函数分别表示返回表或者序列的前 `n` 行和后 `n` 行，其中 `n` 默认为5

```python 
# 1.汇总函数
import numpy as np 
import pandas as pd 

print(df.head(2))
print("========================")
print(df.tail(3))

'''
                          School     Grade            Name  Gender  Height  \
0  Shanghai Jiao Tong University  Freshman    Gaopeng Yang  Female   158.9   
1              Peking University  Freshman  Changqiang You    Male   166.5   

   Weight Transfer  
0    46.0        N  
1    70.0        N  
========================
                            School      Grade            Name  Gender  Height  \
197  Shanghai Jiao Tong University     Senior  Chengqiang Chu  Female   153.9   
198  Shanghai Jiao Tong University     Senior   Chengmei Shen    Male   175.3   
199            Tsinghua University  Sophomore     Chunpeng Lv    Male   155.7   

     Weight Transfer  
197    45.0        N  
198    71.0        N  
199    51.0        N  
'''
```

- `info, describe` 分别返回表的 信息概况 和表中 数值列对应的主要统计量 

```python 
# info , describe
import numpy as np 
import pandas as pd 

print(df.info())
print("========================")
print(df.describe())

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   School    200 non-null    object 
 1   Grade     200 non-null    object 
 2   Name      200 non-null    object 
 3   Gender    200 non-null    object 
 4   Height    183 non-null    float64
 5   Weight    189 non-null    float64
 6   Transfer  188 non-null    object 
dtypes: float64(2), object(5)
memory usage: 11.1+ KB
None
========================
           Height      Weight
count  183.000000  189.000000
mean   163.218033   55.015873
std      8.608879   12.824294
min    145.400000   34.000000
25%    157.150000   46.000000
50%    161.900000   51.000000
75%    167.500000   65.000000
max    193.900000   89.000000
'''
```

注意：

`info, describe` 只能实现较少信息的展示，如果想要对一份数据集进行全面且有效的观察，特别是在列较多的情况下，推荐使用 [pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html) 包，它将在后面被再次提到

#### 2. 特征统计函数

- 在 `Series` 和 `DataFrame` 上定义了许多统计函数，最常见的是 `sum, mean, median, var, std, max, min` 。

例如，选出身高和体重列进行演示

```python 
# 统计函数
import numpy as np 
import pandas as pd 

df_demo = df[['Height','Weight']]
print(df_demo.mean()) # 均值
print(df_demo.max()) # 最大值
print(df_demo.min()) # 最小值

'''
Height    163.218033
Weight     55.015873
dtype: float64
Height    193.9
Weight     89.0
dtype: float64
Height    145.4
Weight     34.0
dtype: float64
'''
```

- 此外，需要介绍的是 `quantile, count, idxmax, idxmin` 这四个函数，它们分别返回的是分位数、非缺失值个数、最大值对应的索引

```python 
# quantile , count , idxmax , idxmin
import numpy as np 
import pandas as pd 

print(df_demo.quantile(0.75))
print(df_demo.count())
print(df_demo.idxmax())
print(df_demo.idxmin())

'''
Height    167.5
Weight     65.0
Name: 0.75, dtype: float64
Height    183
Weight    189
dtype: int64
Height    193
Weight      2
dtype: int64
Height    143
Weight     49
dtype: int64
'''
```

- 上面这些所有的函数，由于操作后返回的是标量，所以又称为聚合函数，它们有一个公共参数 `axis` ，默认为0代表逐列聚合，如果设置为1则表示逐行聚合

```python 
# axis 参数
import numpy as np 
import pandas as pd

# 只做演示，身高和体重的均值并没有意义
print(df_demo.mean(axis = 1).head()) # axis 按行聚合

'''
0    102.45
1    118.25
2    138.95
3     41.00
4    124.00
dtype: float64
'''
```

#### 3. 唯一值函数

- 对序列使用 `unique` 和 `nunique` 可以分别得到其唯一值组成的列表和唯一值的个数

```python 
# 唯一值函数
import numpy as np 
import pandas as pd 

print(df['School'].unique())
print(df['School'].nunique())

'''
['Shanghai Jiao Tong University' 'Peking University' 'Fudan University' 'Tsinghua University']
4
'''
```

- `value_counts` 可以得到唯一值和其对应出现的频数

```python
# 唯一值函数
import numpy as np 
import pandas as pd 

print(df['School'].value_counts())

'''
Tsinghua University              69
Shanghai Jiao Tong University    57
Fudan University                 40
Peking University                34
Name: School, dtype: int64
'''
```

- 如果想要观察多个列组合的唯一值，可以使用 `drop_duplicates` 。其中的关键参数是 `keep` ，默认值 `first` 表示每个组合保留第一次出现的所在行， `last` 表示保留最后一次出现的所在行， `False` 表示把所有重复组合所在的行剔除

```python
# drop_duplicates
import numpy as np 
import pandas as pd 

df_demo = df[['Gender','Transfer','Name']]
print(df_demo.drop_duplicates(['Gender','Transfer']))
print("=============================")
print(df_demo.drop_duplicates(['Gender','Transfer'],keep = 'last'))
print("=============================")
print(df_demo.drop_duplicates(['Name','Gender'],keep = False).head())
print("=============================")
print(df['School'].drop_duplicates()) # 在Series上也可以使用

'''
    Gender Transfer            Name
0   Female        N    Gaopeng Yang
1     Male        N  Changqiang You
12  Female      NaN        Peng You
21    Male      NaN   Xiaopeng Shen
36    Male        Y    Xiaojuan Qin
43  Female        Y      Gaoli Feng
=============================
     Gender Transfer            Name
147    Male      NaN        Juan You
150    Male        Y   Chengpeng You
169  Female        Y   Chengquan Qin
194  Female      NaN     Yanmei Qian
197  Female        N  Chengqiang Chu
199    Male        N     Chunpeng Lv
=============================
   Gender Transfer            Name
0  Female        N    Gaopeng Yang
1    Male        N  Changqiang You
2    Male        N         Mei Sun
4    Male        N     Gaojuan You
5  Female        N     Xiaoli Qian
=============================
0    Shanghai Jiao Tong University
1                Peking University
3                 Fudan University
5              Tsinghua University
Name: School, dtype: object
'''
```

- 此外， `duplicated` 和 `drop_duplicates` 的功能类似，但前者返回了是否为唯一值的布尔列表，其 `keep` 参数与后者一致。其返回的序列，把重复元素设为 `True` ，否则为 `False` 。 `drop_duplicates` 等价于把 `duplicated` 为 `True` 的对应行剔除

```python 
# duplicates 
import numpy as np 
import pandas as pd 

print(df_demo.duplicated(['Gender','Transfer']).head())
print("=========================")
print(df['School'].duplicated().head())  # 在 Series 上也可以使用

'''
0    False
1    False
2     True
3     True
4     True
dtype: bool
=========================
0    False
1    False
2     True
3    False
4     True
Name: School, dtype: bool
'''
```

#### 4. 替换函数

一般而言，替换操作是针对某一个列进行的，因此下面的例子都以 `Series` 举例。 `pandas` 中的替换函数可以归纳为三类：映射替换、逻辑替换、数值替换。其中映射替换包含 `replace` 方法、第八章中的 `str.replace` 方法以及第九章中的 `cat.codes` 方法，此处介绍 `replace` 的用法

- 在 `replace` 中，可以通过字典构造，或者传入两个列表来进行替换

```python
# 替换函数
import numpy as np 
import pandas as pd 

df = pd.read_csv('data/learn_pandas.csv')
df = df[df.columns[:7]]
print(df['Gender'].replace({'Female':0,'Male':1}).head()) # 通过字典替换
print("============================")
print(df['Gender'].replace(['Female','Male'],[0,1]).head()) # 通过两个列表替换

'''
0    0
1    1
2    1
3    0
4    1
Name: Gender, dtype: int64
============================
0    0
1    1
2    1
3    0
4    1
Name: Gender, dtype: int64
'''
```

- 另外， `replace` 还有一种特殊的方向替换，指定 `method` 参数为 `ffill` 则为用前面一个最近的未被替换的值进行替换， `bfill` 则使用后面最近的未被替换的值进行替换。从下面的例子可以看到，它们的结果是不同的

```python
# ffill bfill
import numpy as np 
import pandas as pd 

s = pd.Series(['a',1,'b',2,1,1,'a'])
print(s)
print("=====================")
print(s.replace([1,2],method = 'ffill'))
print("=====================")
print(s.replace([1,2],method = 'bfill'))

'''
0    a
1    1
2    b
3    2
4    1
5    1
6    a
dtype: object
=====================
0    a
1    a
2    b
3    b
4    b
5    b
6    a
dtype: object
=====================
0    a
1    b
2    b
3    a
4    a
5    a
6    a
dtype: object
'''
```

注意：虽然对于 `replace` 而言可以使用正则替换，但是当前版本下对于 `string` 类型的正则替换还存在 [bug](https://github.com/pandas-dev/pandas/pull/36038) ，因此如有此需求，请选择 `str.replace` 进行替换操作，具体的方式将在后面中学习

- 逻辑替换包括了 `where` 和 `mask` ，这两个函数是完全对称的： `where` 函数在传入条件为 `False` 的对应行进行替换，而 `mask` 在传入条件为 `True` 的对应行进行替换，当不指定替换值时，替换为缺失值

```python 
# 逻辑替换 where mask 
import numpy as np 
import pandas as pd 

s = pd.Series([-1,1.2345,100,-50])
print(s)
print("=====================")
print(s.where(s < 0))
print("=====================")
print(s.where(s < 0,100))
print("=====================")
print(s.mask(s < 0))
print("=====================")
print(s.mask(s < 0,-50))

'''
0     -1.0000
1      1.2345
2    100.0000
3    -50.0000
dtype: float64
=====================
0    -1.0
1     NaN
2     NaN
3   -50.0
dtype: float64
=====================
0     -1.0
1    100.0
2    100.0
3    -50.0
dtype: float64
=====================
0         NaN
1      1.2345
2    100.0000
3         NaN
dtype: float64
=====================
0    -50.0000
1      1.2345
2    100.0000
3    -50.0000
dtype: float64
'''
```

需要注意的是，传入的条件只需是与被调用的 `Series` 索引一致的布尔序列即可

```python
# 传入Series索引一致的布尔序列
import numpy as np 
import pandas as pd 

s = pd.Series([-1,1.2345,100,-50])
s_condition = pd.Series([True,False,False,True],index = s.index)
print(s.mask(s_condition,-50)) 

'''
0    -50.0000
1      1.2345
2    100.0000
3    -50.0000
dtype: float64
'''
```

- 数值替换包含了 `round, abs, clip` 方法，它们分别表示按照给定精度四舍五入、取绝对值和截断

```python 
# 数值替换
import numpy as np 
import pandas as pd 

s = pd.Series([-1,1.2345,100,-50]) # 按精度四舍五入
print(s.round(2))
print("======================")
print(s.abs())
print("======================")
print(s.clip(0,2)) # 前两个数分别表示上下截断边界

'''
0     -1.00
1      1.23
2    100.00
3    -50.00
dtype: float64
======================
0      1.0000
1      1.2345
2    100.0000
3     50.0000
dtype: float64
======================
0    0.0000
1    1.2345
2    2.0000
3    0.0000
dtype: float64
'''
```

注意：

在 `clip` 中，超过边界的只能截断为边界值，如果要把超出边界的替换为自定义的值，应当如何做

使用两次 `where` 或 `mask` 函数



#### 5. 排序函数

排序共有两种方式，其一为值排序，其二为索引排序，对应的函数是 `sort_values` 和 `sort_index` 

- 为了演示排序函数，下面先利用 `set_index` 方法把年级和姓名两列作为索引，多级索引的内容和索引设置的方法将在第三章进行详细讲解

对身高进行排序，默认参数 `ascending=True` 为升序

```python 
# 排序函数
import numpy as np 
import pandas as pd 

df_demo = df[['Grade','Name','Height','Weight']].set_index(['Grade','Name'])
# 对身高进行排序
print(df_demo.sort_values('Height').head())
print("==========================")
print(df_demo.sort_values('Height',ascending = False).head())

'''
                         Height  Weight
Grade     Name                         
Junior    Xiaoli Chu      145.4    34.0
Senior    Gaomei Lv       147.3    34.0
Sophomore Peng Han        147.8    34.0
Senior    Changli Lv      148.7    41.0
Sophomore Changjuan You   150.5    40.0
==========================
                        Height  Weight
Grade    Name                         
Senior   Xiaoqiang Qin   193.9    79.0
         Mei Sun         188.9    89.0
         Gaoli Zhao      186.5    83.0
Freshman Qiang Han       185.3    87.0
Senior   Qiang Zheng     183.9    87.0
'''
```

- 在排序中，经常遇到多列排序的问题，比如在体重相同的情况下，对身高进行排序，并且保持身高降序排列，体重升序排列

```python 
# 多列排序
import numpy as np 
import pandas as pd 

# 体重相同的情况下，对身高进行排序，并且保持身高降序排列，体重升序排列
print(df_demo.sort_values(['Weight','Height'],ascending = [True,False]).head())

'''
                       Height  Weight
Grade     Name                       
Sophomore Peng Han      147.8    34.0
Senior    Gaomei Lv     147.3    34.0
Junior    Xiaoli Chu    145.4    34.0
Sophomore Qiang Zhou    150.5    36.0
Freshman  Yanqiang Xu   152.4    38.0
'''
```

- 索引排序的用法和值排序完全一致，只不过元素的值在索引中，此时需要指定索引层的名字或者层号，用参数 `level` 表示。另外，需要注意的是字符串的排列顺序由字母顺序决定

```python 
# 索引排序
import numpy as np 
import pandas as pd 

print(df_demo.sort_index(level = ['Grade','Name'],ascending = [True,False]).head())

'''
                        Height  Weight
Grade    Name                         
Freshman Yanquan Wang    163.5    55.0
         Yanqiang Xu     152.4    38.0
         Yanqiang Feng   162.3    51.0
         Yanpeng Lv        NaN    65.0
         Yanli Zhang     165.1    52.0
'''
```

#### 6. apply方法

`apply` 方法常用于 `DataFrame` 的行迭代或者列迭代，它的 `axis` 含义与第2小节中的统计聚合函数一致， `apply` 的参数往往是一个以序列为输入的函数。

- pandas 的 `apply()` 函数可以作用于 `Series` 或者整个 `DataFrame`，功能也是自动遍历整个 `Series` 或者 `DataFrame`, 对每一个元素运行指定的函数

例如对于 `.mean()` ，使用 `apply` 可以如下地写出

```python
# apply函数
import numpy as np 
import pandas as pd 

df = pd.read_csv('data/learn_pandas.csv')
df = df[df.columns[:7]]
df_demo = df[['Height','Weight']]
# 定义函数
def my_mean(x):
    return x.mean()

print(df_demo.apply(my_mean))

'''
Height    163.218033
Weight     55.015873
dtype: float64
'''
```

- 同样的，可以利用 `lambda` 表达式使得书写简洁，这里的 `x` 就指代被调用的 `df_demo` 表中逐个输入的序列

```python 
# apply 函数 lambda
import numpy as np 
import pandas as pd 

print(df_demo.apply(lambda x:x.mean()))

'''
Height    163.218033
Weight     55.015873
dtype: float64
'''
```

- 若指定 `axis=1` ，那么每次传入函数的就是行元素组成的 `Series` ，其结果与之前的逐行均值结果一致

```python
# 改变axis = 1 参数
import numpy as np 
import pandas as pd 

print(df_demo.apply(lambda x:x.mean(),axis = 1).head())

'''
0    102.45
1    118.25
2    138.95
3     41.00
4    124.00
dtype: float64
'''
```

- `mad` 函数返回的是一个序列中偏离该序列均值的绝对值大小的均值，例如序列1,3,7,10中，均值为5.25，每一个元素偏离的绝对值为4.25,2.25,1.75,4.75，这个偏离序列的均值为3.25。现在利用 `apply` 计算身高和体重的 `mad` 指标

```python 
# mad函数
import numpy as np 
import pandas as pd 

# 普通方法计算 mad 值
print(df_demo.apply(lambda x:(x - x.mean()).abs().mean()))

print("===================")
# 使用内置 mad 函数
print(df_demo.mad())

'''
Height     6.707229
Weight    10.391870
dtype: float64
===================
Height     6.707229
Weight    10.391870
dtype: float64
'''
```

注意：

谨慎使用 `apply`

得益于传入自定义函数的处理， `apply` 的自由度很高，但这是以性能为代价的。一般而言，使用 `pandas` 的内置函数处理和 `apply` 来处理同一个任务，其速度会相差较多，因此只有在确实存在自定义需求的情境下才考虑使用 `apply`

### 四、窗口对象

`pandas` 中有3类窗口，分别是滑动窗口 `rolling` 、扩张窗口 `expanding` 以及指数加权窗口 `ewm` 。需要说明的是，以日期偏置为窗口大小的滑动窗口将在第十章讨论，指数加权窗口见后面练习

#### 1. 概念

- 为了处理数字数据，Pandas提供了几个变体，如滚动，展开和指数移动窗口统计的权重。 其中包括总和，均值，中位数，方差，协方差，相关性等；

- 所谓窗口，就是将某个点的取值扩大到包含这个点的一段区间，用区间来进行判断；

- 移动窗口就是窗口向一端滑行，默认是从右往左，每次滑行并不是区间整块的滑行，而是一个单位一个单位的滑行；

- 窗口函数主要用于通过平滑曲线来以图形方式查找数据内的趋势。如果日常数据中有很多变化，并且有很多数据点可用，那么采样和绘图就是一种方法，应用窗口计算并在结果上绘制图形是另一种方法。 通过这些方法，可以平滑曲线或趋势。

#### 2. 滑窗对象

- 要使用滑窗函数，就必须先要对一个序列使用 `.rolling` 得到滑窗对象，其最重要的参数为窗口大小 `window`

```python 
# 滑窗对象
import numpy as np 
import pandas as pd 

s = pd.Series([1,2,3,4,5])
print(s)
roller = s.rolling(window = 3)
print(roller)

'''
0    1
1    2
2    3
3    4
4    5
dtype: int64
Rolling [window=3,center=False,axis=0]
'''
```

- 在得到了滑窗对象后，能够使用相应的聚合函数进行计算，需要注意的是窗口包含当前行所在的元素，例如在第四个位置进行均值运算时，应当计算(2+3+4)/3，而不是(1+2+3)/3

```python  
# roller 
import numpy as np 
import pandas as pandas 

s = pd.Series([1,2,3,4,5])
print(s)
print("=========================")
roller = s.rolling(window = 3)
print(roller.mean()) # 均值
print("=========================")
print(roller.sum()) # 求和

'''
0    1
1    2
2    3
3    4
4    5
dtype: int64
=========================
0    NaN
1    NaN
2    2.0     (1+2+3)/3
3    3.0     (2+3+4)/3
4    4.0
dtype: float64
=========================
0     NaN
1     NaN
2     6.0     1+2+3
3     9.0     2+3+4
4    12.0
dtype: float64
'''
```

- 对于滑动相关系数或滑动协方差的计算，可以如下写出

```python 
# 滑动相关系数和滑动协方差
import numpy as np 
import pandas as pd 

s = pd.Series([1,2,3,4,5])
print(s)
print("=========================")
roller = s.rolling(window = 3)
s2 = pd.Series([1,2,6,16,30])
print(s2)
print("==========================")

print(roller.cov(s2))  # 滑动协方差
print("==========================")
print(roller.corr(s2))  # 滑动相关系数

'''
0    1
1    2
2    3
3    4
4    5
dtype: int64
=========================
0     1
1     2
2     6
3    16
4    30
dtype: int64
==========================
0     NaN
1     NaN
2     2.5
3     7.0
4    12.0
dtype: float64
==========================
0         NaN
1         NaN
2    0.944911
3    0.970725
4    0.995402
dtype: float64
'''
```

- 此外，还支持使用 `apply` 传入自定义函数，其传入值是对应窗口的 `Series` ，例如上述的均值函数可以等效表示

```python 
# 滑动窗口使用 apply 
import numpy as np 
import pandas as pd 

# 不适用 apply 函数
print(roller.mean())
print("=======================")
# 使用 apply 函数
print(roller.apply(lambda x:x.mean()))

'''
0    NaN
1    NaN
2    2.0
3    3.0
4    4.0
dtype: float64
=======================
0    NaN
1    NaN
2    2.0
3    3.0
4    4.0
dtype: float64
'''
```

- `shift, diff, pct_change` 是一组类滑窗函数，它们的公共参数为 `periods=n` ，默认为1，分别表示取向前第 `n` 个元素的值、与向前第 `n` 个元素做差（与 `Numpy` 中不同，后者表示 `n` 阶差分）、与向前第 `n` 个元素相比计算增长率。这里的 `n` 可以为负，表示反方向的类似操作

(1) `shift`  :  **shift**函数是对数据进行移动的操作

(2) `diff`    :  **diff**函数是用来将数据进行某种移动之后与原数据进行比较得出的差异数据

(3) `pct_change`   :  **pct_change**函数表示当前元素与先前元素的相差百分比，当然指定periods=n,表示当前元素与先前n 个元素的相差百分比

```python 
# 类滑窗函数 
import numpy as np 
import pandas as pd 

s = pd.Series([1,3,6,10,15])
print(s)
print("======================")
print(s.shift(2))  # shift 函数
print("======================")
print(s.diff(3))   # diff 函数
print("======================")
print(s.pct_change())  # pct_change 函数
print("======================")
print(s.shift(-1))
print("======================")
print(s.diff(-2))

'''
0     1
1     3
2     6
3    10
4    15
dtype: int64
======================
0    NaN
1    NaN
2    1.0   向后移 2 位
3    3.0
4    6.0
dtype: float64
======================
0     NaN
1     NaN
2     NaN
3     9.0   向后移 3 位 原数据与之做差  s - s.shift(3)  10 - 1 = 9
4    12.0
dtype: float64
======================
0         NaN
1    2.000000   向后移 1 位 （原数据 - 现数据）/ 现数据 (3 - 1)/1 = 2
2    1.000000
3    0.666667
4    0.500000
dtype: float64
======================
0     3.0
1     6.0
2    10.0
3    15.0
4     NaN
dtype: float64
======================
0   -5.0
1   -7.0
2   -9.0
3    NaN
4    NaN
dtype: float64
'''
```

- 将其视作类滑窗函数的原因是，它们的功能可以用窗口大小为 `n+1` 的 `rolling` 方法等价代替

```python 
import numpy as np 
import pandas as pd 

s = pd.Series([1,3,6,10,15])
print(s)
print("======================")
print(s.rolling(3).apply(lambda x:list(x)[0]))  # s.shift(2)
print("======================")
print(s.rolling(4).apply(lambda x:list(x)[-1] - list(x)[0])) # s.diff(3)
print("======================")
def my_pct(x):
    L = list(x)
    return L[-1]/L[0] - 1

print(s.rolling(2).apply(my_pct)) # s.pct_change()

'''
0     1
1     3
2     6
3    10
4    15
dtype: int64
======================
0    NaN
1    NaN
2    1.0
3    3.0
4    6.0
dtype: float64
======================
0     NaN
1     NaN
2     NaN
3     9.0
4    12.0
dtype: float64
======================
0         NaN
1    2.000000
2    1.000000
3    0.666667
4    0.500000
dtype: float64

'''
```

练一练：

`rolling` 对象的默认窗口方向都是向前的，某些情况下用户需要向后的窗口，例如对1,2,3设定向后窗口为2的 `sum` 操作，结果为3,5,NaN，此时应该如何实现向后的滑窗操作

```

```



#### 3. 扩张窗口

扩张窗口又称累计窗口，可以理解为一个动态长度的窗口，其窗口的大小就是从序列开始处到具体操作的对应位置，其使用的聚合函数会作用于这些逐步扩张的窗口上。具体地说，设序列为a1, a2, a3, a4，则其每个位置对应的窗口即[a1]、[a1, a2]、[a1, a2, a3]、[a1, a2, a3, a4]

```python 
# 扩张窗口
import numpy as np 
import pandas as pd 

s = pd.Series([1,3,6,10])
print(s.expanding().mean())

'''
0    1.000000
1    2.000000
2    3.333333
3    5.000000
dtype: float64
'''
```

练一练：

`cummax, cumsum, cumprod` 函数是典型的类扩张窗口函数，请使用 `expanding` 对象依次实现它们

```

```





### 五、练习

#### 1. 口袋妖怪数据集

**题目说明：**

现有一份口袋妖怪的数据集，下面进行一些背景说明：

- `#` 代表全国图鉴编号，不同行存在相同数字则表示为该妖怪的不同状态
- 妖怪具有单属性和双属性两种，对于单属性的妖怪， `Type 2` 为缺失值
- `Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed` 分别代表种族值、体力、物攻、防御、特攻、特防、速度，其中种族值为后6项之和

**读取文件：**

```python
# 练习1 口袋妖怪数据集
import numpy as np 
import pandas as pd 

df = pd.read_csv('data/Pokemon.csv')
print(df.head())

'''
  #                   Name Type 1  Type 2  ...  Defense  Sp. Atk  Sp. Def  Speed
0  1              Bulbasaur  Grass  Poison  ...       49       65       65     45
1  2                Ivysaur  Grass  Poison  ...       63       80       80     60
2  3               Venusaur  Grass  Poison  ...       83      100      100     80
3  3  VenusaurMega Venusaur  Grass  Poison  ...      123      122      120     80
4  4             Charmander   Fire     NaN  ...       43       60       50     65

[5 rows x 11 columns]
'''
```

**问题解答：**

(1)  对 `HP, Attack, Defense, Sp. Atk, Sp. Def, Speed` 进行加总，验证是否为 `Total` 值

```python
# (1)
import numpy as np 
import pandas as pd 

df = pd.read_csv('data/Pokemon.csv')

df[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']].sum(axis = 1).head(10) == df['Total'].head(10)

'''
0    True
1    True
2    True
3    True
4    True
5    True
6    True
7    True
8    True
9    True
dtype: bool
'''
```

(2)  对于 `#` 重复的妖怪只保留第一条记录，解决以下问题：

i. 求第一属性的种类数量和前三多数量对应的种类

ii. 求第一属性和第二属性的组合种类

iii. 求尚未出现过的属性组合

```python 
# (2)
import numpy as np 
import pandas as pd 

df = pd.read_csv('data/Pokemon.csv')

# 只保留第一条记录
df_unique = df.drop_duplicates(['#'],keep = 'first')
print(df_unique.head(5))
# a. 第一属性的种类数量
print(df_unique['Type 1'].nunique())
# a. 前三多数量对应的种类
print(df_unique['Type 1'].value_counts().index[:3])
# b. 第一属性和第二属性的组合种类
df_type_sum = df_unique.drop_duplicates(['Type 1','Type 2'])
# print(df_type_sum.sum()) # unhashable type: 'list'
print(df_type_sum.shape[0])
# c. 尚未出现过的属性组合
L_full = [i+' '+j for i in df['Type 1'].unique() for j in (df['Type 1'].unique().tolist() + [''])]
L_part = [i+' '+j for i, j in zip(df['Type 1'], df['Type 2'].replace(np.nan, ''))]
res = set(L_full).difference(set(L_part))
print(len(res))

'''
   #        Name Type 1  Type 2  ...  Defense  Sp. Atk  Sp. Def  Speed
0  1   Bulbasaur  Grass  Poison  ...       49       65       65     45
1  2     Ivysaur  Grass  Poison  ...       63       80       80     60
2  3    Venusaur  Grass  Poison  ...       83      100      100     80
4  4  Charmander   Fire     NaN  ...       43       60       50     65
5  5  Charmeleon   Fire     NaN  ...       58       80       65     80

[5 rows x 11 columns]
18
Index(['Water', 'Normal', 'Grass'], dtype='object')
143
188
'''
```

(3) 按照下述要求，构造 `Series` ：

i. 取出物攻，超过120的替换为 `high` ，不足50的替换为 `low` ，否则设为 `mid`

ii. 取出第一属性，分别用 `replace` 和 `apply` 替换所有字母为大写

iii. 求每个妖怪六项能力的离差，即所有能力中偏离中位数最大的值，添加到 `df` 并从大到小排序

```python 
# (3)
import numpy as np 
import pandas as pd 

df = pd.read_csv('data/Pokemon.csv')

# a. 
#print(df.mask(df['Attack'] > 120,'high').mask(df['Attack'] < 50,'low').mask(df['Attack'] >= 50 and df['Attack'] <= 120,'mid')) #The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
#print(df['Attack'].mask(df['Attack'] > 120,'high').mask(df['Attack'] < 50,'low').mask(df['Attack'] >= 50 and df['Attack'] <= 120,'mid'))
print(df['Attack'].mask(df['Attack']>120, 'high').mask(df['Attack']<50, 'low').mask((50<=df['Attack'])&(df['Attack']<=120), 'mid').head())
print("================================")
# b.
print(df['Type 1'].replace({i:str.upper(i) for i in df['Type 1'].unique()}).head())
print(df['Type 1'].apply(lambda x:str.upper(x)).head())
print("================================")
# c.
df['Deviation'] = df[['HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed']].apply(lambda x:np.max((x-x.median()).abs()), 1)
print(df.sort_values('Deviation', ascending=False).head())

'''
0    low
1    mid
2    mid
3    mid
4    mid
Name: Attack, dtype: object
================================
0    GRASS
1    GRASS
2    GRASS
3    GRASS
4     FIRE
Name: Type 1, dtype: object
0    GRASS
1    GRASS
2    GRASS
3    GRASS
4     FIRE
Name: Type 1, dtype: object
================================
       #                 Name  Type 1  ... Sp. Def  Speed  Deviation
230  213              Shuckle     Bug  ...     230      5      215.0
121  113              Chansey  Normal  ...     105     50      207.5
261  242              Blissey  Normal  ...     135     55      190.0
333  306    AggronMega Aggron   Steel  ...      80     50      155.0
224  208  SteelixMega Steelix   Steel  ...      95     30      145.0

[5 rows x 12 columns]
'''
```



#### 2. 指数加权窗口

问题一：作为扩张窗口的 `ewm` 窗口

在扩张窗口中，用户可以使用各类函数进行历史的累计指标统计，但这些内置的统计函数往往把窗口中的所有元素赋予了同样的权重。事实上，可以给出不同的权重来赋给窗口中的元素，指数加权窗口就是这样一种特殊的扩张窗口。

![image-20201219230537167](https://gitee.com/smithbee/image_bed/raw/master/image-20201219230537167.png)

对于 `Series` 而言，可以用 `ewm` 对象如下计算指数平滑后的序列：

```python 
# 作为扩张窗口的 ewm 窗口
import numpy as np 
import pandas as pd

np.random.seed(0)
s = pd.Series(np.random.randint(-1,2,30).cumsum())
print(s.head())
print(s.ewm(alpha=0.2).mean().head())

'''
0   -1
1   -1
2   -2
3   -2
4   -2
dtype: int32
0   -1.000000
1   -1.000000
2   -1.409836
3   -1.609756
4   -1.725845
dtype: float64
'''
```

用 `expanding` 窗口实现:

```python 
# 1. 
import numpy as np 
import pandas as pd 

np.random.seed(0)
s = pd.Series(np.random.randint(-1,2,30).cumsum())
print(s.ewm(alpha=0.2).mean().head())

def ewm_func(x, alpha=0.2):
    win = (1-alpha)**np.arange(x.shape[0])[::-1]
    res = (win*x).sum()/win.sum()
    return res

print(s.expanding().apply(ewm_func).head())

'''
0   -1.000000
1   -1.000000
2   -1.409836
3   -1.609756
4   -1.725845
dtype: float64
0   -1.000000
1   -1.000000
2   -1.409836
3   -1.609756
4   -1.725845
dtype: float64
'''
```



问题二：作为滑动窗口的 `ewm` 窗口

从第1问中可以看到， `ewm` 作为一种扩张窗口的特例，只能从序列的第一个元素开始加权。现在希望给定一个限制窗口 `n` ，只对包含自身的最近的 `n` 个元素作为窗口进行滑动加权平滑。请根据滑窗函数，给出新的 wiwi 与 ytyt 的更新公式，并通过 `rolling` 窗口实现这一功能。

![image-20201219231411135](https://gitee.com/smithbee/image_bed/raw/master/image-20201219231411135.png)

```python 
# 2. 
import numpy as np 
import pandas as pd 

np.random.seed(0)
s = pd.Series(np.random.randint(-1,2,30).cumsum())

def ewm_func(x, alpha=0.2):
    win = (1-alpha)**np.arange(x.shape[0])[::-1]
    res = (win*x).sum()/win.sum()
    return res

print(s.rolling(window=4).apply(ewm_func).head())

'''
0         NaN
1         NaN
2         NaN
3   -1.609756
4   -1.826558
dtype: float64
'''
```

