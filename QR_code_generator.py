#MODULES
import qrcode
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as ms
import os,sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def qr_make():
    #from PIL import ImageTk, Image
    global link_lb
    global can
    global win

    link=str(link_lb.get())
    if link != '':
        qr_stru=qrcode.QRCode(version=4,box_size=4,border=2)
        link_data=f'{link}'
        qr_stru.add_data(link_data)
        qr_stru.make(fit=True)
        img=qr_stru.make_image(fill='black',back_color='white')
        img.save('QR_CODE.jpg')
        ms.showinfo('success','QR CODE is CREATED and SUCCESSFULLY saved as QR_CODE(format .jpg)')
        img = ImageTk.PhotoImage(Image.open(resource_path('QR_CODE.jpg')))
        can.create_image(70, 120, image=img, anchor='nw')
        win.mainloop()
    else:
        ms.showinfo('ERR','kindly enter LINK,name,etc')

def call_again():
    global win
    win.destroy()
    qr_gen()
def qr_gen():
    global win
    global link_lb
    global can

    win=Tk()
    win.geometry('300x300')
    win.title("QR_CODE GENERATOR")
    win.resizable(False,False)

    #  CANVAS

    can=Canvas(win,width=300,height=300)
    can.pack(fill='both',expand=True)

    img_bg=ImageTk.PhotoImage(Image.open(resource_path('qr_code_bg image.jpg')))
    can.create_image(0,0,image=img_bg,anchor='nw')

    can.create_text(70,30,font=('arial',12,'bold'),text='Enter the link:- ',fill='black')

    link_lb=Entry(win,font=('arial',12,'bold'),width=18)
    can.create_window(210,30,window=link_lb)

    But_create=Button(win,font=('arial',12,'bold'),text='ACCEPT',command=qr_make,bg='white')
    can.create_window(70,80,window=But_create)

    quit_create=Button(win,font=('arial',12,'bold'),text='QUIT',command=win.destroy,bg='grey')
    can.create_window(240,80,window=quit_create)

    clear_create=Button(win,font=('arial',12,'bold'),text='CLEAR',command=call_again,bg='light grey')
    can.create_window(163,80,window=clear_create)

    win.mainloop()

qr_gen()