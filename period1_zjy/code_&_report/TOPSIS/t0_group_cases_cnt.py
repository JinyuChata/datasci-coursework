

import pandas as pd
import json
from xpinyin import Pinyin

with open("../../data/cases_analysis_source.json", 'r', encoding='UTF-8') as f:
    case_info = json.load(f)

with open("../../data/group-tests.json") as f:
    group_case = json.load(f)

group_converter = {
    1: "g1", 2: "g2", 3: "g3", 4: "g4", 5: "g5"
}

case_types = [
    "字符串", "树结构", "图结构", "线性表", "数组", "查找算法", "排序算法", "数字操作"
]

res = {"g1": {}, "g2": {}, "g3": {}, "g4": {}, "g5": {}, }

for grp_id in group_converter:
    grp_name = group_converter[grp_id]
    li_of_group = group_case[grp_name]
    for case_typo in case_types:
        cnt = 0
        for case_id in li_of_group:

            if case_info[case_id]["题目类别"] == case_typo:
                cnt += 1
        res[grp_name][case_typo] = cnt

print(res)
