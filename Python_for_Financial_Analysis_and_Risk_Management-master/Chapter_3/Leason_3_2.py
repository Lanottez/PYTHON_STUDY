#coding:utf-8
import numpy as np
'直接输入数组'
array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])


'将列表转为数组'
list_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_array = np.array(list_2)
array_2 = list_array.reshape(4,5)

'将多维数组转为一维数组'
array_3 = array_2.ravel()

'生成整数数列'
array_4 = np.arange(10)
array_5 = np.arange(1,10,3)

'生成等差序列'
array_6 = np.linspace(0,100,51) #0～100，元素个数51，以数组形成存放


'创建元素0的数组'
array_7 = np.zeros(5) 
array_8 = np.zeros([3,4])
array_9 = np.zeros_like(array_2)
print(array_8)