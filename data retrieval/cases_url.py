from collections import defaultdict
import urllib.request,urllib.parse
import os
import json
nestedDic = lambda: defaultdict(nestedDic)
dir = nestedDic()
with open("data/test_data.json","r",encoding="utf-8") as load_fl:
    load_dict = json.load(load_fl)
for user_id in load_dict:
    for case in load_dict[user_id]['cases']:
        case_id = case['case_id']
        dir[case_id]=urllib.parse.quote(case['case_zip'],safe="/:?=")
print(len(dir))
with open("data/cases_url.json",'w',encoding='utf-8') as ans:
     json.dump(dir,ans,ensure_ascii=False,indent=4)