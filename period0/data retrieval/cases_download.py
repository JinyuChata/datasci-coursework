from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.parse
import os
import json
nestedDic = lambda: defaultdict(nestedDic)
dir = nestedDic()

def download(urlandfilename):
    url = urlandfilename[0]
    filename = urlandfilename[1]
    print(filename)
    urllib.request.urlretrieve(url,filename)
    print(filename+"  Done !")

with open("Datas\\cases_url.json","r",encoding="utf-8") as load_fl:
    load_dict = json.load(load_fl)
urls = []
if not os.path.exists(os.getcwd()+"\\cases"):
    os.mkdir(os.getcwd()+"\\cases")
for case_id in load_dict:
    urls.append((load_dict[case_id],"cases\\"+case_id+".zip"))

with ThreadPoolExecutor(32) as executor:
    executor.map(download,urls)