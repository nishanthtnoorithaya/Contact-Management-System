# -*- coding: utf-8 -*-
"""
Created on Friday 23-10-2020 17:34:02

@author: Nishanth T (Junior Python Developer)

"""


import tkinter as tk  # main module which deals with whole application.
from tkinter import messagebox as mb
import sqlite3
from tkinter import ttk

def Search_contact_GUI():
    global s
    def Search_connection():
        global s
        global First_Name
        try:        
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            Name=c.execute('SELECT * FROM Contacts WHERE First_Name=?',(First_Name,))
            S=c.fetchone()
            if type(S) == type(None):
                mb.showinfo("error",'No contact Saved as'+" "+str(Name),parent=s)
            else:
                mb.showinfo("succuess",S,parent=s)
            c.close()
            conn.close()
        except Exception as e:
            print(e)
            
    
    def FN(First_Name): 
        global s
        if First_Name.isalpha(): 
            if len(First_Name)>1: 
                e2.delete(0,tk.END)
                return True
            else:
                e1.delete(0,tk.END)
                mb.showinfo("error","Name should be greater than one character",parent=s) 
                return False
        elif First_Name.isdigit(): 
            e1.delete(0,tk.END)
            mb.showinfo("error","should not be number",parent=s) 
            return False   
        elif First_Name==" ":
            return True
            
        return First_Name.isalpha()
        
        
    def PN(Phone_number): 
        global s
        if Phone_number.isdigit(): 
            e1.delete(0,tk.END)
            return True                       
        
        elif Phone_number.isalpha():
            mb.showinfo("error","Not valid",parent=s)  
            e2.delete(0,tk.END)
            return False      
        else:
            Phone_number==""
            return True
            
        return Phone_number.isdigit()
    
    
    def gotoFN():
            e1.focus_set()
        
    def gotoPN():
        e2.focus_set()
    
    
    def submit():
        global s
        global First_Name
        global Phone_number
        First_Name=e1.get() 
        if First_Name.isdigit():
            e1.delete(0,tk.END)
            mb.showinfo("error",'Please No number is allowed',parent=s)
        Phone_number=e2.get()        
        if len(Phone_number)>1:
            e1.delete(0,tk.END)  
            e2.bind('<Return>',gotoPN()) 
            First_Name=[]
            if not Phone_number.isdigit():
                mb.showinfo("error",'Phone number should not contain Letters',parent=s)
                e2.delete(0,tk.END)
        if len(First_Name)>1:
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            c.execute('SELECT * FROM Contacts WHERE First_Name=?',(First_Name,))
            S=c.fetchone()
            print(S)
            if type(S) == type(None):
                mb.showinfo("error",'No contact Saved as'+" "+str(First_Name),parent=s)
                tree.insert("", 0,values="")
                tree.pack()
            else:        
                tree.insert("", 0,values=S)
                tree.pack()
                
        elif len(Phone_number)>1:
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            c.execute('SELECT * FROM Contacts WHERE Phone_Number=?',(Phone_number,))
            S=c.fetchone()
            print(S)
            if type(S) == type(None):
                mb.showinfo("error",'No contact Saved as'+" "+str(Phone_number),parent=s)
                tree.insert("", 'end',values="")
                tree.pack()
            else:        
                tree.insert("", 'end',values=S)
                tree.pack()
        else:
            mb.showinfo('Error','Please enter the contact to search ',parent=s)
                
    def deleteauponsel():    
        tree.bind('<<TreeviewSelect>>', on_select)
        tree.pack()
        
        
    def on_select(a):
        global Data
        global Name
        curItem = tree.focus()
        print(tree.item(curItem))
        Name=tree.item(curItem)['values'][1]
        Data=tree.item(curItem)['values']
        print(Name)
        print(Data)
        
    def edit_contact():
        from Edit_contact_window import Edit_Contact_GUI
        global s
        try:
            global Data
            print(Data)
            if len(Data[2])>1:
                print(Data)
                Edit_Contact_GUI(Data[2],Data[3],Data[4],Data[5],Data[0])
        except Exception as e:
            mb.showinfo('error','Please select the contact to edit'+str(e),parent=s)
        
    def Refresh():
        global Data
        conn = sqlite3.connect('Contact_Database.db')
        c=conn.cursor()
        c.execute('SELECT * FROM Contacts WHERE name_id=?',(Data[0],))
        S=c.fetchone()
        tree.delete(*tree.get_children())
        if type(S) != type(None):
           tree.insert("", 'end',values=S)
           tree.pack()
           c.close()
           conn.close()
         
        
    def delete():
        global s
        try:
            global First_Name
            global Phone_number
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            if len(First_Name)>1:               
                res=mb.askyesno("Continue?", "Do you wish to delete this Contact?",parent=s)
                if res==True:
                    c.execute("DELETE FROM Contacts WHERE First_Name=?",(First_Name,))
                    selected_item=tree.selection()[0]
                    tree.delete(selected_item)
                    tree.pack()
                    mb.showinfo('Success', 'Contact'+' '+ First_Name +' '+ 'Deleted Succesfully',parent=s)
                    conn.commit()  
                    c.execute('VACUUM')
                    c.close()
                    conn.close()
            elif len(Phone_number)>1:
                res1=mb.askyesno("Continue?", "Do you wish to delete this Contact?",parent=s)
                if res1==True:
                    c.execute("DELETE FROM Contacts WHERE Phone_Number=?",(Phone_number,))
                    selected_item=tree.selection()[0]
                    tree.delete(selected_item)
                    tree.pack()
                    mb.showinfo('Success', 'Contact'+' '+ First_Name +' '+ 'Deleted Succesfully',parent=s)
                    conn.commit()   
                    c.close()
                    conn.close()
        except Exception as e:
            print(e)
            mb.showinfo('Error','PLease select the contact to delete',parent=s)
               
    
            
    s = tk.Tk(screenName=None,  baseName=None,  className='',  useTk=1) 
    s.geometry("600x400+400+90")
    s.resizable(0, 0) 
    s.configure(bg='green yellow')
    s.title('Search Contacts')
    s.iconbitmap( r'D:\Nishu_works\Last_Year_projects\Contact_GUI\contact_icon.ico') 
    tk.Label(s, text="Search Contact",bg='green yellow',fg="DarkOrange4",font=("Helvetica", 16,"bold"),width=30,height=1,anchor='center').pack()    
     
    firstname=tk.StringVar() 
    phonenumber=tk.StringVar() 
    
    validation1 = s.register(FN)   
    validation2= s.register(PN)
       
    
    tk.Label(s, text="Search by First Name",bg='green yellow',fg="black",font=("Helvetica", 13,"bold"),width=30,height=2,anchor='center').pack(pady=10)
    e1 = tk.Entry(s,textvariable=firstname,font=('calibre',10,'bold'),validate="focusout",validatecommand=(validation1, '%s'))
    e1.pack()   
    
    tk.Label(s, text="Search by Phone Number",bg='green yellow',fg="black",font=("Helvetica", 13,"bold"),width=30,height=2,anchor='center').pack(pady=10)
    e2 = tk.Entry(s,textvariable=phonenumber,font=('calibre',10,'bold'),validate="key",validatecommand=(validation2, '%P'))
    e2.pack()
    
    bs = tk.Button(s, text ='Search by Contact', compound='center',bg='blue',width=15,height=1,command=lambda:submit())
    bs.pack(pady=30)   
    tree =ttk.Treeview(s, height=1, columns=("Tags"), show=["headings"])
    tree['columns']=("ID","Date Time","First Name","Last Name","Email ID","Phone Number")   
    T= tk.Frame(s)
    T.pack()
    style = ttk.Style(T)
    style.theme_use("clam") 
    style.configure("Treeview.Heading", font=("aerial", 8,'bold'))
    
    tree.column("#1", width=20,anchor='center')
    tree.column("#2", width=120,anchor='center')
    tree.column("#3", width=100,anchor='center')
    tree.column("#4", width=70,anchor='center')
    tree.column("#5", width=120,anchor='center')
    tree.column("#6", width=100,anchor='center')
    
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Date Time")
    tree.heading("#3", text="First Name")
    tree.heading("#4", text="Last Name")
    tree.heading("#5", text="Email ID")
    tree.heading("#6", text="Phone Number")
    
    deleteauponsel()
    
    bs = tk.Button(s, text ='Delete', compound='center',bg='orange',width=10,height=1,command=lambda:delete())
    bs.pack(padx=30,side='left') 
    
    be = tk.Button(s, text ='Edit', compound='center',bg='orange',width=10,height=1,command=lambda:edit_contact())
    be.pack(padx=30,side='left')
    
    br = tk.Button(s, text ='Refresh', compound='center',bg='blue',width=10,height=1,command=lambda:Refresh())
    br.pack(padx=30,side='left')
    
    bmain = tk.Button(s, text ='Main Window', compound='center',bg='orange',fg='white',width=15,height=1,command=lambda:closewindow())
    bmain.pack(padx=30,side='left')
      
    def closewindow():
        s.destroy()
    
    s.mainloop()
        
  


















############################## Main Window #######################################
#m=tk.Tk(screenName=None,  baseName=None,  className='',  useTk=1) 

#m.geometry("600x550+400+90")
#tk.Label(m, text="Contact Management System",fg="red",font=("Helvetica", 16,"bold"),width=30,height=1,anchor='center').pack()  
    
#b1 = tk.Button(m, text ='Create Contact', compound='center',bg='blue',width=20,height=2)
#b1.pack(pady=50)       

#b2 = tk.Button(m, text ='Search a Contact', compound='center',bg='orange',width=20,height=2,command=lambda:searchwindow())
#b2.pack(pady=50)

#b3 = tk.Button(m, text ='View Contact', compound='center',bg='yellow',width=20,height=2)
#b3.pack(pady=50)

#m.mainloop() 
