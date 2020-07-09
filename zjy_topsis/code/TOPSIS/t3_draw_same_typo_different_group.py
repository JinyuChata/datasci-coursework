# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import json
from xpinyin import Pinyin
p = Pinyin()

# TODO: 绘制不同组在同一种类上的不同表现图
#       共计8类 8张图 每张图中5条折线

f_mgr = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


group_converter = {
    1: "g1", 2: "g2", 3: "g3", 4: "g4", 5: "g5"
}

case_types = [
    "字符串", "树结构", "图结构", "线性表", "数组", "查找算法", "排序算法", "数字操作"
]

pinyin_name = p.get_pinyin("typo".encode('utf-8').decode())

data_to_draw = {"字符串": {}, "树结构": {}, "图结构": {}, "线性表": {}, "数组": {},
                "查找算法": {}, "排序算法": {}, "数字操作": {}}
# 对8个类型进行遍历
for typo in case_types:
    pinyin_typo_name = p.get_pinyin(typo.encode('utf-8').decode(), '')

    # 对5个组别进行遍历
    for group_id in group_converter:
        group_name = group_converter[group_id]
        csv_file_name = 'ahp_'+group_name+'_'+pinyin_typo_name+'.csv'
        full_path = './matlab_dir/ahp_data/'+csv_file_name
        # 创建DataFrame
        csv_df = pd.read_csv(full_path, low_memory=False)
        csv_df.sort_values(by='AHP_score', ascending=False, inplace=True)
        data_to_draw[typo][group_name] = csv_df

with open("../../分组/group-counts.json", 'r', encoding='UTF-8') as f:
    user_group_count = json.load(f)

for typo in case_types:
    plt.figure(figsize=(20, 8), dpi=80)
    _plt_yticks = [i / 10 for i in range(21, 49)]
    _plt_xticks = range(0, 69)

    plt.title(typo, fontproperties=f_mgr)

    plt.xticks(_plt_xticks[::5])
    plt.yticks(_plt_yticks[::5])

    curr_typo_data = data_to_draw[typo]
    for group_id in group_converter:
        curr_grp_data = curr_typo_data[group_converter[group_id]]
        y = curr_grp_data.loc[:, 'AHP_score']
        x = range(len(y))
        # 开始绘图
        plt.plot(x, y, label=group_converter[group_id])
        plt.legend()
        # break

    plt.savefig('topsis_typo_group_analysis/'+p.get_pinyin(typo.encode('utf-8').decode())+'.jpg')
