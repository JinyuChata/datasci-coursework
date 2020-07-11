#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=20);


x=range(0,8)
y1=[-1.1,-1.1,-1.4,-2.2,-1.9,-3.0,-0.8,-1.3]
y2=[-2.2,-1.1,-2.4,-2.9,-2.3,-2.6,-1.5,-0.3]
y3=[-2.8,-1.4,-3.1,-3.8,-3.6,-4.2,-3.1,-1.8]
y4=[-2.7,-0.7,-1.9,-2.0,-2.4,-2.6,-2.7,-1.3]
y5=[-2.6,-0.4,-2.1,-1.9,-2.9,-2.5,-1.8,-1.0]


plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y1,label="group1")
plt.plot(x,y2,label="group2")
plt.plot(x,y3,label="group3")
plt.plot(x,y4,label="group4")
plt.plot(x,y5,label="group5")


plt.grid(alpha=0.4,linestyle=":")#alpha透明度





_x=list(x)
print(_x)
_xtick_labels=["array","graph","linear","number","searching","sorting","string","tree"]
plt.xticks(_x,_xtick_labels,fontproperties=my_font)











plt.xlabel("category",fontproperties = my_font)
plt.ylabel("difficulty",fontproperties = my_font)
plt.title("difficultie of each category in each group",fontproperties = my_font)

plt.legend(prop=my_font,loc=3)#图例 只有这里是prop 其他都是properties
plt.show()