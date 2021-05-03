# -*- coding: utf-8 -*-
"""
Created on Friday 23-10-2020 17:34:02

@author: Nishanth T (Junior Python Developer)

"""

import tkinter as tk  # main module which deals with whole application.
from tkinter import messagebox as mb
import re
import datetime
import sqlite3

############################## Database Connection #######################################    
def Create_Contact_GUI():
    global r
    def Create_connection():
        global r
        global First_Name,Last_Name,Email_id,Phone_number
        #print(First_Name,Last_Name,Email_id,Phone_number)
        try:        
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Contacts(name_id INTEGER PRIMARY KEY,Date_Time text NOT NULL,First_Name text NOT NULL, Last_Name text NOT NULL, Email_id text NOT NULL, Phone_Number INTEGER NOT NULL)''')  
            now = datetime.datetime.now()
            date_time = now.strftime("%d-%m-%Y-%H:%M:%S")
            c.execute("INSERT INTO Contacts VALUES(null,?, ?, ?, ?,? )",(date_time,First_Name,Last_Name,Email_id,Phone_number))
            conn.commit()
            c.close()
            conn.close()
        except Exception as e:
            mb.showinfo("error",'Databse is not storing data'+str(e),parent=r)
            print(e)
    def Databseexist(First_Name):
        Flag=[]
        try:        
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Contacts(name_id INTEGER PRIMARY KEY,Date_Time text NOT NULL,First_Name text NOT NULL, Last_Name text NOT NULL, Email_id text NOT NULL, Phone_Number INTEGER NOT NULL)''')    
            c.execute('SELECT * FROM Contacts WHERE First_Name=?',(First_Name,))
            S=c.fetchone()
            if type(S) == type(None):
                Flag=0
                pass
            else:
               mb.showinfo("Error","Name you entered is already exists,Please enter any other name",parent=r)
               Flag=1
        except Exception as e:
            print(e)
        return Flag
    ############################ Create Contact Window ############################
    def FN(First_Name): 
        global r
        if First_Name.isalpha(): 
            if len(First_Name)>1:
                Z=Databseexist(First_Name)
                if Z==0:
                    e1.bind('<Return>',gotoLN())                
                elif Z==1:
                    e1.delete(0,tk.END)
                    e1.bind('<Return>',gotoFN())
            else:
                e1.delete(0,tk.END)
                mb.showinfo("error","First Name should be greater than 1",parent=r) 
                e1.bind('<Return>',gotoFN())
                return False
        elif First_Name.isdigit(): 
            e1.delete(0,tk.END)
            mb.showinfo("error","should not be number",parent=r) 
            e1.bind('<Return>',gotoFN())
            return False   
        elif First_Name==" ":
            return False
            
        return First_Name.isalpha()
    
    def databasecheck(First_Name):
        Z=Databseexist()
        if Z==0:
             e1.bind('<Return>',gotoLN())
        elif Z==1:
             e1.bind('<Return>',gotoFN())
             
            
        
             
    def LN(Last_Name):
        global r
        if Last_Name.isalpha(): 
            e2.bind('<Return>',gotoEM())
            return True
            
        elif Last_Name.isdigit():  
            e2.delete(0,tk.END)
            mb.showinfo("error","should not be number",parent=r) 
            e2.bind('<Return>',gotoLN())
            return False
           
        return Last_Name.isalpha()
    
    def EM(Email_id): 
        global r
        regex ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.match(regex,Email_id):
            e3.bind('<Return>',gotoPN())
            return  True
        elif Email_id=="":
            e3.bind('<Return>',gotoPN())
            return  True
        else:
            e3.delete(0,tk.END)       
            mb.showinfo("error","Invalid Email",parent=r) 
            e3.bind('<Return>',gotoEM()) 
            return False
               
        return re.match(regex,Email_id)
              
    
    def PN(Phone_number): 
        global r
        if Phone_number.isdigit():
            return True                       
        
        elif Phone_number.isalpha():
            mb.showinfo("error","Not valid",parent=r)  
            e4.delete(0,tk.END)
            e4.bind('<Return>',gotoPN())
            return False   
        else:
            Phone_number==""
            return True
            
        return Phone_number
      
    
    def gotoFN():
        e1.focus_set()
    
    def gotoLN():
        e2.focus_set()
    
    def gotoEM():
        e3.focus_set()
         
           
    def gotoPN():
        e4.focus_set()
        
        
    def submit():    
        global r
        global First_Name,Last_Name,Email_id,Phone_number
        store={}
        First_Name=e1.get()
        if First_Name=="":
            mb.showinfo("error",'Please enter the first name ',parent=r)
            e1.bind('<Return>',gotoFN())      
            
        Last_Name=e2.get() 
        if Last_Name=="":
            mb.showinfo("error",'Please enter the Last name ',parent=r)
            
        Email_id=e3.get() 
        if  Email_id=="":
            mb.showinfo("error",'Please enter the Email id ',parent=r)
        
        Phone_number=e4.get()
        if Phone_number=="":
            mb.showinfo("error",'Please enter the Phone number',parent=r)
        elif not Phone_number.isdigit():
            mb.showinfo("error",'Letters is not allowed',parent=r)
            e4.delete(0,tk.END)
        store={}
        if len(First_Name)>1:
                if len(Last_Name)>0:
                    if len(Email_id)>1:
                        if Phone_number.isdigit():
                            mb.showinfo("success","Contact"+" "+First_Name+" "+Last_Name+" Saved Successfully",parent=r)
                            store={'First Name':First_Name,'Last Name':Last_Name,'Eamil Id':Email_id,'Phone Number':Phone_number}
                            # Create a Database Connection.
                            Create_connection()
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e4.bind('<Return>',gotoFN())
                
                return First_Name,Last_Name,Email_id,Phone_number  
     
    global r
                                
    r = tk.Tk(screenName=None,  baseName=None,  className='',  useTk=1)
    r.lift()
    r.attributes('-topmost',True)
    r.geometry("600x550+400+90")
    r.configure(bg='steelblue1')
    r.resizable(0, 0) 
    r.title('New Contact')
    r.iconbitmap( r'D:\Nishu_works\Last_Year_projects\Contact_GUI\contact_icon.ico') 
    tk.Label(r, text="Create Contact",bg='steelblue1',fg='midnight blue',font=("Helvetica", 16,"bold"),width=30,height=1,anchor='center').pack()
    
    firstname=tk.StringVar() 
    lastname=tk.StringVar() 
    email_id=tk.StringVar() 
    phonenum=tk.StringVar() 
     
    validation1 = r.register(FN)   
    validation2= r.register(LN) 
    validation3= r.register(EM)  
    validation4= r.register(PN)   
    
    
    tk.Label(r, text="First Name",bg='steelblue1',fg="black",font=("Helvetica", 13,"bold"),width=30,height=2,anchor='center').pack(pady=10)
    e1 = tk.Entry(r,textvariable=firstname,font=('calibre',10,'bold'),validate="focusout",validatecommand=(validation1, '%s'))
    e1.pack()   
    
    tk.Label(r, text="Last Name",bg='steelblue1',fg="black",font=("Helvetica", 13,"bold"),width=30,height=2,anchor='center').pack(pady=10)
    e2 = tk.Entry(r,textvariable=lastname,font=('calibre',10,'bold'),validate="focusout",validatecommand=(validation2, '%s'))
    e2.pack()
    
    tk.Label(r, text="Email ID",bg='steelblue1',fg="black",font=("Helvetica", 13,"bold"),width=30,height=2,anchor='center').pack(pady=10)
    e3=tk.Entry(r,textvariable=email_id,font=('calibre',10,'bold'),validate="focusout",validatecommand=(validation3, '%s'))
    e3.pack()
    
    
    tk.Label(r, text="Phone Number",bg='steelblue1',fg="black",font=("Helvetica", 13,"bold"),width=30,height=2,anchor='center').pack(pady=10)
    e4=tk.Entry(r,textvariable=phonenum,font=('calibre',10,'bold'),validate='key',validatecommand=(validation4,'%P'))
    e4.pack()
    
    bs = tk.Button(r, text ='Save Contact', compound='center',bg='blue',width=15,height=1,command=lambda:submit())
    bs.pack(pady=30)
    
    bmain = tk.Button(r, text ='Main Window', compound='center',bg='orange',fg='white',width=15,height=1,command=lambda:closewindow())
    bmain.pack(pady=10)
    
    def closewindow():
        #global F
        #F=1 
        r.destroy()      
        #return F   
    
    r.mainloop()
    #return F



    
    



















       
      












    

    




