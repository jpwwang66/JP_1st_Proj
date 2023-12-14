# Rock paper scissors 2.py  editted from a previous file
from tkinter import *
import random
import time
import os

def showFinal(i):
    if g1.get() != 0:
        matchmapping=[[1,2,0],[0,1,2],[2,0,1]]   # 列是你出拳，行是電腦出拳，0是你贏，1平手，2電腦贏
        matchlist=[["你獲勝",1,0,0],["雙方平手",0,1,0],["電腦獲勝",0,0,1]]  # ["xxx",你贏加一筆，平手加一筆，你輸加一筆]
        Label(image=imagelist[i],text=game0[i],compound=TOP).grid(row=1,column = 1)  # 顯示:你出拳
        cpx=random.randint(0,2)   # 電腦隨機出拳
        Label(font="24",width=8,text=matchlist[matchmapping[i][cpx]][0]).grid(row=1,column = 2)  #依表查出輸贏                    
        Label(text=game0[cpx],image=imagelist[cpx],compound=TOP).grid(row=1,column = 3)  # 顯示:電腦出拳
        g1.set(g1.get()-1)
        w0.set(w0.get()+matchlist[matchmapping[i][cpx]][1])  # 你贏數
        ev0.set(ev0.get()+matchlist[matchmapping[i][cpx]][2])  # 平手數
        lo0.set(lo0.get()+matchlist[matchmapping[i][cpx]][3])   # 你輸數
        if g1.get() == 0:
            k0=(w0.get()+ev0.get()+lo0.get())
            temp0 = time.asctime()+"   "+str(n0.get())+"   玩" + str(k0) +"場.  贏" +str(w0.get()) +"場.  平手" +str(ev0.get())+"場.  輸"+ str(lo0.get())+"場."
            lb0.set(temp0)            

def show3():   # 存檔與重置
    file0=open("rock.txt", mode="a")
    print(lb0.get(),file=file0)
    file0.close()
    n0.set("")
    g1.set(0)
    w0.set(0)
    ev0.set(0)
    lo0.set(0)
    lb0.set("")

def show4():  # 另開視窗顯示歷史資料
    global sliderlimit
    def show44():
        AA=[]
        fn = 'rock.txt'
        with open(fn,'r') as fileobj:
            for line in fileobj:
                line=line.rstrip()
                AA.append(line)
            datalen = len(AA)
            print(datalen)
            strAA=""    
            for n2 in range(len(AA)):
                strAA=strAA+(AA[n2]+"\n")
        return AA,strAA, datalen

    def showsome(self):
        global sliderlimit
        nos = slider2.get()
        AA=[]
        fn = 'rock.txt'
        with open(fn,'r') as fileobj:
            for line in fileobj:
                line=line.rstrip()
                AA.append(line)
        datalen = len(AA)
        sliderlimit=datalen
        print(sliderlimit)
        strAA=""    
        for n2 in range(nos-1, len(AA)):
            strAA=strAA+(AA[n2]+"\n")
        label4["text"]= strAA
        e40.delete(0,END)
        e40.insert(1,AA[nos-1])
        slider2.update()

    def editdata(todo, data0,nos):
        datalen=len(data0)
        print(nos)
        if todo == "插入":
            print("插入")
            temp0 = data0[0:nos]
            temp0.append(e40.get())
            temp0.extend(data0[nos:datalen])
            data0 = temp0[:]
        elif todo == "覆蓋":
            print("覆蓋")            
            temp0 = data0[0:nos-1]
            temp0.append(e40.get())
            temp0.extend(data0[nos:datalen])
            data0 = temp0[:]
        elif todo == "刪除":
            print("刪除")
            temp0 = data0[0:nos-1]
            temp0.extend(data0[nos:datalen])
            data0 = temp0[:]

        else:
            pass

        os.remove("rock.txt")
        with open("rock.txt", mode="a") as fileobj:
            for i in range(len(data0)):
                print(data0[i],file=fileobj)
        rec.destroy()
        show4()
        
    rec = Tk()
    rec.geometry("600x600")  # 視窗大小
    content0=StringVar()
    sliderlimit=IntVar()
    sliderlimit.set(20)
    rec.title("Rock_paper_scissors歷史紀錄")          # 視窗標題
    e40 = Entry(rec,width=70,justify="center",fg="red")
    e40.pack()
    data0, wholedata, sliderlimit =show44()
    content0.set(wholedata)
    print("content0=\n",content0.get())
    print(data0)
    label4 = Label(rec,width=70,height=20,anchor= "n",text=wholedata)  #textvariable=content0.get()).pack()
    label4.pack()
    slider2 = Scale(rec,from_=1,to=sliderlimit, orient=HORIZONTAL,length=300,command=showsome)
    slider2.pack()

    btn1 =Button(rec,width=6,height=1,text="插入",command = lambda:editdata("插入", data0,slider2.get()))
    btn1.pack()
    btn2 =Button(rec,width=6,height=1,text="覆蓋",command = lambda:editdata("覆蓋", data0,slider2.get()))
    btn2.pack()
    btn3 =Button(rec,width=6,height=1,text="刪除",command = lambda:editdata("刪除", data0,slider2.get()))
    btn3.pack()
    rec.mainloop()




window = Tk()
window.geometry("550x600")  # 視窗大小
window.title("猜拳")          # 視窗標題

game0=["剪刀","石頭","布"]   # 陣列


Label(window,width=20,height=10,text="").grid(row=1,column = 1)   # 以下連續橫列3個空白標籤，佔位置(第一橫列)
Label(window,width=20,height=10,text="").grid(row=1,column = 2)   # 參考上面
Label(window,width=20,height=10,text="").grid(row=1,column = 3)   # 參考上面

l1=Label(window,text="你出拳")  # 以固定位置標上"電腦出拳"，(在label2上面)
l1.place(x=50,y=20)
l2=Label(window,text="電腦出拳") # 以固定位置標上"電腦出拳"，(在label2上面)
l2.place(x=335,y=20)

imagelist=[]
for xxx in game0:
    imagelist.append(PhotoImage(file=xxx +".gif"))

Button(window,text=game0[0],width=65,image=imagelist[0],compound=TOP,command=lambda:showFinal(0)).grid(row=2,column = 1)
Button(window,text=game0[1],width=65,image=imagelist[1],compound=TOP,command=lambda:showFinal(1)).grid(row=2,column = 2)
Button(window,text=game0[2],width=65,image=imagelist[2],compound=TOP,command=lambda:showFinal(2)).grid(row=2,column = 3)

namex=[0,1,2]
lb = Label(window, text='')
lb.place(x=10,y=350)
pg=[]
g1= IntVar()  #局數
w0=IntVar()   # 你贏數
ev0=IntVar()  # 平手數
lo0=IntVar()  # 你輸數 
n0=StringVar()  # 名字
lb0=StringVar()
g1.set(0)
w0.set(0)
ev0.set(0)
lo0.set(0)
lb0.set("")
temp0=""


name0_label = Label(window, text='名字?')
name0_label.place(x=10,y=250)
name0=Entry(window,width=12,textvariable=n0)
name0.place(x=50,y=250)

games_label = Label(window, text='局數?')
games_label.place(x=10,y=300)
games_text=Entry(window,width=6,textvariable=g1)
games_text.place(x=50,y=300)

win_label = Label(window, text='你贏?')
win_label.place(x=120,y=300)
win0_text=Entry(window,width=6,textvariable=w0)
win0_text.place(x=150,y=300)

even_label = Label(window, text='平手?')
even_label.place(x=220,y=300)
even0_text=Entry(window,width=6,textvariable=ev0)
even0_text.place(x=250,y=300)

lose_label = Label(window, text='你輸?')
lose_label.place(x=320,y=300)
lose0_text=Entry(window,width=6,textvariable=lo0)
lose0_text.place(x=350,y=300)

lb = Label(window, textvariable=lb0)
lb.place(x=10,y=350)

btn3=Button(window,text="存檔與重置",width=12,compound=TOP,command=show3)
btn3.place(x=400,y=350)

btn4=Button(window,text="檢視紀錄",width=12,compound=TOP,command=show4)
btn4.place(x=400,y=390)


window.mainloop()






