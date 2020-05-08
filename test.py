import json
class AutoVivification(dict):
 """生成嵌套字典"""
 def __getitem__(self, item):
    try:
        return dict.__getitem__(self, item)
    except KeyError:
        value = self[item] = type(self)()
        return value
dir = AutoVivification()
case_id_list=[]
with open("data/test_data.json",'r',encoding='utf-8') as load_f:
     load_dict = json.load(load_f)
for i in load_dict:#i为学生id j为case_id
    for j in load_dict[i]['cases']:
        dir[j['case_id']]['题目类别']=j['case_type']
        dir[j['case_id']]['总提交次数'] = 0
        dir[j['case_id']]['有效提交次数'] = 0
        dir[j['case_id']]['平均得分']=0
        dir[j['case_id']]['方差']=0
for i in load_dict:#i为学生id j为case_id
    for j in load_dict[i]['cases']:
        dir[j['case_id']]['总提交次数'] += len(j["upload_records"])
        for h in j["upload_records"]:#h为一次次提交的信息
            if h['score']==100:
                dir[j['case_id']]['有效提交次数'] += 1
            dir[j['case_id']]['平均得分'] += h['score']
for i in dir:#i为case_id
    dir[i]['平均得分']=dir[i]['平均得分']/dir[i]['总提交次数']#计算平均值
for i in load_dict:#i为学生id j为case_id
    for j in load_dict[i]['cases']:
        for h in j["upload_records"]:  # h为一次次提交的信息
            dir[j['case_id']]['方差'] += pow(h['score']-dir[j['case_id']]['平均得分'],2)
for i in dir:#i为case_id
    dir[i]['方差']=dir[i]['方差']/dir[i]['总提交次数']#计算平均值
sorted(dir)
# print(dir)
with open("data/题目难度分析V1.json",'w',encoding='utf-8') as ans:
     json.dump(dir,ans,ensure_ascii=False,indent=4)