# coding=utf-8

import pandas as pd
import json
from xpinyin import Pinyin
p = Pinyin()

# 要做的是 人有多牛
# TODO: 1. 按照五个班级的数据进行整理 5个班级*8个类型
#       2. 每个班级要有: user_id, mean_score_of_committed, mean_score_of_submitted,
#                      commit_ratio, example_fronted_ratio, submit_times_commit_ratio

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

case_types = [
    "字符串", "树结构", "图结构", "线性表", "数组", "查找算法", "排序算法", "数字操作"
]

# 初始化DF
for i in group_converter:
    for j in case_types:
        result_template[group_converter[i]][j] = \
            pd.DataFrame(columns=['user_id', 'mean_score_of_committed', 'mean_score_of_submitted', 'commit_ratio', 'example_fronted_ratio', 'submit_times_commit_ratio'])

with open("../../data/group-results.json", 'r', encoding='UTF-8') as f:
    user_group_info = json.load(f)

with open("../../data/group-tests.json", 'r', encoding='UTF-8') as f:
    group_case_info = json.load(f)

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
            'example_fronted_ratio': 0
        }

    for case in cases_list:
        case_id = case["case_id"]

        if case_id in ordered_cases:
            typo_tmp_data = tmp_data[case['case_type']]

            typo_tmp_data['tot_commit_score'] += case['final_score']
            typo_tmp_data['tot_commit_cnt'] += 1

            typo_tmp_data['finished_ordered_cases_count'] += 1

            for record in case['upload_records']:
                typo_tmp_data['tot_submit_score'] += record['score']
                typo_tmp_data['tot_submit_cnt'] += 1

                # columns = ['user_id', 'mean_score_of_committed', 'mean_score_of_submitted',
                #            'commit_ratio', 'example_fronted_ratio', 'submit_times_commit_ratio'])

    # 处理单人数据
    # print(user_id)
    for typo in tmp_data:
        curr_typo_tmp_data = tmp_data[typo]
        new = pd.DataFrame({'user_id': user_id,
                            'mean_score_of_committed':
                                curr_typo_tmp_data['tot_commit_score'] / curr_typo_tmp_data['tot_commit_cnt']
                                if curr_typo_tmp_data['tot_commit_cnt'] != 0 else 0
                               ,
                            'mean_score_of_submitted':
                                curr_typo_tmp_data['tot_submit_score'] / curr_typo_tmp_data['tot_submit_cnt']
                                if curr_typo_tmp_data['tot_submit_cnt'] != 0 else 0
                               ,
                            'commit_ratio':
                                curr_typo_tmp_data['finished_ordered_cases_count'] / len(ordered_cases),
                            'example_fronted_ratio': 0,  # TODO
                            'submit_times_commit_ratio':
                                curr_typo_tmp_data['tot_submit_cnt'] / curr_typo_tmp_data['tot_commit_cnt']
                                if curr_typo_tmp_data['tot_commit_cnt'] != 0 else 2

                            }, index=[1])  # 自定义索引为：1 ，这里也可以不设置index
        to_append = result_template[group_name][typo]
        result_template[group_name][typo] = to_append.append(new, ignore_index=True)

for group in group_converter:
    for typo in case_types:
        result_template[group_converter[group]][typo].to_csv(
            './data/'+group_converter[group]+'_'+p.get_pinyin(typo.encode('utf-8').decode(), '') +'.csv', index=False)
