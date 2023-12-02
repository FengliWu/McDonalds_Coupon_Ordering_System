from tkinter import messagebox
import xlrd
import time
import tkinter as tk
import pickle
import random
from tkinter import *


def main1():
    def confirm(name_arg, address_arg):
        Label(root2, text='##############' + '\n\n' + '请查收您的订单：').grid(column=0, row=2)
        Label(root2, text=order).grid(column=0, row=3)
        Label(root2, text=f'姓名：{name_arg}').grid(column=0, row=5)
        Label(root2, text=f'地址：{address_arg}').grid(column=0, row=6)
        Label(root2, text='谢谢惠顾\n##############').grid(column=0, row=4)

    root2 = Tk()
    root2.title("麦当劳优惠券点单平台")
    root2.geometry("480x720")
    root2.resizable(0, 0)
    ord_name = tk.StringVar()
    ord_address = tk.StringVar()
    Label(root2, text='姓名：').grid(column=0, row=0)
    e1 = Entry(root2, textvariable=ord_name)
    e1.grid(column=1, row=0)
    Label(root2, text='地址：').grid(column=0, row=1)
    e2 = Entry(root2, textvariable=ord_address)
    e2.grid(column=1, row=1)
    Button(root2, text="确认", command=lambda: confirm(e1.get(), e2.get())).grid(column=5, row=1)
    mainloop()


def main():
    root1.destroy()


en1 = None
en2 = None
bt1 = None
bt2 = None
bt3 = None


def unlock():
    b = v.get()

    if b == 2:
        global en1, en2, bt1, bt2, bt3

        en1 = tk.Entry(login_frame, width=40, textvariable=name, state=NORMAL).place(relx=0.3, rely=0.2)
        en2 = tk.Entry(login_frame, width=40, textvariable=password, state=NORMAL).place(relx=0.3, rely=0.3)
        bt1 = tk.Button(login_frame, width=34, text='登录', font=('华文细黑', 10, 'bold'), bd=3, relief=GROOVE, bg='#cccccc',
                        fg='white',
                        command=login).place(
            relx=0.2,
            rely=0.8)

    else:
        en1 = tk.Entry(login_frame, width=40, textvariable=name, state=DISABLED).place(relx=0.3, rely=0.2)
        en2 = tk.Entry(login_frame, width=40, textvariable=password, state=DISABLED).place(relx=0.3, rely=0.3)


def login():
    usr_name = name.get()

    usr_pwd = password.get()

    try:

        with open('users_info.pickle', 'rb') as usr_file:

            users_info = pickle.load(usr_file)

    except FileNotFoundError:

        with open('users_info.pickle', 'wb') as usr_file:

            users_info = {'admin': 'admin'}

            pickle.dump(users_info, usr_file)

    if usr_name in users_info:

        if usr_pwd == users_info[usr_name]:

            root1.destroy()
            global iden
            iden = 1

        else:

            tk.messagebox.showerror(message='密码错误，请重新输入。')

    else:

        is_sign_up = tk.messagebox.askyesno('Error', '您是否需要注册账号')

        if is_sign_up:
            sign_up()


def sign_up():
    def sign():

        nn = new_name.get()

        np = new_pwd.get()

        npf = new_pwd_confirm.get()

        with open('users_info.pickle', 'rb') as usr_file:

            exist_usr_info = pickle.load(usr_file)

        if np == npf == '':

            tk.messagebox.showerror('Error', '两次密码均不能为空，请重新输入')

        elif np != npf:

            tk.messagebox.showerror('Error', '两次密码不一致，请重新输入!')

        elif nn in exist_usr_info:

            tk.messagebox.showerror('Error', '用户名已注册，请重新注册!')

        else:

            exist_usr_info[nn] = np

            with open('users_info.pickle', 'wb') as usr_file:

                pickle.dump(exist_usr_info, usr_file)

            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')

        window_sign_up.destroy()

    window_sign_up = tk.Toplevel(

        root1)

    window_sign_up.title('账号注册')

    window_sign_up.geometry('350x200')

    new_name = tk.StringVar()

    tk.Label(window_sign_up, font=('华文细黑', 10), text='用户名: ').grid(row=0, column=0)

    entry_new_name = tk.Entry(window_sign_up, font=10, textvariable=new_name)

    entry_new_name.grid(row=0, column=1)

    new_pwd = tk.StringVar()

    tk.Label(window_sign_up, font=('华文细黑', 10), text='密码: ').grid(row=1, column=0)

    entry_usr_pwd = tk.Entry(window_sign_up, font=10, textvariable=new_pwd, show='*')

    entry_usr_pwd.grid(row=1, column=1)

    new_pwd_confirm = tk.StringVar()

    tk.Label(window_sign_up, font=('华文细黑', 10), text='确认密码: ').grid(row=2, column=0)

    entry_usr_pwd_confirm = tk.Entry(window_sign_up, font=10, textvariable=new_pwd_confirm, show='*')

    entry_usr_pwd_confirm.grid(row=2, column=1)

    btn_comfirm_sign_up = tk.Button(window_sign_up, font=10, text='确认', command=sign)

    btn_comfirm_sign_up.grid(row=3, column=1)


iden = 0
root1 = tk.Tk()
root1.title("外卖点餐系统")
root1.geometry("480x720")
root1.resizable(0, 0)  # 锁定窗口比例
login_frame = Frame(width=300, height=300).place(x=0.2, y=0.1)
lb1 = tk.Label(login_frame, text="外卖登录系统", font=('幼圆', 20, 'bold'), fg=f'#{random.randint(0, 1677215):06x}',
               bg='#cccccc').place(x=160, rely=0.05)
lb2 = tk.Label(login_frame, text="用户名:", font=('华文细黑', 10, 'bold')).place(relx=0.18, rely=0.2)
lb3 = tk.Label(login_frame, text="密码:", font=('华文细黑', 10, 'bold')).place(relx=0.18, rely=0.3)

name = StringVar()
password = StringVar()
en1 = tk.Entry(login_frame, width=40, textvariable=name, state=DISABLED).place(relx=0.3, rely=0.2)
state = DISABLED
en2 = tk.Entry(login_frame, width=40, textvariable=password, state=DISABLED).place(relx=0.3, rely=0.3)

bt2 = tk.Button(login_frame, width=34, text='账号注册', font=('华文细黑', 10, 'bold'), bd=3, relief=GROOVE, bg='#cccccc',
                fg='white',
                command=sign_up).place(
    relx=0.2,
    rely=0.6)
bt3 = tk.Button(login_frame, width=34, text='非会员直接登录', font=('华文细黑', 10, 'bold'), bd=3, relief=GROOVE, bg='#cccccc',
                fg='white',
                command=main).place(
    relx=0.2,
    rely=0.7)
button4 = tk.Button(login_frame, text='确认', width=10, command=unlock, bd=3, relief=GROOVE, ).place(relx=0.7, rely=0.4)
v = IntVar()
Radiobutton(login_frame, text='非会员登录', foreground='blue', variable=v, value=1).place(relx=0.2, rely=0.4)
Radiobutton(login_frame, text='会员登录', foreground='red', variable=v, value=2).place(relx=0.5, rely=0.4)
v.set(1)
root1.mainloop()

# 显示当前时间
time1 = None
time2 = None
time3 = None


def get_time():
    global time1, time2, time3
    time1 = ''
    time2 = time.strftime('%Y-%m-%d %H:%M:%S')
    time3 = time.strftime('%Y%m%d%H%M%S')
    Label(root, text='当前时间:', foreground='blue', font=('华文细黑', 12)).place(x=650, y=0)
    if time2 != time1:
        time1 = time2
        clock = Label(root, text=time1, foreground='blue', font=('华文细黑', 12))
        clock.configure(text=time2)
        clock.place(x=720, y=0)
        clock.after(20, get_time)


def check():
    if listbox['height'] == 0:
        listbox.config(height=10)
        listbox.place(x=200, y=50, width=564, height=405)
        listbox.delete(0, END)
        for i in range(1, 232):
            if l3[i]["text"] != 0:
                listbox.insert(END, lstdata[i] + '   x' + str(l3[i]["text"]))

    else:
        listbox.config(height=0)
        listbox.place(x=10000, y=1000)


decrease_price = None


def rand():
    global decrease_price
    if iden == 1:
        decrease_price = random.randint(int(totl['text'] * 0.05), int(totl['text'] * 0.1))


order = None


# 提交订单
def submit():
    k = messagebox.askokcancel(title='确认页面', message='您确认要提交订单吗？')
    rand()
    global order
    if k:
        global f
        order = ''
        for i in range(1, 232):
            if l3[i]["text"] != 0:
                f = open('order\\' + str(time3) + '.txt', 'a')
                f.write(lstdata[i] + '   x' + str(l3[i]["text"]) + '\n')
        if iden == 1:
            f.write('\n' + '总价:' + str(totl['text']) + '   会员优惠：' + str(decrease_price) + '元' + '  优惠后价格：' + str(
                totl['text'] - decrease_price))
        else:
            f.write('\n' + '总价:' + str(totl['text']))
        f = open('order\\' + str(time3) + '.txt', 'r')
        a = f.readlines()
        for i in range(0, len(a)):
            order = order + a[i]
        f.close()
        main1()


def add(button):  # 加数量
    global gd
    if len(str(button)[15:]) == 0:
        k = 1
    else:
        k = int(str(button)[15:])
    l3[k]["text"] += 1
    totl["text"] += round(float(lstprice[k]), 3)


def minus(button):  # 减数量
    global ttl
    if len(str(button)[15:]) == 0:
        k = 1
    else:
        k = int(str(button)[15:])
    if l3[k]["text"] != 0:
        l3[k]["text"] -= 1
        totl["text"] -= round(float(lstprice[k]), 3)


def srchf():
    lstsrch = Listbox(frm3, font=('华文细黑', 15), width=25)
    lstsrch.grid(row=1, column=0)

    def listbox_click(event):
        # 向文本区光标处插入列表框当前选中文本
        clck = lstsrch.get(lstsrch.curselection())
        srch.delete(0, 'end')
        srch.insert(0, clck)
        lstsrch.destroy()

    # 列表框绑定函数
    lstsrch.bind('<<ListboxSelect>>', listbox_click)
    for i in range(1, 232):
        if srch.get() in lstdata[i]:
            lstsrch.insert(END, lstdata[i])
            cvs1.yview_moveto((i - 1) * 120 / 28000)
    if lstsrch.size() == 1:
        lstsrch.destroy()

    elif lstsrch.size() == 0:
        messagebox.showinfo(title='提示', message='不好意思~暂时没有您搜索的餐品'
                                                '\n可以尝试输入其他餐名哦~')
        lstsrch.destroy()


def srchdlt(self):
    srch.delete(0, 'end')
    srch.configure(fg='Black')


data = xlrd.open_workbook('.\\data\\info.xls')


def f1():
    cvs1.yview_moveto(0 / 28000)  # 点餐页面跳至指定位置


def f2():
    cvs1.yview_moveto(6540 / 28000)


def f3():
    cvs1.yview_moveto(9540 / 28000)


def f4():
    cvs1.yview_moveto(21780 / 28000)


root = Tk()
root.title('外卖点餐系统')
root.resizable(0, 0)
root.geometry('900x540')

# 主画布
cvs1 = Canvas(root, width=500, height=28000, scrollregion=(0, 0, 28000, 28000))
cvs1.place(x=500, y=80)
get_time()
# 购物车清单
listbox = Listbox(root, font=('华文细黑', 15))
# 底部框架
frm2 = Frame(root, bd=1, bg='White', relief=SUNKEN)
frm2.place(x=0, y=454)
pht1 = PhotoImage(file='.\\data\\ui_icon\\order_icon.png')
Label(frm2, image=pht1).grid(row=0, column=0)
Label(frm2, text='您的购物车→', font=('华文细黑', 13), bg='White').grid(row=0, column=1)
pht2 = PhotoImage(file='.\\data\\ui_icon\\shopping_cart_icon.png')
check = Button(frm2, command=check, bd=2, bg='White', fg='Red', image=pht2, relief=GROOVE).grid(row=0, column=2)
Label(frm2, text='总计：', font=('华文细黑', 15), bg='White').grid(row=0, column=3)
totl = Label(frm2, text=0, font=('华文细黑', 14), bg='White', width=14, anchor=E)
totl.grid(row=0, column=4, sticky=E)
Label(frm2, text='元', font=('华文细黑', 15), bg='White', width=18, anchor=W).grid(row=0, column=5, sticky=W)
Button(frm2, text='提交订单', font=('华文细黑', 18), bg='Yellow', fg='Red', command=submit, bd=2, relief=GROOVE, ).grid(row=0,
                                                                                                              column=6,
                                                                                                              sticky=E)
# 主循环体
lstp = {}
frms = {}
lbls = {}
l3 = {}
l4 = {}
l5 = {}
ql = {}
table = data.sheets()[0]
ncols = table.ncols
lstdata = table.col_values(colx=1, start_rowx=0, end_rowx=232)  # 返回由该列中所有单元格的数据组成的列表
lstprice = table.col_values(colx=2, start_rowx=0, end_rowx=232)
lstnum = table.col_values(colx=0, start_rowx=0, end_rowx=232)
quan = {}
good = []
gd = 0
for i in range(1, 232):
    frms[i] = 0
    lstp[i] = 0
    quan[i] = 0
for i in range(1, 232):
    frms[i] = Frame(cvs1, bd=2, relief=RAISED)
    num = int(lstnum[i])
    lstp[num] = PhotoImage(file='.\\data\\item_gif\\' + str(num + 10) + '.gif')
    lbls[i] = Label(frms[i], text=lstdata[i] + '  ￥' + lstprice[i], font=('华文细黑', 12), compound=LEFT, image=lstp[num],
                    width=450, anchor=W)
    lbls[i].grid(row=0, column=0)

    l5[i] = Button(frms[i], text='-', font=('华文细黑', 15, 'bold'), fg='Red', bg='White')
    l5[i].grid(row=0, column=1)
    l5[i].config(command=lambda button=frms[i]: minus(button))

    Label(frms[i], text=' ').grid(row=0, column=2)

    ql[i] = 0
    l3[i] = Label(frms[i], text=ql[i])
    l3[i].grid(row=0, column=3)

    Label(frms[i], text=' ').grid(row=0, column=4)

    l4[i] = Button(frms[i], text='+', font=('宋体', 15, 'bold'), fg='White', bg='Red')
    l4[i].config(command=lambda button=frms[i]: add(button))
    l4[i].grid(row=0, column=5)

    Label(frms[i], text='  ').grid(row=0, column=6)

vbar = Scrollbar(cvs1, orient=VERTICAL, command=cvs1.yview)  # 竖直滚动条
cvs1.configure(yscrollcommand=vbar.set)
vbar.pack(side="right", fill="y")
cvs1.pack(side="left", fill="both", expand=True)
for i in range(1, 232):
    cvs1.create_window(200, i * 120, window=frms[i], anchor="w")

# 搜索栏
frm3 = Frame(root)
frm3.place(x=200, y=0)
Label(frm3, text='  123 ', font=25, width=5000).place(x=100, y=0)
srch = Entry(frm3, font=('华文细黑', 15), fg='Grey', width=25)
srch.insert(0, '请输入您想搜索的餐品')
srch.grid(row=0, column=0)
srch.bind('<Button-1>', srchdlt)
Button(frm3, text='搜索', command=srchf, bg='White').grid(row=0, column=1)

# 侧边按钮
frm1 = Frame(root)
frm1.place(x=0, y=69)

Button(frm1, text='超值套餐', font=('华文细黑', 17), height=3, width=12, activeforeground='Pink', bg='White', fg='Red',
       command=f1, bd=3, relief=GROOVE).grid(row=0, column=0)
Button(frm1, text='人气汉堡', font=('华文细黑', 17), height=3, width=12, activeforeground='Pink', bg='White', fg='Red',
       command=f2, bd=3, relief=GROOVE).grid(row=1, column=0)
Button(frm1, text='小食甜品', font=('华文细黑', 17), height=3, width=12, activeforeground='Pink', bg='White', fg='Red',
       command=f3, bd=3, relief=GROOVE).grid(row=2, column=0)
Button(frm1, text='冷热饮品', font=('华文细黑', 17), height=3, width=12, activeforeground='Pink', bg='White', fg='Red',
       command=f4, bd=3, relief=GROOVE).grid(row=3, column=0)

root.mainloop()

############################################
