'''import tkinter
from tkinter import *
from PIL import ImageTk, Image'''
import random

global point
global contain_list
global ques_tkinter

def quiz_generator(num_ques):
    count = 1
    point = 0
    contain_list = []
    file = open('quiz file.txt','r',newline='\n')
    file_read = file.readlines()
    if num_ques == 1:
        while True:
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
                user_input = input('Enter the answer plz: ')
                user_input = user_input.lower()

                if user_input == ans:
                    print('your answer is correct')
                    point += 1
                else:
                    print('sorry wrong answer')
                    print('Your score is: ',point)
                    break
            else:
                pass
    else:
        num_ques = int(input('Please enter a valid number(1): '))
        quiz_generator(num_ques)


num_ques = int(input('Enter 1 to start the test: '))
quiz_generator(num_ques)

