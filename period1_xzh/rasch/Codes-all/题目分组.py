#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);
#处理原始数据
with open('../group-results.json', 'r') as f:
    group_data = json.load(f)
# print(data)
groups={
    "g1":[],
    "g2":[],
    "g3":[],
    "g4":[],
    "g5":[]
}
#转换进去
for key in group_data:
    groups[group_data[key]].append(int(key))


datascisample = pd.read_json("../../pca/test_data.json")

# print(datascisample)
set1=set()
set2=set()
set3=set()
set4=set()
set5=set()
for user_id in datascisample:
    # if(user_id in groups["g1"]):
    dataFrame = datascisample[user_id]
    cases = dataFrame["cases"]

    for j in range(len(cases)):
        # 取得某一个case
        case = cases[j]
        case_id=case["case_id"]
        if user_id in groups["g1"]:
            set1.add(case_id)
        elif user_id in groups["g2"]:
            set2.add(case_id)
        elif user_id in groups["g3"]:
            set3.add(case_id)
        elif user_id in groups["g4"]:
            set4.add(case_id)
        elif user_id in groups["g5"]:
            set5.add(case_id)
result_dict = {
    "g1":sorted(list(set1)),
    "g2":sorted(list(set2)),
    "g3":sorted(list(set3)),
    "g4":sorted(list(set4)),
    "g5":sorted(list(set5))

}
with open('../group-exercises.json', 'w', encoding='UTF-8') as f:
    json.dump(result_dict, f, ensure_ascii=False, sort_keys=True, indent=4)


