#from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg
import os
import openpyxl
import sqlite3

#import pyshorteners
#Function for onSubmit Button(Submit)

def enter_data():
    accepted = acceptvar.get()
    
    if accepted == 'Terms Accepted':
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_entry.get()
        nationality = nationality_entry.get()
        courses = degree_checkbox.get()
        semester = semester_entry.get()
        currregistered = regiStatusVar.get()
        #termsvar = acceptvar.get()
        #Data saved succesfully will appear in messagebox
        tmsg.showinfo(message="Data saved")
        print("First Name",firstname,'Last Name',lastname)
        print('Title',title,'Age',age,'Nationality',nationality)
        print('Currently Registered',currregistered)
        print('------------------------------------')
        print('Terms and Condition',accepted)
        filepath = "/home/maverick/Desktop/TkinterProjets/Data Entry/data.xlsx"
        
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ['First Name','Last Name','Title','Age','Nationality','Courses','Semester','Registration Status','Terms&Conditions']
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([firstname,lastname,title,age,nationality,courses,semester,currregistered,accepted])
        workbook.save(filepath)
        
        #creating connection for database
        conn = sqlite3.connect('data.db')
        filepath = '/home/maverick/Desktop/TkinterProjets/Data Entry/data.db'
        table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
        (firstname TEXT ,lastname TEXT,title TEXT,age INT,nationality TEXT,courses INT,semester INT,currregistered TEXT,accepted TEXT)'''
        conn.execute(table_create_query)
        
        
        conn.close()
    
    else:
        tmsg.showerror(message='Please accept the terms and condition column')
        
        

window = tk.Tk()
window.geometry('500x500')
window.title('Entry Sheet')
frame = tk.Frame(window)

#frame.pack()
#saving user info 
user_info_frame = tk.LabelFrame(frame,text='User Information')
user_info_frame.grid(row=0,column=0,sticky='news',pady=10)

#creating widgets
first_name_label = tk.Label(user_info_frame,text='First Name')
first_name_entry = tk.Entry(user_info_frame)
last_name_label = tk.Label(user_info_frame,text='Last Name')
last_name_entry = tk.Entry(user_info_frame)
title_label = tk.Label(user_info_frame,text='title')
title_combobox = ttk.Combobox(user_info_frame,values=['','MR.','MRS','MS','Dr'])
age_label = tk.Label(user_info_frame,text='Age')
age_entry = tk.Spinbox(user_info_frame,from_=18 ,to = 110)
nationality_label = tk.Label(user_info_frame,text='Nationality')
nationality_entry = ttk.Combobox(user_info_frame,values=['INDIA','PAKISTAN','CHINA','JAPAN'])
#creating grid
first_name_label.grid(row=0,column=0,padx=2)
first_name_entry.grid(row=0,column=1,padx=2)
last_name_label.grid(row=1,column=0,padx=2)
last_name_entry.grid(row=1,column=1,padx=2)
title_label.grid(row=2,column=0,padx=4)
title_combobox.grid(row=2,column=1,padx=2)
age_label.grid(row=3,column=0,padx=4)
age_entry.grid(row=3,column=1,padx=2)
nationality_label.grid(row=4,column=0,padx=4)
nationality_entry.grid(row=4,column=1,padx=2)

#saving course info
course_frame = tk.LabelFrame(frame,text='Course Information')
course_frame.grid(row=1,column=0,sticky='news',pady=10)


#adding widgets related to course_frame
regiStatusVar = tk.StringVar(value='Not Registered')

registered_check = tk.Checkbutton(course_frame,text='Currently Registered',variable=regiStatusVar,offvalue="Not registered"
                                  ,onvalue='Registered')
numcourses_label = tk.Label(course_frame,text='Completed Courses')
numcourses_spin = tk.Spinbox(course_frame,from_=1,to=100)
degree_label = tk.Label(course_frame,text='Degree')
degree_checkbox = ttk.Combobox(course_frame,values=['','B.E','B.A','B.B.A','B.Com'])
semester_label = tk.Label(course_frame,text='Semester')
semester_entry = ttk.Combobox(course_frame,values=['',1,2,3,4,5,6,7,8])

#adding grid related to course_frame widgets

registered_check.grid(row=1,column=0,padx=10)
 


numcourses_label.grid(row=2,column=0,padx=7)
numcourses_spin.grid(row=2,column=1)
degree_label.grid(row=3,column=0)
degree_checkbox.grid(row=3,column=1,pady=5)
semester_label.grid(row=4,column=0)
semester_entry.grid(row=4,column=1)

# Accept Terms

acceptterms = tk.LabelFrame(frame,text='Terms and Conditions')
acceptterms.grid(row=2,column=0,sticky='news',pady=10)



# Adding widgets for accept terms frame
acceptvar = tk.StringVar(value='Terms Not Accepted')

accept_check = tk.Checkbutton(acceptterms,text='Terms and Condition ',variable=acceptvar,onvalue='Terms Accepted'
                              ,offvalue='Terms Not Accepted')

#terms_checkbox = ttk.Checkbutton(acceptterms,text='Terms and Conditions')
#terms_label = tk.Label(acceptterms,text='')

# Adding grid for accept terms frame widget
accept_check.grid(row=2,column=0,padx=10)
#terms_label.grid(row=2,column=1)

#code for submit button
submit_button = tk.Button(frame,command=enter_data,text='Submit')
submit_button.grid(row=3,column=0)




#code to add padding in every widget we add

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=2,pady=4)

    
frame.pack()
window.mainloop()