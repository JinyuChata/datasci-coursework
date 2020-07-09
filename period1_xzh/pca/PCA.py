#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);
#处理原始数据
datascisample = pd.read_json("./test_data.json")

df  = pd.DataFrame(
    {
        "user_id":[],
        "数组":[],
        "字符串":[],
        "查找算法":[],
        "线性表":[],
        "排序算法":[],
        "树结构":[],
        "图结构":[],
        "数字操作":[]
    }
)
# print(df["user_id"])

for user_id in datascisample:
    #加入userid
    # df["user_id"]=df["user_id"]+user_id
    #计算平均成绩
    dataFrame = datascisample[user_id]
    cases = dataFrame["cases"]
    #用来记录每个用户在每个类别里面的均分
    user_scores = dict(
        {
            "数组":[],
            "字符串":[],
            "查找算法":[],
            "线性表":[],
            "排序算法":[],
            "树结构":[],
            "图结构":[],
            "数字操作":[]
        }
    )
    # print(cases)
    for j in range(len(cases)):
        # 取得某一个case
        case = cases[j]
        type = case["case_type"]
        #计算所有提交的分数(这里需要每道题的难度来赋分应该,暂且用最终得分来计算)
        #用每道题的最终得分来计算每个人在某类题目里面的平均分
        final_score = case["final_score"]#某个人做某道题的最终

        # print((user_scores[type]))
        user_scores[type]=user_scores[type]+[final_score]

    print(user_scores)
    #检查用户均分是否有空,有的就补零
    for type in user_scores:
        if(len(user_scores[type])<=0):
            user_scores[type]=user_scores[type]+[0]
    # user_scores.fillna(0)
    print("-"*100)
    print(user_scores)
    #计算用户的均分,然后填入df中
    avg_scores=[]
    for type in user_scores:
        avg_scores=avg_scores+[
            np.mean(user_scores[type])
        ]
    avg_scores=[user_id]+avg_scores
    print(avg_scores)
    series = pd.Series(
        {
            "user_id":avg_scores[0],
            "数组": avg_scores[1],
            "字符串": avg_scores[2],
            "查找算法": avg_scores[3],
            "线性表": avg_scores[4],
            "排序算法": avg_scores[5],
            "树结构": avg_scores[6],
            "图结构": avg_scores[7],
            "数字操作": avg_scores[8]
        },
        name=user_id
    )
    df=df.append(series)

print(df)





# 数据标准化
# PCA is effected by scale so you need to scale the
# features in your data before applying PCA.
# (PCA会被数据的大小所影响, 所以在做之前, 我们需要先对数据进行标准化).
# 我们使用StandardScaler进行标准化, 标准化之后变为均值为0, 方差为1的数据.

features = [
        "数组",
        "字符串",
        "查找算法",
        "线性表",
        "排序算法",
        "树结构",
        "图结构",
        "数字操作"]
# Separating out the features
x = df.loc[:,features].values
# Separating out the target
y = df.loc[:,['user_id']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)
print("*"*100)
# 查看标准化之后的数据
print(pd.DataFrame(data = x, columns = features).head())

#先查看原来8维的
pca = PCA(n_components=8)
principalComponents = pca.fit_transform(x)
print(pca.explained_variance_ratio_)




# 原始数据进行可视化
importance = pca.explained_variance_ratio_
# plt.scatter(importance)
plt.plot(importance)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()





# 使用PCA进行降维,降到两维
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
# 查看降维后的数据
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
principalDf["user_id"]=df[['user_id']].values.astype(int)
finalDf = principalDf
# print(df[['user_id']].values)
# finalDf = pd.concat([principalDf, df[['user_id']].values.tolist()], axis = 1)
print(principalDf.head(5))

#查看转换系数
print("*"*100)
print(pca.components_)




# 对系数进行可视化
import seaborn as sns

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
# # plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# # sns.set(font='SimHei')  # 解决Seaborn中文显示问题
sns.set(font=my_font.get_name())
df_cm = pd.DataFrame(np.abs(pca.components_), columns=df.columns[1:])
plt.figure(figsize = (12,6))
ax = sns.heatmap(df_cm, annot=True, cmap="BuPu")
# 设置y轴的字体的大小
ax.yaxis.set_tick_params(labelsize=15)
ax.xaxis.set_tick_params(labelsize=15)
plt.title('PCA', fontsize='xx-large')
# Set y-axis label
plt.savefig('factorAnalysis.png', dpi=200)

plt.show()







#数据降维可视化
fig = plt.figure(figsize = (20,8),dpi=80)
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Components PCA', fontsize = 20)
users = [i for j in df[['user_id']].values.astype(int) for i in j ]
colors = list('b'*len(users))

print(finalDf.head(5))
for user, color in zip(users,colors):
    in_finalDf = finalDf['user_id'].astype(int)
    indicesToKeep = in_finalDf== user
    # 选择某个label下的数据进行绘制
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
# ax.legend(users)
ax.grid(alpha=0.2,color='black',linestyle="--")
plt.show()