# -*- coding: utf-8 -*-


import os
from os import path
import glob
import pandas as pd
LOCATE_PY_FILENAME = __file__
LOCATE_PY_DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))
LOCATE_PY_PARENT_DIR = os.path.abspath(os.path.join(LOCATE_PY_DIRECTORY_PATH, ".."))
data_path = os.path.join(LOCATE_PY_PARENT_DIR,'DATA\\DATA.csv')

d = pd.read_csv(data_path, sep=',', encoding='utf-8')

label = d['label']
title = d['title']
content = d['content']
text = []
for i in range (0, len(title)):
  text.append(str(title[i]) +str(' ') + str(content[i]))
print('ok')

change_label = { 
'ChinhTri' : 'Chính trị',
'DoanhNghiep': 'Doanh nghiệp',
'BatDongSan': 'Bất động sản',
'ChungKhoan': 'Chứng khoán',
'PhatMinh': 'Khoa học',
'Khoa hoc trong nuoc': 'Khoa học',
'UngDung': 'Khoa học',
'Phim' :'Giải trí',
'Nhac': 'Giải trí',
'Sach': 'Giải trí',
'Gioisao': 'Giải trí', 
'DanSinh':'Dân sinh', 
'GiaoThong': 'Giao thông', 
'HoSoPhaAn': 'Pháp luật', 
'Phapluat' : 'Pháp luật',
'DuHoc': 'Giáo dục', 
'KhoeDep': 'Sức khỏe',
'DanOng' : 'Sức khỏe',
'Tintuc': 'Sức khỏe', 
'ThiTruong': 'Thị trường', 
'BongDa':'Thể thao',
'Affcup2020':'Thể thao',
'Hautruong' :'Thể thao',
'Tuongthuat':'Thể thao',
'WorldCup2022':'Thể thao',
'Euro2021':'Thể thao',
'Ecommerce40' :'Kinh doanh',
'ViMo':'Kinh doanh',
'HangHoa' :'Kinh doanh',
'Ebank' :'Kinh doanh',
'QuocTe' :'Kinh doanh',
'BaoHiem' :'Kinh doanh',
'TienCuaToi' :'Kinh doanh',
}

save_path = os.path.join(LOCATE_PY_PARENT_DIR,'DATA')

data = pd.DataFrame(columns=['labels', 'texts'])
labels = []
texts = []

max = len(label)
for i in range(0, max):
    
    if(label[i] in change_label):
        labels.append(change_label[label[i]])
        texts.append(text[i])
print(len(label))
print(len(text))
print('ok')
data['labels'] = labels
data['texts'] = texts
data.to_csv(os.path.join(save_path,'DATA_remove_thoisu.csv'), sep=',', encoding='utf-8', index=False)
i = {}
count = 0

for d in labels:
    if d in i:
        i[d] += 1;
    else: 
        i[d] = 1
print (i)
print(len(labels))




