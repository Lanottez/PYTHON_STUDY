# 3.1.1 元组
4,5,6,[1,2] #元组
(4,5,6),(7,8) #nested tuple
tuple([4,0,2]) #将列表转化为元组
tuple('string') #将字符串转化为元组
tup[0] #索引元组
tup[-1].append(3) #修改元组内可变的对象
(4,None,'foo') + (6,0) + ('bar',) #利用加号链接元组
('foo',) * 4 #利用乘号拷贝元组
a, b, c, d = tup #元组拆包
x,y = y,x #变换变量名

#使用拆包遍历元组/列表组成的元组
seq = [(1,2,3),[4,5,6],[7,8,9]]
for a,b,c in seq:
    print('a = {0}, b= {1}, c = {2}'.format(a,b,c))
    
#在函数调用时获取任意长度的位置参数列表
values = 1,2,3,4,5
a,b,*rest = values

tup.count(4) #计量某个数值在元组中出现的次数

# 3.1.2 列表
a_list=[2,3,6,'asd'] #列表
list(('foo','bar',)) #将元组转化为列表
a_list[1] = 'pee' #索引，修改
list(range(0,10)) #将迭代器转化为列表
a_list.append('dwarf') #在尾部添加元素
a_list.insert(1,'red') #在指定位置添加元素
a_list.pop(2) #移除指定位置的元素
a_list.remove('foo') #移除该元素
'foo' in b_list #检查该元素是否在该list中；相对字典、集合，检查列表中是否包含一个值耗时较长
list_a + list_b #用+号连接两个列表；需要额外代价，不推荐
list_a.extend([7,8,(2,3)]) #向已存在的列表添加元素；不需要额外代价，推荐
list_a.sort() #内部排序
list_a.sort(key=len) #通过字符串的长度进行排序

#内建的bisect模块实现了二分搜索和已排序列表
import bisect
bisect.bisect(a_list,4) #找到元素应当被插入的位置
bisect.insort(a_list,4) #将元素插入到相应位置

a_list[1:5] #切片；包含start位置的元素，不包含stop位置的元素
a_list[::2] #隔两个数取一个值
a_list[::-1] #翻转列表
# 3.1.3 内建序列函数

# 3.1.4 字典

# 3.1.5 集合

# 3.1.6 列表、集合和字典的推导式