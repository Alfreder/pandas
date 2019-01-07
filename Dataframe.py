#-*- coding: utf-8 -*-
import pandas as pd
import xlrd
import numpy as np
excel_path =r'/Users/kun/Desktop/Citation/patent1.xlsx'
d = pd.read_excel(excel_path, header=0, index_col=None, na_values='NULL',dtype=str,sheet_name='Sheet1')
d2 = pd.read_excel(excel_path, header=0, index_col=None, na_values='NULL',dtype=str,sheet_name='Sheet2')
#d.columns = ['a']
#print(d.iloc[0,0])
#d2.columns = ['a']
#查看前5行
print(d.head(5))
print(d.tail(5))
# 查看总行数
print(d.iloc[:,0].size)
#查看总列数
print(d.columns.size)
print('hello')
#print(d)
#print(d2)


#print(d['a'].values[0].split(';'))
#print(d2['a'].values.tolist())

#list1 = d['a'].values[313].split(';')
#list1 = d['a'].values[314]
#print(list1)

list2=d2['H1'].values.tolist()
#print(str(list2))
#list3 = ""
#str1 = ";".join(list2)
#list1 = d['H1'].values[341].split(';')
#print(list1)
#print([x for x in list2 if x in list1])
j = 0
for i in range(0,d.iloc[:,0].size):
    #list1 = []
    list1 = (d['H1'].values[i]).replace(' ','').replace('\n','').replace('\r','').split(';')
    tmp = [x for x in list2 if x in list1]
    print("patent "+ str(i+1) + " citation = " + str(len(tmp)))
    j = j + len(tmp)
print("total citation = " + str(j))
#print(d['Sheet1'])