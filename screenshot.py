from tkinter import *
import pyautogui
import time
from PIL import ImageTk,Image
window=Tk()
name=""
def datas():
    print(username_value.get())
    t1.insert(END,username_value.get())
    cleartext()

def cleartext():
    name=username_value.get()
    e1.delete(first=0,last=200)
    e1.update()
    window.destroy()
    time.sleep(2)
    newwindow(name)
    #newwindow(newshot)
def newwindow(iname):
    def saveit(names):
            pathfile=r"C:\\test\\"
            screen.save(pathfile+names+".png")
    imgname=iname
    screen= pyautogui.screenshot()

    #screen.save(pathfile+imgname+".png")
    apps=Tk()
    time.sleep(5)
    #load=Image.open(screen)
    render=ImageTk.PhotoImage(screen)
    img = Label(apps, image=render)
    img.image = render
    img.place(x=0, y=0)
    b2=Button(apps,text="save",command=saveit(imgname),width=8,height=1)
    b2.grid(row=2,column=6,padx=10,pady=10 ,columnspan=10,sticky=E)

b1=Button(window,text="submit",command=datas)
b1.grid(row=0,column=1,pady=3,columnspan=1,sticky=W)

username_value= StringVar()
e1=Entry(window,textvariable=username_value)
e1.grid(row=0,column=4,padx=3,columnspan=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1,columnspan=6)


window.wm_title("ScreeshotSoft")
window.mainloop()
