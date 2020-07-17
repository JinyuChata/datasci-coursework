# coding=utf-8

import pandas as pd
import json
from xpinyin import Pinyin

p = Pinyin()

# 要做的是 人有多牛
# TODO: 1. 按照五个班级的数据进行整理 5个班级*8个类型
#       2. 每个班级要有: user_id, mean_score_of_committed, mean_score_of_submitted,
#                      submit_times_per_commit, commit_ratio, commit_diff_ratio

test_data = pd.read_json("../../data/test_data.json")

group_converter = {
    1: "g1", 2: "g2", 3: "g3", 4: "g4", 5: "g5"
}

# result_template = {}
result_template = {
    "g1": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g2": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g3": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g4": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g5": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
}

case_tot_diff_table = {
    "g1": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g2": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g3": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g4": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
    "g5": {
        "字符串": None,
        "树结构": None,
        "图结构": None,
        "线性表": None,
        "数组": None,
        "查找算法": None,
        "排序算法": None,
        "数字操作": None,
    },
}

case_types = [
    "字符串", "树结构", "图结构", "线性表", "数组", "查找算法", "排序算法", "数字操作"
]

# 初始化DF
for i in group_converter:
    for j in case_types:
        result_template[group_converter[i]][j] = \
            pd.DataFrame(columns=['user_id', 'mean_score_of_committed', 'mean_score_of_submitted',
                                  'submit_times_per_commit', 'commit_ratio', 'commit_diff_ratio'])

# 初始化题目难度
csv1 = pd.read_csv('../../data/all-topsis.csv', sep=',', usecols=[0, 7])

with open("../../data/group-results.json", 'r', encoding='UTF-8') as f:
    user_group_info = json.load(f)

with open("../../data/group-tests.json", 'r', encoding='UTF-8') as f:
    group_case_info = json.load(f)

with open("../../data/cases_analysis_source.json", 'r', encoding='UTF-8') as f:
    case_info = json.load(f)

case_cnt = {'g1': {'字符串': 17, '树结构': 28, '图结构': 12, '线性表': 32, '数组': 44, '查找算法': 21, '排序算法': 11, '数字操作': 35},
            'g2': {'字符串': 17, '树结构': 25, '图结构': 21, '线性表': 32, '数组': 40, '查找算法': 18, '排序算法': 12, '数字操作': 35},
            'g3': {'字符串': 18, '树结构': 31, '图结构': 13, '线性表': 30, '数组': 45, '查找算法': 16, '排序算法': 12, '数字操作': 35},
            'g4': {'字符串': 18, '树结构': 28, '图结构': 14, '线性表': 29, '数组': 50, '查找算法': 20, '排序算法': 8, '数字操作': 33},
            'g5': {'字符串': 18, '树结构': 29, '图结构': 14, '线性表': 28, '数组': 39, '查找算法': 24, '排序算法': 17, '数字操作': 37}}



for group_id in group_converter:
    group_name = group_converter[group_id]
    for typo in case_types:
        tot_score_with_diff = 0
        for cid in group_case_info[group_name]:
            if case_info[cid]["题目类别"] == typo:
                tot_score_with_diff += 100 * csv1[csv1['id'] == int(cid)].iloc[0, 1]
        case_tot_diff_table[group_name][typo] = tot_score_with_diff

for user_id in test_data:
    user_id = str(user_id)
    group_name = user_group_info[user_id]
    group_df = result_template[group_name]
    cases_list = test_data[int(user_id)]["cases"]

    ordered_cases = group_case_info[group_name]

    # tmp data
    tmp_data = {}
    # 建立tmp_data
    for typo in case_types:
        tmp_data[typo] = {
            'tot_commit_score': 0, 'tot_commit_cnt': 0,
            'tot_submit_score': 0, 'tot_submit_cnt': 0,
            'finished_ordered_cases_count': 0,
            'example_fronted_ratio': 0,
            'tot_commit_score_with_diff': 0
        }

    for case in cases_list:
        case_id = case["case_id"]

        if case_id in ordered_cases:
            typo_tmp_data = tmp_data[case['case_type']]

            typo_tmp_data['tot_commit_score'] += case['final_score']
            typo_tmp_data['tot_commit_cnt'] += 1

            diff = csv1[csv1['id'] == int(case_id)].iloc[0, 1]
            typo_tmp_data['tot_commit_score_with_diff'] += diff * case['final_score']

            typo_tmp_data['finished_ordered_cases_count'] += 1

            for record in case['upload_records']:
                typo_tmp_data['tot_submit_score'] += record['score']
                typo_tmp_data['tot_submit_cnt'] += 1

                #       2. 每个班级要有: user_id, mean_score_of_committed, mean_score_of_submitted,
                #                      submit_times_per_commit, commit_ratio, commit_diff_ratio

    # 处理单人数据
    # print(user_id)
    for typo in tmp_data:
        curr_typo_tmp_data = tmp_data[typo]
        # 获取对应组别的题目数目
        new = pd.DataFrame({'user_id': user_id,
                            'mean_score_of_committed':
                                curr_typo_tmp_data['tot_commit_score'] / curr_typo_tmp_data['tot_commit_cnt']
                                if curr_typo_tmp_data['tot_commit_cnt'] != 0 else 0
                               ,
                            'mean_score_of_submitted':
                                curr_typo_tmp_data['tot_submit_score'] / curr_typo_tmp_data['tot_submit_cnt']
                                if curr_typo_tmp_data['tot_submit_cnt'] != 0 else 0
                               ,
                            'submit_times_per_commit':
                                curr_typo_tmp_data['tot_submit_cnt'] / curr_typo_tmp_data['tot_commit_cnt']
                                if curr_typo_tmp_data['tot_commit_cnt'] != 0 else 2,
                            'commit_ratio':
                                curr_typo_tmp_data['finished_ordered_cases_count'] / case_cnt[group_name][typo],

                            'commit_diff_ratio': curr_typo_tmp_data['tot_commit_score_with_diff'] /
                                                            case_tot_diff_table[group_name][typo]
                                if curr_typo_tmp_data['tot_commit_cnt'] != 0 else 0,
                            }, index=[1])  # 自定义索引为：1 ，这里也可以不设置index
        to_append = result_template[group_name][typo]
        result_template[group_name][typo] = to_append.append(new, ignore_index=True)

for group in group_converter:
    for typo in case_types:
        result_template[group_converter[group]][typo].to_csv(
            './data/' + group_converter[group] + '_' + p.get_pinyin(typo.encode('utf-8').decode(), '') + '.csv',
            index=False)
