
# -*- coding: utf-8 -*-

from collections import defaultdict
# import urllib.request,urllib.parse
# import os
# import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

temp = pd.read_csv(f"data\\TOPSIS\\all-topsis.csv",encoding="utf-8")
# print(Result)
temp = temp.set_index("id")
data = temp.loc[:,"综合得分指数"]
# print(Datas)

plt.figure(figsize=(30,15),dpi=80)
plt.grid()
plt.xlabel('综合得分',fontproperties = 'SimHei')
plt.ylabel('数量',fontproperties = 'SimHei')
plt.hist(data)
# plt.show()
plt.title(f'综合得分分布',fontproperties = 'SimHei')
plt.savefig(f"pic\\综合得分分布.png")
