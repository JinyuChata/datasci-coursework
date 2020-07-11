import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
from collections import Counter

colors2 = '#DC143C'
f_mgr = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# 散点图
def read_data_from_json(from_path):
    # pandas读取csv中的文件
    data = pd.read_json(from_path)
    data_list = []
    case_dict = {}

    for i in data:
        cases_list = data[i]["cases"]
        for case in cases_list:
            case_id = case["case_id"]
            # 创建case数组
            if case_dict.get(case_id) is None:
                case_dict[case_id] = []

            upload_list = case["upload_records"]
            upload_time_count = len(case["upload_records"])
            # time/total, score
            cnt = 0
            for upload in upload_list:
                cnt += 1
                case_dict[case_id].append((cnt / upload_time_count, upload['score']))
    return case_dict

def execScatter():
    case_dict = read_data_from_json("test_data.json")

    xtick_labels = [(i*0.1) for i in range(11)]
    xtick_labels_l = ["{:.1f}".format(i*0.1) for i in range(11)]
    ytick_labels = range(101)
    for case_id in case_dict.keys():
        case_info = case_dict[case_id]
        x = []
        y = []
        for c in case_info:
            x.append(c[0])
            y.append(c[1])

        weights = [3 * i for i in Counter(x).values() for j in range(i)]
        plt.figure(figsize=(20, 8), dpi=80)
        plt.scatter(x, y, s=weights, c=colors2, alpha=0.4)
        plt.xticks(xtick_labels, xtick_labels_l)
        plt.yticks(ytick_labels[::10], ytick_labels[::10])
        plt.xlabel("提交次数/总次数", fontproperties=f_mgr)
        plt.ylabel("分数", fontproperties=f_mgr)
        plt.savefig("./imgs/"+str(case_id)+".png")
        # plt.show()
        # break

