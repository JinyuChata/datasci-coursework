import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
from collections import Counter
import json

f_mgr = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

def read_data_from_json(from_path):
    # pandas读取csv中的文件
    data = pd.read_json(from_path)

    with open("./cases_analysis_source.json", 'r', encoding='UTF-8') as f:
        load_dict = json.load(f)

    for i in data:
        cases_list = data[i]["cases"]
        for case in cases_list:
            case_id = case["case_id"]
            # 处理提交人数
            if load_dict.get(case_id).get("提交人数") is None:
                load_dict[case_id]["提交人数"] = 1
            else:
                load_dict[case_id]["提交人数"] += 1

            # 创建相关系数表
            if load_dict.get(case_id).get("面向用例人数") is None:
                load_dict[case_id]["面向用例人数"] = 0

            corr_list_origin_data_score = []
            corr_list_origin_data_division = []
            upload_list = case["upload_records"]
            upload_time_count = len(case["upload_records"])
            # time/total, score
            cnt = 0
            for upload in upload_list:
                cnt += 1
                corr_list_origin_data_score.append(upload['score'])
                corr_list_origin_data_division.append(cnt / upload_time_count)

            if upload_time_count >= 3:
                # 大于等于3的情况下 才有必要计算相关系数
                d = pd.DataFrame({'score': corr_list_origin_data_score,
                                  'division': corr_list_origin_data_division})
                if d.corr().iat[0, 1] >= 0.5:
                    load_dict[case_id]["面向用例人数"] += 1

            # 满分人数统计
            if load_dict.get(case_id).get('满分人数') is None:
                load_dict.get(case_id)['满分人数'] = 0
            if case['final_score'] == 100:
                load_dict.get(case_id)['满分人数'] += 1


    with open('new_cases_data.json', 'w', encoding='UTF-8') as f:
        json.dump(load_dict, f, ensure_ascii=False,sort_keys=True, indent=4)
    return load_dict

if __name__ == '__main__':
    read_data_from_json('./test_data.json')
