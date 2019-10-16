import tkinter
from tkinter import ttk  # 导入内部包
from spider import SpiderXiaoMi


def go():
    #  获取种类

    type = typevalue.get()

    # 通过种类获得物品
    goods = data[type]


    # 先执行清空之前的item
    x = tree.get_children()
    for item in x:
        tree.delete(item)

    # 下标
    index = 1

    for d in goods:   #  goods   [{'小米9 Pro 5G': '3699元起'}, {'小米MIX Alpha': '19999元'}, {'小米CC9': '1799元起'}, {'小米CC9e': '1299元起'}, {'小米CC9 美图定制版': '2599元'}, {'小米9': '2799元起'}]
        for k,v in d.items():
            # 插入数据
            tree.insert("", index, values=(index, k, v))
            index = index + 1





def start_spider():
    """爬虫启动"""
    spider = SpiderXiaoMi()
    return spider.start_spider()




def get_types(data):
    """获取到种类"""
    types = []

    for key,value in data.items():
        types.append(key)

    return types



# 窗口
win = tkinter.Tk()
# 标题
win.title('MI')

# 启动爬虫
data = start_spider()

#  获取种类列表
type_list = get_types(data)

# 种类框
timelabel = ttk.Label(win,text="种类: ")
timelabel.grid(row=0,column=0)



# 种类列表框

typevalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
comboxlist2 = ttk.Combobox(win, textvariable=typevalue)  # 初始化
comboxlist2["values"] = type_list
comboxlist2.current(0)  #选择第一个
comboxlist2.grid(row=0,column=1)

# 按钮
button = ttk.Button(win, text="查询", command=go)

button.grid(row=0,column=2)

# 数据标题
timelabel = ttk.Label(win,text="数据: ")
timelabel.grid(row=1,column=0)

# 表格
tree = ttk.Treeview(win,show="headings")  # 表格

tree["columns"] = ("序号", "商品", "价格")
tree.column('序号',width=50,anchor="center")
tree.column("商品", width=200,anchor="center")  # 表示列,不显示
tree.column("价格", width=200,anchor="center")


tree.heading('序号',text='序号')
tree.heading("商品", text="商品")  # 显示表头
tree.heading("价格", text="价格")

tree.grid(row=2,columnspan=4)


win.mainloop()