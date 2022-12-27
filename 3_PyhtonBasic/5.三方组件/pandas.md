Python 数据分析工具 pandas 中以 DataFrame 和 Series 作为主要的数据结构。

Series 是一个数据序列。DataFrame 是一张数据表（可以理解由多个 Series 构成，每个 Series 为一列）。DataFrame 和 Excel 和数据库的数据表类似（实际结构更复杂，因为支持多重索引），因此可以对其做类似 Excel 数据表的排序、筛选、聚合、透视表等操作，也可以做类似于数据库数据表的多表关联（ join ）等操作。



### 创建DataFrame 对象

```python
import pandas as pd
df = pd.DataFrame()  # 创建DataFrame对象
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
```

#### 从文件读入

```python
df = pandas.read_json('abc.json')
df = pandas.read_csv('abc.csv', sep=';', nrows=2) # 首先输入csv文本地址,然后分割符选择等等
```

#### 保存到文件

```python
df.to_csv('abc.csv', encoding="utf8") # 要支持中文，python2必须指定encoding。python3已默认使用utf8
df.to_excel('foo.xlsx',sheet_name='Sheet1');pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])#写入读取excel数据，pd.read_excel读取的数据是以DataFrame形式存储
df.to_hdf('foo.h5','df');pd.read_hdf('foo.h5','df')#写入读取HDF5数据
```







### 查看 DataFrame 数据及属性

```python
df.dtypes #查看各行的数据格式
df['col1'].astype(int)#转换某列的数据类型
df.head() #查看前几行的数据,默认前5行
df.tail() #查看后几行的数据,默认后5行
df.index #查看索引
df.columns #查看列名
df.values #查看数据值
df.describe() #描述性统计
df.T #转置
```



### 选择数据

```python
df[1:-3] # 获取1到倒数第三行
df.ix[1:3] # 同上 
df.ix[1:3，[1,3]]#获取1列3列的1~3行数据
df['c1'] # 选择列
df.c1 # 效果同上
df.columns[[0,1,3]] # zero indexed
```

需要注意 DataFrame 取下标和索引速度非常慢，不建议对其做 for 循环操作，若要做循环操作，建议两种替换方案，一种使用内建函数（ apply、map、trasnform ）等，另外一种将每列 Series 转为 list 之后处理（ col_list = df.col.tolist()）。

### 4. 筛选数据（保留对应的行）

```
alist = ['023-18996609823']
df['code'].isin(alist) #将要过滤的数据放入字典中,使用isin对数据进行筛选,返回行索引以及每行筛选的结果,若匹配则返回ture
df[df['code'].isin(alist)] #获取匹配结果为ture的行
df[df.value>0]
df[df['plan'].str.contains(r'.*?语音CDMA.*')] #使用正则表达式进行模糊匹配,*匹配0或无限次,?匹配0或1次
```

### 5. 删除数据

```python
df[columns].drop_duplicates() #剔除重复行数据
df[df.isnull()]
df[df.notnull()]
df.dropna()#将所有含有nan项的row删除
df.dropna(axis=1,thresh=3) #将在列的方向上三个为NaN的项删除
df.dropna(how='ALL')#将全部项都是nan的row删除填充值
```

#### 5.1. 删除特定列

```
del df.col1  # 删除列 inplace
df = df.drop('column_name', 1) # 返回删除后的新的DataFrame
df.drop('column_name', axis=1, inplace=True)
df.drop([df.columns[[0, 1, 3]]], axis=1, inplace=True)   # Note: zero indexed
```

### 6. 修改数据

#### 6.1. 修改列名

```
df.rename(columns={'A':'a', 'C':'c'}, inplace=True)
df.columns = ['A', 'B', 'C']

df.c
df.fillna(0)
df.fillna({1:0,2:0.5}) #对第一列nan值赋0，第二列赋值0.5
df.fillna(method='ffill') #df
df.ix[1:3，[1,3]]=1#所选位置数据替换为1   
df['支局_维护线'] = df['支局_维护线'].str.replace('巫溪分公司(.{2,})支局','\1')#可以使用正则表达式
```

#### 6.2. 新增列

```
df['new_column'] = df['old_column']   # 新增了一列 
df.new_column = df['old_column']      # 这样不会新增列，只会跟原列起了个别名引用
```

### 7. apply

```
df.apply(lambda col: sum(col), axes=0) # 对每列求和
df.apply(lambda row: sum(row), axes=0) # 对每行求和
df.col2 = df.col1.apply(lambda col: sum(col))    # 对col1列求和
df.col3 = df.col3.apply(lambda x: x+1) # col3列都加1
df = df.applymap(lambda x:x+1) # 每个元素都加1
df.transform(lambda x:x+1)     # 效果同上，相当于inplace的applymap
```

### 8. 聚合数据(类似 SQL 中的 GROUP BY 或 HAVING):

```
df.groupby(['col1', 'col2']) # 将数据
 data_obj.groupby('支局_维护线')['用户标识'] #上面的简单写法
 adsl_obj.groupby('支局_维护线')['用户标识'].agg([('ADSL','count')])#按支局进行汇总对用户标识进行计数,并将计数列的列名命名为ADSL
```

### 9. 透视表

```
df = df.pivot(index='A', columes='B', values='C') # 先聚合再透视。
table = pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum) # 复杂一点的，支持同时聚合
```

### 10. 合并数据集（类似于数据库的 union/union all ）



```
df1 = df1.append(df2) # df2放在df1后面，注意append会返回一个新的对象，不是在原对象上修改。
df = pandas.concat([df1, df2], ignore_index=True) # 等价于append
```

### 11. Join 数据集（类似于数据库的 left/right/inner/outer join ）

```
df = pandas.concat([df1, df2], axis=1) # 和sql的join类似，on index_key
merge(df1, df2, on='abc',how='inner')# df1和df2将用户标识当成重叠列的键合并两个数据集,inner表示取两个数据集的交集.
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
```

### 12. 排序

```
df.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
```





numpy与pandas构建数据

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(3, 4), index=['aa', 'bb', 'cc'], columns=['a', 'b', 'c', 'd'])
```





行列操作

```python
# 添加尾列c，全为空白，添加尾列d，为[5,6]
data['c'] = ''
data['d'] = [5,6]

# 在第二列插入列名为c的空列，编号索引从0开始
data.insert(2,'c','')

# 删除列名为c的列
del data['c']


# 删除某行或者某列
df.drop("a", axis=0) # 删除行名为a的行
df.drop("a", axis=1) # 删除列名为a的列
```



```python
import numpy as np
import pandas as pd

ser = pd.Series(np.arange(3.))
print(ser)

data = pd.DataFrame(np.arange(16).reshape(4, 4), index=list('abcd'), columns=list('wxyz'))
print(data)

# 选择表格中的'w'列，使用类字典属性,返回的是Series类型
print(data['w'])
# 选择表格中的'w'列，使用点属性,返回的是Series类型
print(data.w)

# 选择表格中的'w'列，返回的是DataFrame类型
print(data[['w']])
# 选择表格中的'w'、'z'列
print(data[['w', 'z']])

# 返回第1行到第2行的所有行，前闭后开，包括前不包括后
print(data[0:2])
# 返回第2行，从0计，返回的是单行，通过有前后值的索引形式，
print(data[1:2])
# 如果采用data[1]则报错
# data.ix[1:2] 跟data[1:2]同，已废弃

# 利用index值进行切片，返回的是**前闭后闭**的DataFrame,
print(data['a':'b'])

# 选取DataFrame最后一行，返回的是Series
print(data.iloc[-1])
# 选取DataFrame最后一行，返回的是DataFrame
print(data.iloc[-1:])
# 返回‘a’行'w'、'x'列，这种用于选取行索引列索引已知
print(data.loc['a', ['w', 'x']])
# 选取第二行第二列，用于已知行、列位置的选取。
print(data.iat[1, 1])

```





pandas的dataframe数据类型转换

 

在使用pandas库进行数据分析时，有时候会需要将object类型转换成数值类型(float,int)，那么如何做呢？

主要有以下三种方法：创建时指定类型，df.astype强制类型转换，以及使用pd.to_numeric() 转换成适当数值类型。
