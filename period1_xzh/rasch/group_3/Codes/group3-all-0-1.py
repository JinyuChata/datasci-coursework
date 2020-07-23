#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D
from pandas import DataFrame
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# 2804，2456，2309这三道题目有太多nan

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);
#处理原始数据
with open('../../group-results.json', 'r') as f:
    group_data = json.load(f)
with open('../../group-tests.json', 'r') as f:
    group_exercises = json.load(f)

#处理原始数据
datascisample = pd.read_json("../../../pca/test_data.json")
# print(data)


group_people={
    "g1":[],
    "g2":[],
    "g3":[],
    "g4":[],
    "g5":[]
}

#转换进去
for key in group_data:
    group_people[group_data[key]].append(key)

# print(groups)



#第一组同学每道题每个人的得分情况
# 形式是二维数组
# 每一行代表一个同学,每一列代表题目的分数
#先做形式 user:{"每道题目的分数"}
result_group3= {}
set_of_scores3=set()#分数的种类,为了好用jmetrik
 #初始化
for user_id in group_people["g3"]:
    user_scores = {}
    for case in group_exercises["g3"]:
        user_scores[case] = 0
    result_group3[user_id]=user_scores
    # print(user_scores)
print(result_group3)
#计算每道题每个人的平均分
for user_id in group_people["g3"]:
    #加入userid
    # df["user_id"]=df["user_id"]+user_id
    #计算平均成绩
    dataFrame = datascisample[int(user_id)]
    cases = dataFrame["cases"]
    for j in range(len(cases)):
        case = cases[j]
        type = case["case_type"]
        case_id=case["case_id"]
        uploads=case["upload_records"]
        final_score = case["final_score"]
        sum_of_scores=0
        if len(uploads)>0:
            # avg_of_scores = sum_of_scores/(len(uploads))
            result_group3["" + str(user_id)][case_id] = 1 if (final_score==100) else 0 #通过

df_group3=DataFrame(result_group3)
df_group3=df_group3.T

#有很多nan 原因是有一个人做了很多别的组的题 47339,因此上面的json数据里面去掉47339
# df_group3=df_group3.drop(['47339'])

print(df_group3)

df_group3.to_csv("./group3_results0_1.csv",index=False,header=True)
print("set_of_scores3 :"+str(set_of_scores3))


