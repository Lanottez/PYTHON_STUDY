# 结合金融场景演示Numpy模块的操作

* 开源的数据计算扩展模块，可以用来储存和处理大型矩阵
* 强大的N维数组对象
* 复杂的广播功能
* 用于集成C/C++和Fortran代码的工具
* 实用的线性代数、傅立叶变换和随机数功能
* 通用数据的高效多维容器

<br />

## Leason 3.2: N维数组
* np.array(一个数列): 创建一维数组
* np.array([数列1，数列2，数列3，....，数列m])： 创建多维数组
* np.arange(起始值，终止值，步长)
* np.linspace(起始值，终止值，元素个数)
* np.zeros_like(数列): 相同尺寸的数列
* np.ones_like(数列): 相同尺寸的数列
* np.eye(数字): 创建单位矩阵
* ndim: 查看数组的维度
* size: 查看数组的元素数量
* dtype: 查看数组的元素类型

<br />

## Leason 3.3: 数组的索引、切片和排序

<br />

## Leason 3.4: 数组的相关运算

<br />

## Leason 3.5: 通过Numpy生成随机数

二项分布(Binomial distribution)
* X: 随机试验的结果
* p: 事件发生的概率
* n次独立重复实验中发生k次事件的概率: <img src="http://chart.googleapis.com/chart?cht=tx&chl=P(X = k) = C_{n}^{k}p^{k}(1-p)^{n-k}" style="border:none;">, where <img src="http://chart.googleapis.com/chart?cht=tx&chl=C_{k}^{n} = \frac{n!}{(n-k)!}" style="border:none;">
* 期望值: <img src="http://chart.googleapis.com/chart?cht=tx&chl=D(X) = np(1-p)" style="border:none;">
* 方差: <img src="http://chart.googleapis.com/chart?cht=tx&chl=D(X) = np(1-p)" style="border:none;">
