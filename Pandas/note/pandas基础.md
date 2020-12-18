## pandas基础

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

