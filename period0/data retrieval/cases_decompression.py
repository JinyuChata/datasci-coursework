import zipfile
import os
import json
from collections import defaultdict
nestedDic=lambda :defaultdict(nestedDic)
dir=nestedDic()
#解压
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')

#读取json文件对象数量
def get_number_of_objects(case_id):
    path="ziped/"+case_id+"/.mooctest/testCases.json"
    with open(path, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    return len(load_dict)

#读取py脚本行数
def get_number_of_lines(case_id):
    path = "ziped/" + case_id + "/.mooctest/answer.py"
    count = len(open(path, 'r',encoding='utf-8').readlines())
    return count

if not os.path.exists(os.getcwd()+"\\ziped"):
    os.mkdir(os.getcwd()+"\\ziped")
g = os.walk(r"cases")
for path,dir_list,file_list in g:
    for file_name in file_list:
        print(os.path.join(path, file_name) )
        unzip_file(os.path.join(path, file_name), "ziped/"+file_name[:-4])
        dir[file_name[:-4]]['测试用例个数']=get_number_of_objects(file_name[:-4])
        dir[file_name[:-4]]['脚本行数'] = get_number_of_lines(file_name[:-4])

with open("Datas\\cases_test.json",'w',encoding = 'utf-8') as f:
    json.dump(dir,f,ensure_ascii=False)
print(len(dir))