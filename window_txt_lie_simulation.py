import tkinter as tk
import pandas as pd

window = tk.Tk()
window.title('Simulation_lie')
#window.geometry('200x200')
# e = tk.Entry(window, show="*")
var=tk.StringVar()
var1=tk.StringVar()
var2=tk.StringVar()
var3 = tk.StringVar()
on_hit = False

Label1 = tk.Label(window,text='txt name:').grid(row=0,column=0)
Label2 = tk.Label(window,text='lie name:').grid(row=1,column=0)
Label3 = tk.Label(window,text='txt count:').grid(row=2,column=0)
#e = tk.Entry(window, textvariable=var).pack()
e = tk.Entry(window, textvariable=var)
e.grid(row=0,column=1,padx=10,pady=5)
#e.grid(row=0,column=1)
#f = tk.Entry(window, textvariable=var1).pack()
f = tk.Entry(window, textvariable=var1)
f.grid(row=1,column=1,padx=10,pady=5)

g = tk.Entry(window, textvariable=var2)
g.grid(row=2,column=1,padx=10,pady=5)
#f.grid(row=1,column=1)

def Start():
    txt_name = var.get()
    lie_name = var1.get()
    txt_count = var2.get()
    #print(var.get())
    #print(var1.get())
    try:
        lie(txt_name,lie_name,txt_count)
    except Exception as result:
        #print(result)
        on_hit = result
        hit_me(on_hit)

def lie(txt1,lie1,txt2):
    l = lie1
    #l = "Production 1_1 (1 2000)"
    #l = input('请输入列名：')
    filename = "./lie/all_"+l+".txt"
    file = open(filename,'a+')
    # 写入列名
    #file.write(l)
    #file.write('\n')
    for j in range(0,int(txt2)):
        #print(i)
        #file_path = "./lie/InnEEInnXBank_"+str(j)+".res"
        file_path = "./lie/"+txt1+str(j+1) + ".res"
        #print(file_path)
        data = pd.read_table(file_path)
        columns = data.columns.values.tolist()
        #print(columns)

        col_xian = []  # 存储包含‘列名’字段的列名
        for i in columns:
            if l in i:
                col_xian.append(i)
        #print(col_xian)
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
            s = s.replace("'",'').replace(',','') +'\t' #\n按列写入,\t 按行写入，一个企业在一行
            file.write(s)
        #下一个企业换行
        file.write('\n')
        file.close()
        #print("保存第"+str(j)+"文件成功")
        #global on_hit
        on_hit = True
        hit_me(on_hit)
        on_hit = False
        hit_me(on_hit)
    on_hit = "success"
    hit_me(on_hit)

def hit_me(on):

    if on == True:
        on_hit = False
        var3.set("process...")
    if on == False:
        var3.set("")
    if on == "success":
        var3.set("SUCCESS")
    else:
        var3.set(on)


b1 = tk.Button(window, text='Start', width=15,
              height=2, command=Start)

b1.grid(row=3,columnspan=2,padx=10,pady=5)
#t = tk.Text(window, height=2).pack()
l = tk.Label(window,textvariable=var3,
             bg='green',font=('Arial',12),width=25,height=2)

l.grid(row=4,columnspan=2,padx=10,pady=5)

window.mainloop()