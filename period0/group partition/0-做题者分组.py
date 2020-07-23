import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
from collections import Counter
import json


data = pd.read_json("./test_data.json")
partition_list = {}
validate_set = set()

for user_id in data:
    cases_list = data[user_id]["cases"]
    this_partition_list = []
    for case in cases_list:
        this_partition_list.append(case['case_id'])
    this_partition_list.sort()

    if len(this_partition_list) > 199:
        first_three_tuple = tuple(this_partition_list[0:20])
        if first_three_tuple not in validate_set:
            validate_set.add(first_three_tuple)
            partition_list[user_id] = this_partition_list


with open('分组/group-tests.json', 'w', encoding='UTF-8') as f:
    json.dump(partition_list, f, ensure_ascii=False, sort_keys=True, indent=4)
