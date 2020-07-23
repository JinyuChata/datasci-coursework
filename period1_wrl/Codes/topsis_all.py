
# -*- coding: utf-8 -*-

from collections import defaultdict
# import urllib.request,urllib.parse
# import os
# import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import csv

types = ["查找算法","排序算法","树结构","数字操作","数组","图结构","线性表","字符串"]

def entropyWeight(data):
	data = np.array(data)
	# 归一化
	P = data / data.sum(axis=0)

	# 计算熵值
	E = np.nansum(-P * np.log(P) / np.log(len(data)), axis=0)

	# 计算权系数
	return (1 - E) / (1 - E).sum()

temp = pd.DataFrame()
for filename in types:
    inp = pd.read_csv(f"data\\{filename}.csv",encoding="utf-8")
    temp = temp.append(inp)

# print(temp.describe())

#将id设为索引列
temp = temp.set_index("id")
#计算权重
# weight = np.linspace(0.4,0.1,4)
weight = entropyWeight(temp)
# weight = [0.50,0.15,0.15,0.20]
# print(weight)
# weight_md = "|".join(weight.astype(str))
# print("|"+weight_md+"|")

#指标正向化
temp["均分"] = temp["均分"].max()-temp["均分"]

#归一化
temp = temp / np.sqrt((temp ** 2).sum())
# print(temp)


# 最优最劣方案
Z = pd.DataFrame([temp.min(), temp.max()], index=['负理想解', '正理想解'])
# print(Z)

# 距离
Result = temp.copy()
Result['正理想解'] = np.sqrt(((temp - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
Result['负理想解'] = np.sqrt(((temp - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

# 综合得分指数
Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
Result['排序'] = Result.rank(ascending=False)['综合得分指数']

#排序
Result = Result.sort_values(by="排序",ascending = True)

# print(Result.index)

# #将数据保存到csv
Result.to_csv(f"data\\all-topsis.csv",encoding='utf-8-sig',index =True)


#绘制雷达图
data = Result.iloc[[0,49,99,149,199],:]
# print(Datas)

# for index, row in Datas.iterrows():
#     print("|"+str(index)+"|"+"|".join(row.astype(str))+"|")

# Datas.append()
data = data.iloc[:,:4]
# print(Datas)

labels = ["均分","提交次数","测试用例个数","答案代码行数"]
kinds = data.index
data = pd.concat([data,data[['均分']]],axis = 1)
centers = np.array(data)
# print(Datas)

n = len(labels)
angle = np.linspace(0,2*np.pi,n,endpoint=False)
angle = np.concatenate((angle,[angle[0]]))

fig = plt.figure(figsize=(20,10),dpi=80)
ax = fig.add_subplot(111, polar=True)    # 参数polar, 以极坐标的形式绘制图形

# 画线
for i in range(len(kinds)):
    ax.plot(angle, centers[i], linewidth=2, label=kinds[i])
    ax.fill(angle, centers[i],alpha = 0.4)  # 填充底色

# 添加属性标签
ax.set_thetagrids(angle * 180 / np.pi, labels,fontproperties = 'SimHei')
plt.title(f'案例分析',fontproperties = 'SimHei')
# plt.legend(loc='lower right')
plt.legend(loc='lower left')
# plt.show()
plt.savefig(f"result\\案例分析.png")