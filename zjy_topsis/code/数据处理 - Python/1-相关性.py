import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import seaborn as sns

import numpy as np

f_mgr = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

## 读入数据
if __name__ == '__main__':
    data_raw = pd.read_json("test_data.json")

    user_mean_score_by_type = {}
    user_all_score_by_type = {}
    # print(case_info)
    # 获取题目类别 print(case_info.loc["题目类别"][2067])

    for i in data_raw:
        cases_list = data_raw[i]["cases"]
        user_id = i
        if user_mean_score_by_type.get(user_id) is None:
            user_mean_score_by_type[user_id] = {
                "数组": None, "字符串": None, "查找算法": None, "线性表": None,
                "排序算法": None, "树结构": None, "图结构": None, "数字操作": None
            }
        if user_all_score_by_type.get(user_id) is None:
            user_all_score_by_type[user_id] = {
                "数组": [], "字符串": [], "查找算法": [], "线性表": [],
                "排序算法": [], "树结构": [], "图结构": [], "数字操作": []
            }
        for case in cases_list:
            case_id = case["case_id"]
            upload_records = case["upload_records"]
            df_records = pd.DataFrame(upload_records)
            # 题目类别
            typo = case["case_type"]
            # 本题平均分
            if df_records.empty:
                mean_score = case["final_score"]
            else:
                mean_score = df_records.mean()["score"]

            user_all_score_by_type[user_id][typo].append(mean_score)

    for user_id in user_all_score_by_type:
        user_all_score_info = user_all_score_by_type[user_id]
        for typo in user_all_score_info:
            mean_val = float(np.mean(user_all_score_info[typo]))
            user_mean_score_by_type[user_id][typo] = mean_val

    df = pd.DataFrame(user_mean_score_by_type).transpose()

    for column in list(df.columns[df.isnull().sum() > 0]):
        mean_val = df[column].mean()
        df[column].fillna(mean_val, inplace=True)

    # 对各个分类的平均得分情况制作直方图
    # for column in list(df.columns):
    #     x = df[column]
    #     plt.hist(x=x, bins=20)
    #     plt.xticks(range(100)[::5], range(100)[::5])
    #     plt.xlabel("score", fontproperties=f_mgr)
    #     plt.show()
    #     break

    sns.set(font=f_mgr.get_name())
    sns.heatmap(df.corr())
    plt.show()
    plt.savefig("相关性.jpg")

    print(df.head())