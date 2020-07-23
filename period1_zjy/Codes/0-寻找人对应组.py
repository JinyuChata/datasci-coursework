import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
from collections import Counter
import json

data = pd.read_json("./test_data.json")

with open("./分组/group-tests.json", 'r', encoding='UTF-8') as f:
    grp_info_origin = json.load(f)

grp_info_set = {}
for grp in grp_info_origin:
    grp_info_set[grp] = set(grp_info_origin[grp])

user_info_dict = {}
group_cnt = {
    "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0
}

for user_id in data:
    cases_list = data[user_id]["cases"]
    this_partition_set = set()
    for case in cases_list:
        this_partition_set.add(case['case_id'])

    max_size = -1
    probably_grp = -1
    for grp in grp_info_set:
        sort_size = len(this_partition_set.intersection(grp_info_set[grp]))
        if sort_size > max_size:
            probably_grp = grp
            max_size = sort_size

    user_info_dict[user_id] = probably_grp
    group_cnt[probably_grp] += 1


with open('./分组/group-results.json', 'w', encoding='UTF-8') as f:
    json.dump(user_info_dict, f, ensure_ascii=False, sort_keys=True, indent=4)

with open('./分组/group-counts.json', 'w', encoding='UTF-8') as f:
    json.dump(group_cnt, f, ensure_ascii=False, sort_keys=True, indent=4)