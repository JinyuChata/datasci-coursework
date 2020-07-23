import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

f_mgr = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

new_cases_data = pd.read_json("./new_cases_data.json")

df = pd.DataFrame({
    "case_id": [],
    "平均得分补": [],
    "平均每人提交次数": [],
    "面向用例提交人数比": [],
    "未满分人数比": [],
    "题目类别": []
})

for case_id in new_cases_data:
    case_data = new_cases_data[case_id]
    series = pd.Series({
        "case_id": case_id,
        "平均得分补": (100 - case_data["平均得分"]) / 100,
        "平均每人提交次数": case_data["总提交次数"] / case_data["提交人数"],
        "面向用例提交人数比": case_data["面向用例人数"] / case_data["提交人数"],
        "未满分人数比": 1 - (case_data["满分人数"] / case_data["提交人数"]),
        "题目类别": case_data["题目类别"]
    }, name=case_id)
    df = df.append(series)

# 数据标准化
feats = [
    "平均得分补",
    "平均每人提交次数",
    "面向用例提交人数比",
    "未满分人数比"
]

x = df.loc[:, feats].values
y = df.loc[:, ['case_id']].values
x = StandardScaler().fit_transform(x)

# # 3维度
# pca = PCA(n_components=3)
# principalComponents = pca.fit_transform(x)
# print(pca.explained_variance_ratio_)

# # 原始数据可视化
# importance = pca.explained_variance_ratio_
# plt.plot(importance)
# plt.title('Scree Plot')
# plt.xlabel('Factors')
# plt.ylabel('Eigenvalue')
# plt.grid()
# plt.show()

print("*"*100)
# 降维到2维
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
print("*"*100)
print(principalComponents)

# 查看转换系数
print(pca.components_)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
principalDf["type"] = df["题目类别"].values
finalDf = principalDf

# 数据降维可视化
fig = plt.figure(figsize=(20, 8), dpi=80)
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Components PCA', fontsize = 20)

case_types = [
    "数组",
    # "字符串",
    # "查找算法", "线性表", "排序算法", "树结构",
    "图结构",
    # "数字操作"
]
color_of_types = ["blue", "orange",
                  # "cyan", "blue", "gold", "grey", "red", "green"
                  ]

for case_type, color in zip(case_types, color_of_types):
    in_finalDf = finalDf['type']
    indicesToKeep = in_finalDf == case_type
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s=50)

ax.grid(alpha=0.2,color='black',linestyle="--")
plt.show()

