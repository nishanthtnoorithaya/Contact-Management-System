# -*- coding: utf-8 -*-
"""
Created on Friday 23 17:34:02

@author: Nishanth T (Junior Python Developer)

"""

import tkinter as tk  # main module which deals with whole application.

############################# Integration of Scripts #############################   

from Create_contact_GUI import *
from View_GUI import *
from search_GUI import *

############################## Main Window #######################################
def Create_contact_window():
    Create_Contact_GUI()
      
def Search_contact_window():
    Search_contact_GUI()
       
def view_contact_window():
    View_contact_GUI()


global m
  
m=tk.Tk(screenName=None, baseName=None,  className='',  useTk=1) 
m.geometry("600x550+400+90")
m.configure(bg='grey20')
m.resizable(0, 0) 
m.iconbitmap( r'D:\Nishu_works\Last_Year_projects\Contact_GUI\contact_icon.ico') 
m.title('Contact Book')
tk.Label(m, text="Contact Management System",bg='grey20',fg="gold",font=("Aerial", 18,"bold"),width=30,height=1,anchor='center').pack()  

b1 = tk.Button(m, text ='Create Contact',font=("calibri", 12,"bold"),compound='center',bg='SlateBlue1',width=20,height=2,command=lambda:Create_contact_window())
b1.pack(pady=25)       

b2 = tk.Button(m, text ='Search a Contact',font=("calibri", 12,"bold"), compound='center',bg='orange',width=20,height=2,command=lambda:Search_contact_window())
b2.pack(pady=25)

b3 = tk.Button(m, text ='View Contact', font=("calibri", 12,"bold"),compound='center',bg='yellow',width=20,height=2,command=lambda:view_contact_window())
b3.pack(pady=25)

b4 = tk.Button(m, text ='Close Window', font=("calibri", 12,"bold"),compound='center',bg='springgreen',width=20,height=2,command=lambda:closewindow())
b4.pack(pady=25)

def closewindow():
    m.destroy()

m.mainloop() 