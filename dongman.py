import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
import tkinter as t
import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webbrowser
import PyInstaller
#界面设置
root=ttk.Window(themename="solar")
root.title("vip视频")
root.geometry("800x400+610+200")
root.resizable(False,False)
lable_1=ttk.Label(root,text="vip视频随便看！",font=("arial",20),style="success")
lable_1.place(x=300,y=10)
f=ttk.Separator(root,style="prinary")
f.place(x=10,y=70,width=780)
labe_2=ttk.Label(root,text="腾讯视频",style="inverse-danger",font=("arial",20),anchor=CENTER)
labe_2.place(x=50,y=90,height=50,width=200)
labe_3=ttk.Label(root,text="爱奇艺视频",style="inverse-primary",font=("arial",20),anchor=CENTER)
labe_3.place(x=300,y=90,height=50,width=200)
labe_4=ttk.Label(root,text="YoKu",style="inverse-info",font=("arial",20),anchor=CENTER)
labe_4.place(x=550,y=90,height=50,width=200)
root1=ttk.LabelFrame(root,width=760,height=220,style="success",text="开始操作吧！")
root1.pack(ipadx=10,ipady=10,fill=Y,side=BOTTOM)
labe_5=ttk.Label(root1,text="请输入视频链接: ",style="warning",font=("arial",15),anchor=CENTER)
labe_5.place(x=10,y=10)
get1=ttk.StringVar()
get1.set("")
enttry_1=ttk.Entry(root1,font=("arial",15),textvariable=get1)
enttry_1.place(x=225,y=5,width=500)
print(get1.get())
labe_6=ttk.Label(root1,text="选择通道 ",style="warning",font=("arial",15),anchor=CENTER)
labe_6.place(x=30,y=120)
url_vip={"蓝光":'https://vip.bljiex.com/?v=',"蓝光2":'https://jx.xmflv.com/?url=',"爱奇艺专用通道":'//www.daga.cc/vip3/?url=',"优酷":'https://jx.xmflv.com/?url=',"普通0.1":'https://svip.bljiex.cc/?v=',"b站":'https://www.asmrv.com/parse_video?url='}
com=ttk.Combobox(root1,width=10,style="secondary",values=tuple(url_vip.keys()))
com.place(x=160,width=100,y=117)
def das():
    if len(com.get())==0 or len(get1.get())==0:
        t.messagebox.showerror(title="请求失败！", message="请正确输入")
        return
    else:
        url=url_vip[f"{com.get()}"]+get1.get()
        webbrowser.open(url=url)



button = ttk.Button(root1, text="开始观看", style="infor-outline",command=das)
button.place(x=380,y=90,width=200,height=90)



t.mainloop()





