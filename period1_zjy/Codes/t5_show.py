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

csv = pd.read_csv('./matlab_dir/ahp_data/ahp_g1_chazhaosuanfa.csv', low_memory=False)
csv.drop(csv.index, inplace=True)

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
        csv = csv.append(csv_df[csv_df['user_id']==58547])

csv.to_csv("./out.csv")