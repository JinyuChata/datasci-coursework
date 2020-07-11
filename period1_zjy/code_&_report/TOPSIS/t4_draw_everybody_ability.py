# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np
import json
from xpinyin import Pinyin
p = Pinyin()

# TODO: 绘制每个人在不同类型题目中展现出的雷达图

f_mgr = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


group_converter = {
    1: "g1", 2: "g2", 3: "g3", 4: "g4", 5: "g5"
}

case_types = [
    "字符串", "树结构", "图结构", "线性表", "数组", "查找算法", "排序算法", "数字操作"
]

pinyin_name = p.get_pinyin("typo".encode('utf-8').decode())

data_to_draw = {"g1": {}, "g2": {}, "g3": {}, "g4": {}, "g5": {}}

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
        data_to_draw[group_name][typo] = csv_df

with open("../../分组/group-tests.json", 'r', encoding='UTF-8') as f:
    user_grp_info = json.load(f)

with open("../../分组/group-results.json", 'r', encoding='UTF-8') as f:
    user_info = json.load(f)

# 对所有学生进行遍历
for user_id in user_info:
    group_name = user_info[user_id]
    tmp_data = {}
    for typo in case_types:
        data = data_to_draw[group_name][typo]
        tmp_data[typo] = data[data['user_id'] == int(user_id)].iloc[0, 6]

    fig = plt.figure(figsize=(8, 8))
    ax1 = fig.add_subplot(111, polar=True)  # 设置第一个坐标轴为极坐标体系
    data_radar = np.array([i for i in tmp_data.values()]).astype(float)
    data_label = np.array([i for i in tmp_data.keys()])

    angle = np.linspace(0, 2 * np.pi, len(data_radar), endpoint=False)  # data里有几个数据，就把整圆360°分成几份
    angles = np.concatenate((angle, [angle[0]]))  # 增加第一个angle到所有angle里，以实现闭合
    data_radar = np.concatenate((data_radar, [data_radar[0]]))  # 增加第一个人的第一个data到第一个人所有的data里，以实现闭合

    ax1.set_thetagrids(angles * 180 / np.pi, data_label, fontproperties=f_mgr)  # 设置网格标签
    ax1.plot(angles, data_radar, "o-")
    ax1.set_theta_zero_location('NW')  # 设置极坐标0°位置
    ax1.set_rlim(1.8, 6.5)  # 设置显示的极径范围
    ax1.fill(angles, data_radar, facecolor='g', alpha=0.2)  # 填充颜色
    ax1.set_rlabel_position(255)  # 设置极径标签位置
    ax1.set_title(user_id, fontproperties=f_mgr, fontsize=16)  # 设置标题
    plt.savefig('./topsis_user_ability_radar/'+user_id+'_radar.jpg')





