#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import pandas as pd
from matplotlib import font_manager
from pandas import DataFrame


#有很多nan 原因是有一个人做了很多别的组的题 47329,因此上面的json数据里面去掉47329
# df_group1=df_group1.drop(['47329'])
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

#第一组同学每道题每个人的得分情况
# 形式是二维数组
# 每一行代表一个同学,每一列代表题目的分数
#先做形式 user:{"每道题目的分数"}
result_group5 = {}
 #初始化
for user_id in group_people["g5"]:
    user_scores = {}
    for case in group_exercises["g5"]:
        if case=="2726" or case=="2705" or int(case) in [2526,2397]:
            continue
        if(classify_items[case]["题目类别"]=="树结构"):
            user_scores[case] = 0
    result_group5[user_id]=user_scores
print(result_group5)

#计算每道题每个人的平均分
for user_id in group_people["g5"]:
    #加入userid
    # df["user_id"]=df["user_id"]+user_id
    #计算平均成绩
    dataFrame = datascisample[int(user_id)]
    cases = dataFrame["cases"]
    for j in range(len(cases)):
        case = cases[j]
        type = case["case_type"]
        case_id=case["case_id"]
        if(case_id=="2726" or case_id=="2705" or case_id=="2526" or case_id=="2397"):
            continue
        uploads=case["upload_records"]
        final_score = case["final_score"]
        sum_of_scores=0
        # for k in range(len(uploads)):
            # upload=uploads[k]
            # sum_of_scores=sum_of_scores+upload["score"]
        if len(uploads)>0 and type=="树结构":
            # avg_of_scores = sum_of_scores/(len(uploads))
            result_group5["" + str(user_id)][case_id] = 1 if (final_score==100) else 0 #通过

df_group5=DataFrame(result_group5)
df_group5=df_group5.T
df_group5=df_group5.fillna(0)


print(df_group5)

df_group5.to_csv("./group5_results_tree_0_1.csv",index=False,header=True)