## Numpy大作业

本次练习使用 鸢尾属植物数据集，在这个数据集中，包括了三类不同的鸢尾属植物：Iris Setosa，Iris Versicolour，Iris Virginica。每类收集了50个样本，因此这个数据集一共包含了150个样本。

### **1. 导入鸢尾属植物数据集，保持文本不变。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=object, delimiter=',', skiprows=1)
print(iris_data[0:10])
# [['5.1' '3.5' '1.4' '0.2' 'Iris‐setosa']
# ['4.9' '3.0' '1.4' '0.2' 'Iris‐setosa']
# ['4.7' '3.2' '1.3' '0.2' 'Iris‐setosa']
# ['4.6' '3.1' '1.5' '0.2' 'Iris‐setosa']
# ['5.0' '3.6' '1.4' '0.2' 'Iris‐setosa']
# ['5.4' '3.9' '1.7' '0.4' 'Iris‐setosa']
# ['4.6' '3.4' '1.4' '0.3' 'Iris‐setosa']
# ['5.0' '3.4' '1.5' '0.2' 'Iris‐setosa']
# ['4.4' '2.9' '1.4' '0.2' 'Iris‐setosa']
# ['4.9' '3.1' '1.5' '0.1' 'Iris‐setosa']]
1234567891011121314
```

### **2. 求出鸢尾属植物萼片长度的平均值、中位数和标准差（第1列，sepallength）**

```python
import numpy as np
outfile = r'.\iris.data'
sepalLength = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0])
print(sepalLength[0:10])
# [5.1 4.9 4.7 4.6 5. 5.4 4.6 5. 4.4 4.9]
print(np.mean(sepalLength))
# 5.843333333333334
print(np.median(sepalLength))
# 5.8
print(np.std(sepalLength))
# 0.8253012917851409
1234567891011
```

### **3. 创建一种标准化形式的鸢尾属植物萼片长度，其值正好介于0和1之间，这样最小值为0，最大值为1（第1列，sepallength）。**

```python
import numpy as np
outfile = r'.\iris.data'
sepalLength = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0])
# 方法1
aMax = np.amax(sepalLength)
aMin = np.amin(sepalLength)
x = (sepalLength ‐ aMin) / (aMax ‐ aMin)
print(x[0:10])
# [0.22222222 0.16666667 0.11111111 0.08333333 0.19444444 0.30555556
# 0.08333333 0.19444444 0.02777778 0.16666667]
# 方法2
x = (sepalLength ‐ aMin) / np.ptp(sepalLength)
print(x[0:10])
# [0.22222222 0.16666667 0.11111111 0.08333333 0.19444444 0.30555556
# 0.08333333 0.19444444 0.02777778 0.16666667]
123456789101112131415
```

### **4. 找到鸢尾属植物萼片长度的第5和第95百分位数（第1列，sepallength）。**

```python
import numpy as np
outfile = r'.\iris.data'
sepalLength = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0])
x = np.percentile(sepalLength, [5, 95])
print(x) # [4.6 7.255]
12345
```

### **5. 把iris_data数据集中的20个随机位置修改为np.nan值。**

```python
import numpy as np
outfile = r'.\iris.data'
# 方法1
iris_data = np.loadtxt(outfile, dtype=object, delimiter=',', skiprows=1)
i, j = iris_data.shape
np.random.seed(20200621)
iris_data[np.random.randint(i, size=20), np.random.randint(j, size=20)] = np.nan
print(iris_data[0:10])
# [['5.1' '3.5' '1.4' '0.2' 'Iris‐setosa']
# ['4.9' '3.0' '1.4' '0.2' 'Iris‐setosa']
# ['4.7' '3.2' '1.3' '0.2' 'Iris‐setosa']
# ['4.6' '3.1' '1.5' '0.2' 'Iris‐setosa']
# ['5.0' '3.6' '1.4' '0.2' 'Iris‐setosa']
# ['5.4' nan '1.7' '0.4' 'Iris‐setosa']
# ['4.6' '3.4' '1.4' '0.3' 'Iris‐setosa']
# ['5.0' '3.4' '1.5' '0.2' 'Iris‐setosa']
# ['4.4' '2.9' '1.4' '0.2' nan]
# ['4.9' '3.1' '1.5' '0.1' 'Iris‐setosa']]
123456789101112131415161718
```

### **6. 在iris_data的sepallength中查找缺失值的个数和位置（第1列）。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2, 3])
i, j = iris_data.shape
np.random.seed(20200621)
iris_data[np.random.randint(i, size=20), np.random.randint(j, size=20)] = np.nan
sepallength = iris_data[:, 0]
x = np.isnan(sepallength)
print(sum(x)) # 6
print(np.where(x))
# (array([ 26, 44, 55, 63, 90, 115], dtype=int64),)
1234567891011
```

### **7. 筛选具有 sepallength（第1列）< 5.0 并且 petallength（第3列）> 1.5 的 iris_data行。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
sepallength = iris_data[:, 0]
petallength = iris_data[:, 2]
index = np.where(np.logical_and(petallength > 1.5, sepallength < 5.0))
print(iris_data[index])
# [[4.8 3.4 1.6 0.2]
# [4.8 3.4 1.9 0.2]
# [4.7 3.2 1.6 0.2]
# [4.8 3.1 1.6 0.2]
# [4.9 2.4 3.3 1. ]
# [4.9 2.5 4.5 1.7]]
1234567891011121314
```

### **8. 选择没有任何 nan 值的 iris_data行。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
i, j = iris_data.shape
np.random.seed(20200621)
iris_data[np.random.randint(i, size=20), np.random.randint(j, size=20)] = np.nan
x = iris_data[np.sum(np.isnan(iris_data), axis=1) == 0]
print(x[0:10])
# [[5.1 3.5 1.4 0.2]
# [4.9 3. 1.4 0.2]
# [4.7 3.2 1.3 0.2]
# [4.6 3.1 1.5 0.2]
# [5. 3.6 1.4 0.2]
# [4.6 3.4 1.4 0.3]
# [5. 3.4 1.5 0.2]
# [4.9 3.1 1.5 0.1]
# [5.4 3.7 1.5 0.2]
# [4.8 3.4 1.6 0.2]]
12345678910111213141516171819
```

### **9. 计算 iris_data 中sepalLength（第1列）和petalLength（第3列）之间的相关系数。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
sepalLength = iris_data[:, 0]
petalLength = iris_data[:, 2]
# 方法1
m1 = np.mean(sepalLength)
m2 = np.mean(petalLength)
cov = np.dot(sepalLength ‐ m1, petalLength ‐ m2)
std1 = np.sqrt(np.dot(sepalLength ‐ m1, sepalLength ‐ m1))
std2 = np.sqrt(np.dot(petalLength ‐ m2, petalLength ‐ m2))
print(cov / (std1 * std2)) # 0.8717541573048712
12345678910111213
```

### **10. 找出iris_data是否有任何缺失值。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
x = np.isnan(iris_data)
print(np.any(x)) # False
123456
```

### **11. 在numpy数组中将所有出现的nan替换为0。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
i, j = iris_data.shape
np.random.seed(20200621)
iris_data[np.random.randint(i, size=20), np.random.randint(j, size=20)] = np.nan
iris_data[np.isnan(iris_data)] = 0
print(iris_data[0:10])
# [[5.1 3.5 1.4 0.2]
# [4.9 3. 1.4 0.2]
# [4.7 3.2 1.3 0.2]
# [4.6 3.1 1.5 0.2]
# [5. 3.6 1.4 0.2]
# [5.4 0. 1.7 0.4]
# [4.6 3.4 1.4 0.3]
# [5. 3.4 1.5 0.2]
# [4.4 2.9 0. 0.2]
# [4.9 3.1 1.5 0.1]]
12345678910111213141516171819
```

### **12. 找出鸢尾属植物物种中的唯一值和唯一值出现的数量。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=object, delimiter=',', skiprows=1, usecols=[4])
x = np.unique(iris_data, return_counts=True)
print(x)
# (array(['Iris‐setosa', 'Iris‐versicolor', 'Iris‐virginica'], dtype=object), array([50,
50, 50], dtype=int64))
1234567
```

### **13. 将 iris_data 的花瓣长度（第3列）以形成分类变量的形式显示。定义：Less than 3 -->‘small’；3-5 --> ‘medium’；’>=5 --> ‘large’。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
petal_length_bin = np.digitize(iris_data[:, 2], [0, 3, 5, 10])
label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
petal_length_cat = [label_map[x] for x in petal_length_bin]
print(petal_length_cat[0:10])
# ['small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small',
'small']
12345678910
```

### **14. 在 iris_data 中创建一个新列，其中 volume 是 (pi x petallength x sepallength ^ 2）/ 3 。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=object, delimiter=',', skiprows=1)
sepalLength = iris_data[:, 0].astype(float)
petalLength = iris_data[:, 2].astype(float)
volume = (np.pi * petalLength * sepalLength ** 2) / 3
volume = volume[:, np.newaxis]
iris_data = np.concatenate([iris_data, volume], axis=1)
print(iris_data[0:10])
# [['5.1' '3.5' '1.4' '0.2' 'Iris‐setosa' 38.13265162927291]
# ['4.9' '3.0' '1.4' '0.2' 'Iris‐setosa' 35.200498485922445]
# ['4.7' '3.2' '1.3' '0.2' 'Iris‐setosa' 30.0723720777127]
# ['4.6' '3.1' '1.5' '0.2' 'Iris‐setosa' 33.238050274980004]
# ['5.0' '3.6' '1.4' '0.2' 'Iris‐setosa' 36.65191429188092]
# ['5.4' '3.9' '1.7' '0.4' 'Iris‐setosa' 51.911677007917746]
# ['4.6' '3.4' '1.4' '0.3' 'Iris‐setosa' 31.022180256648003]
# ['5.0' '3.4' '1.5' '0.2' 'Iris‐setosa' 39.269908169872416]
# ['4.4' '2.9' '1.4' '0.2' 'Iris‐setosa' 28.38324242763259]
# ['4.9' '3.1' '1.5' '0.1' 'Iris‐setosa' 37.714819806345474]]
12345678910111213141516171819
```

### **15. 随机抽鸢尾属植物的种类，使得Iris-setosa的数量是Iris-versicolor和Iris-virginica数量的两倍。**

```python
import numpy as np
species = np.array(['Iris‐setosa', 'Iris‐versicolor', 'Iris‐virginica'])
species_out = np.random.choice(species, 10000, p=[0.5, 0.25, 0.25])
print(np.unique(species_out, return_counts=True))
# (array(['Iris‐setosa', 'Iris‐versicolor', 'Iris‐virginica'], dtype='<U15'),
array([4927, 2477, 2596], dtype=int64))
123456
```

### **16. 根据 sepallength 列对数据集进行排序。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=object, delimiter=',', skiprows=1)
sepalLength = iris_data[:, 0]
index = np.argsort(sepalLength)
print(iris_data[index][0:10])
# [['4.3' '3.0' '1.1' '0.1' 'Iris‐setosa']
# ['4.4' '3.2' '1.3' '0.2' 'Iris‐setosa']
# ['4.4' '3.0' '1.3' '0.2' 'Iris‐setosa']
# ['4.4' '2.9' '1.4' '0.2' 'Iris‐setosa']
# ['4.5' '2.3' '1.3' '0.3' 'Iris‐setosa']
# ['4.6' '3.6' '1.0' '0.2' 'Iris‐setosa']
# ['4.6' '3.1' '1.5' '0.2' 'Iris‐setosa']
# ['4.6' '3.4' '1.4' '0.3' 'Iris‐setosa']
# ['4.6' '3.2' '1.4' '0.2' 'Iris‐setosa']
# ['4.7' '3.2' '1.3' '0.2' 'Iris‐setosa']]
12345678910111213141516
```

### **17. 在鸢尾属植物数据集中找到最常见的花瓣长度值（第3列）。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=object, delimiter=',', skiprows=1)
petalLength = iris_data[:, 2]
vals, counts = np.unique(petalLength, return_counts=True)
print(vals[np.argmax(counts)]) # 1.5
print(np.amax(counts)) # 14
1234567
```

### **18. 在鸢尾花数据集的 petalwidth（第4列）中查找第一次出现的值大于1.0的位置。**

```python
import numpy as np
outfile = r'.\iris.data'
iris_data = np.loadtxt(outfile, dtype=float, delimiter=',', skiprows=1, usecols=[0, 1, 2,
3])
petalWidth = iris_data[:, 3]
index = np.where(petalWidth > 1.0)
print(index)
print(index[0][0]) # 50
```