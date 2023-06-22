import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


new_s_list = []
header_list = []

no_value = 0
row_1st, clms1 = 0, 0
row_2nd, clms2 = 0, 0
row_3rd, clms3 = 0, 0
row_4th, clms4 = 0, 0
row_5th, clms5 = 0, 0

file_name = input('Enter the file name with extension in which you want to save data: ')
if '.' in file_name:
    url = input('Enter the URL of the you desire: ')
    rows = int(input('Enter the number of rows: '))
    columns = int(input('Enter the number of colums: '))

    if columns < 6:
        print('success1')
        for col in range(1, (columns + 1)):
            if col == 1:
                for hd in range(0, columns):
                    hdr = input('Enter the headers one after another:  ')#it takes headers and runs on the basis of No. of column
                    header_list.append(hdr)
                else:
                    pass

            a = input('Enter the full Xpath of first parameter: ')	#2 XPath required simultaniously(one-after-another) in order of header given
            b = input('Enter the full Xpath of the second parameter: ')

            a_list = a.split('/')
            b_list = b.split('/')
            print(a_list)
            index_value = 0
            fix = []
            print('success2')
            for i_num in range(len(a_list)):
                print('success3')
                if a_list[i_num] != b_list[i_num]:
                    i = a_list[i_num]

                    print(a_list[i_num])
                    print(b_list[i_num])

                    print(i)
                    index_value = i_num
                    print(index_value)
                    for al in i:
                        if al.isalpha():
                            fix.append(al)
                            join_list = ''.join(fix)
                        else:
                            pass

                        if col == 1:
                            if al.isdigit():
                                no_value = int(al)
                                print(no_value)
                            else:
                                pass
                        else:
                            pass

                    a_list[index_value] = join_list + '[{}]'
                    if col == 1:
                        row_1st = '/'.join(a_list)
                    elif col == 2:
                        row_2nd = '/'.join(a_list)
                    elif col == 3:
                        row_3rd = '/'.join(a_list)
                    elif col == 4:
                        row_4th = '/'.join(a_list)
                    else:
                        row_5th = '/'.join(a_list)
                    break
                else:
                    pass
    else:
        print('Given number of columns exceed the number of default number of columns: ')

    driver = webdriver.Edge()
    driver.get(url)

    file = open(file_name, 'w', newline='\n')
    write = csv.writer(file)
    write.writerow(header_list)

    # time.sleep(10)
    if no_value != 0:
        i = int(no_value)
        while rows > 0:
            v_inc = str(i)
            print(v_inc)
            if row_1st != 0:
                clms1 = driver.find_element(By.XPATH,row_1st.format(v_inc)).text
            if row_2nd != 0:
                clms2 = driver.find_element(By.XPATH,row_2nd.format(v_inc)).text
            if row_3rd != 0:
                clms3 = driver.find_element(By.XPATH,row_3rd.format(v_inc)).text
            if row_4th != 0:
                clms4 = driver.find_element(By.XPATH,row_4th.format(v_inc)).text
            if row_5th != 0:
                clms5 = driver.find_element(By.XPATH,row_5th.format(v_inc)).text

            i = i + 1
            k = 1

            s_list = [clms1, clms2, clms3, clms4, clms5]
            for nz in s_list:
                if nz != 0 and nz not in new_s_list:
                    new_s_list.append(nz)
                else:
                    pass

                if k == 1:
                    if len(new_s_list) != 0:
                        pass
                    else:
                        print('No valid values are given:(')
                else:
                    pass
                k = k + 1

            print(new_s_list)
            write.writerow(new_s_list)

            new_s_list = []

            print(new_s_list)

            rows = rows - 1
    else:
        print("search error")
    file.close()

else:
    print('Invalid file name: ')																					

























											#by_rajarshibiswas/24-7_code
