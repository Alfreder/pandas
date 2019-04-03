#处理仿真数据
import pandas as pd
#l = "Production 1_1 (1 2000)"
l = input('请输入列名：')
filename = "./lie/all_"+l+".txt"
file = open(filename,'a+')
# 写入列名
file.write(l)
file.write('\n')
for i in range(1,10):
    #print(i)
    file_path = "./lie/InnEEInnXBank_"+str(i)+".res"
    #print(file_path)
    data = pd.read_table(file_path)
    columns = data.columns.values.tolist()
    #print(columns)

    col_xian = []  # 存储包含‘列名’字段的列名
    for i in columns:
        if l in i:
            col_xian.append(i)
    print(col_xian)
    df_xian = data[col_xian]
    #print(df_xian)

    #print(data.iloc[:,2])
    #list2=data.iloc[:,6].values.tolist()
    #filename = r'/Users/kun/Desktop/txt/all.txt'
    filename = "./lie/all_"+l+".txt"

    data = df_xian.iloc[:,0].values.tolist()
    file = open(filename,'a+')

    #写入列名下的数据
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',','') +'\n' #\n按列写入,\t 按行写入
        file.write(s)
    #file.write('\n')
    file.close()
    print("保存文件成功")