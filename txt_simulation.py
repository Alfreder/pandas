#处理仿真数据

import pandas as pd

for i in range(1,11):
    print(i)
    file_path = "./txt/Market -alpha0.1_"+str(i)+".res"
    print(file_path)
    data = pd.read_table(file_path)

    #print(data.iloc[:,2])
    list2=data.iloc[:,6].values.tolist()
    #filename = r'/Users/kun/Desktop/txt/all.txt'
    filename = r'./txt/all.txt'
    data = list2
    file = open(filename,'a+')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',','') +'\t'
        file.write(s)
    file.write('\n')
    file.close()
    print("保存文件成功")