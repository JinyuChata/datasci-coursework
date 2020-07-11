#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
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

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);
#处理原始数据
with open('../group-results.json', 'r') as f:
    group_data = json.load(f)
with open('../group-tests.json', 'r') as f:
    group_exercises = json.load(f)
with open('../cases_analysis_source.json', 'r', encoding='UTF-8') as f:
    classify_items = json.load(f)
#处理原始数据
datascisample = pd.read_json("../../pca/test_data.json")
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
result_group1 = {}
set_of_scores1=set()#分数的种类,为了好用jmetrik
 #初始化
for user_id in group_people["g1"]:
    user_scores = {}
    for case in group_exercises["g1"]:
        if(classify_items[case]["题目类别"]=="树结构"):
            user_scores[case] = 0
    result_group1[user_id]=user_scores
print(result_group1)

#计算每道题每个人的平均分
for user_id in group_people["g1"]:
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
        # for k in range(len(uploads)):
            # upload=uploads[k]
            # sum_of_scores=sum_of_scores+upload["score"]
        if len(uploads)>0 and type=="树结构":
            # avg_of_scores = sum_of_scores/(len(uploads))
            result_group1["" + str(user_id)][case_id] = 1 if (final_score==100) else 0 #通过

df_group1=DataFrame(result_group1)
df_group1=df_group1.T

#有很多nan 原因是有一个人做了很多别的组的题 47329,因此上面的json数据里面去掉47329
# df_group1=df_group1.drop(['47329'])

print(df_group1)

df_group1.to_csv("./group1_results_tree_0_1.csv",index=False,header=True)
print("set_of_scores1 :"+str(set_of_scores1))
