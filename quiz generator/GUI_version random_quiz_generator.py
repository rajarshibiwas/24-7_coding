import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import time

global contain_list
global ques_tkinter
global ans

point = 0
count = 1

contain_list = []

def taking_function():
    global contain_list
    num_ques = 1
    quiz_generator(num_ques,contain_list)
    #tks_funtion(ques_tkinter,ans)
    
       
def checking_function(ans,user_input):
    #global user_input
    global point
    global win
    if user_input != 'none':
        user_input = user_input.get()
        user_input = user_input.lower()
        win.destroy()
        if user_input == ans:
            point += 1
            print(point)
            taking_function()
        else:
            messagebox.showinfo('result', f'Your score is: {point}')
    else:
        win.destroy()
        taking_function()


def tks_funtion(ques_tkinter, ans):
    #global user_input
    global win

    win = Tk()
    win.title('Quiz Generator')
    win.geometry('600x300')
    img = ImageTk.PhotoImage(Image.open('quiz background image.jpg'))
    can = Canvas(win,width=600,height=300)
    can.pack(fill='both', expand=True)

    can.create_image(0,0,image=img,anchor='nw')

    can.create_text(300,50,font=('arial',11,'bold'),text=ques_tkinter)
    can.create_text(300,200,font=('arial',10,'bold'),text='You have 30 sec in hand after it will automatically move to next question.')

    user_input = Entry(win,font=('arial',12,'bold'))
    can.create_window(300,100,window=user_input)

    ac_but = Button(win,font=('arial','10', 'bold'),text='accept',command=lambda: checking_function(ans,user_input),bg='light green')
    can.create_window(300,150,window=ac_but)

    '''clear_but = Button(win,font=('arial','10', 'bold'),text='clear',command=tks_funtion)
    can.create_window(350,150,window=clear_but)'''
    
    win.after(30000, lambda: checking_function(ans,user_input='none'))
    win.mainloop()


def quiz_generator(num_ques,contain_list):
    global count
    
    file = open('quiz file.txt','r',newline='\n')
    file_read = file.readlines()
    if num_ques == 1:
        #while True:
        choice = random.choice(file_read)
        print(choice)
        spl_value = choice.split(',')
        print(spl_value)
        if spl_value not in contain_list:
            contain_list.append(spl_value)
            print(contain_list)
            ques = spl_value[0]
            ans = spl_value[1]
            ans = ans.replace('\r','')
            ans = ans.replace('\n','')
            ans = ans.lower()
            #print(ans)
            ques_tkinter = f'Question {count}. '+ques
            print(ques_tkinter)
            count = count + 1
            #user_input = input('Enter the answer plz: ')
            #user_input = user_input.lower()

            tks_funtion(ques_tkinter, ans)

            '''if user_input == ans:
                print('your answer is correct')
                point += 1
            else:
                print('sorry wrong answer')
                print('Your score is: ',point)
                '''
        else:
            pass
    else:
        num_ques = int(input('Please enter a valid number(1): '))
        quiz_generator(num_ques)


'''num_ques = int(input('Enter 1 to start the test: '))
quiz_generator(num_ques)'''


taking_function()