import os
import folium
import numpy as np

f1=open("f://icm//data11111.txt","r").read().split("\n")       //经度数据
fx=[]
for item in f1:
    a=eval(item)
    fx.append(a)
f2=open("f://icm//data22222.txt","r").read().split("\n")     //纬度数据
fy=[]
for item in f2:
    a=eval(item)
    fy.append(a)
f3=open("f://icm//data33333.txt","r").read().split("\n")   //地图上的坐标的热力值
fz=[]
for item in f3:
    a=eval(item)
    fz.append(a)
data=[]
i=0
for i in range(len(fx)-1):
    item=[]
    item.append(fx[i])
    item.append(fy[i])
    item.append(fz[i])
    data.append(item)
    
from folium.plugins import HeatMap
 
m = folium.Map([ 33., 113.], tiles='stamentoner', zoom_start=5)
 
HeatMap(data).add_to(m)
 
m.save(os.path.join(r'f://', 'Heatmap_restday1.html'))       //将地图保存在电脑文件里

m /              //显示地图