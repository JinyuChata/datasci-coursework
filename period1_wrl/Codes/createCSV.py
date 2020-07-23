
# -*- coding: utf-8 -*-

from collections import defaultdict
# import urllib.request,urllib.parse
# import os
import json
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


nestedDic = lambda: defaultdict(nestedDic)
dir = nestedDic()
# plt.figure(figsize=(40,20),dpi=80)

#读取文件
#test文件按照类别分类
#cases_test题目id分类
with open("Datas\\test.json","r",encoding="utf-8") as load_fl:
    test_dict = json.load(load_fl)

with open("Datas\\cases_test.json","r",encoding="utf-8") as load_fl:
    ctest_dict = json.load(load_fl)

#设置要保存的csv文件头
header = ["id","均分","提交次数","测试用例个数","答案代码行数"]

#读取计算相应的数据
for case_type in test_dict:
    res = []
    for case_id in test_dict[case_type]:
        temp_res = [case_id]
        #current_case获取当前题目的所有提交分数,list
        current_case = test_dict[case_type][case_id]
        temp_res.append(np.mean(current_case))
        temp_res.append(len(current_case))
        temp_res.append(ctest_dict[case_id]["测试用例个数"])
        temp_res.append(ctest_dict[case_id]["脚本行数"])
        #添加在res中
        res.append(temp_res)
        # print(res)
    
    #同一类型的数据构建完成后,保存文件,路径为./Datas/TOPSIS/{CASE_TYPE}.CSV
    with open(f'Datas\\{case_type}.csv', mode='w',encoding="utf-8") as csvf:
        writer = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(res)
        
