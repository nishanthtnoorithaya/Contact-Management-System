# -*- coding: utf-8 -*-
"""
Created on Friday 23 17:34:02

@author: Nishanth T (Junior Python Developer)

"""


import tkinter as tk  # main module which deals with whole application.
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3

def View_contact_GUI():
    global v
    def deleteallcontact():
        conn = sqlite3.connect('Contact_Database.db')
        c=conn.cursor()     
        c.execute('SELECT * FROM Contacts')
        E=c.fetchall()
        if E==[]:
            mb.showinfo('Error',"No Contacts to Delete",parent=v) 
        else:
            res=mb.askyesno("Continue?", "Do you wish to delete All the Contact?",parent=v)
            if res==True:               
                c.execute('DELETE FROM Contacts')
                print(c.fetchall())
                conn.commit()
                mb.showinfo('Success',"All the Contacts are deleted",parent=v)
                c.close()
                conn.close()
                for i in tree.get_children():
                    tree.delete(i)
                tree.pack()
                              
       
    def deleteauponsel():    
        tree.bind('<<TreeviewSelect>>', on_select)
        tree.pack()
    
    
    def delete():
        global v
        try:
            global Name
            global Data
            if len(Name)>1:
                res=mb.askyesno("Continue?", "Do you wish to delete this Contact?",parent=v)
                if res==True:
                    conn = sqlite3.connect('Contact_Database.db')
                    c=conn.cursor()              
                    c.execute("DELETE FROM Contacts WHERE First_Name=?",(Name,))
                    selected_item=tree.selection()[0]
                    tree.delete(selected_item)
                    tree.pack()
                    mb.showinfo('Success', 'Contact'+' '+ Name +' '+ 'Deleted Succesfully',parent=v)
                    conn.commit()   
                    c.close()
                    conn.close()
        except Exception as e:
         mb.showinfo('Error', 'Please select the contact to delete',parent=v) 
            
            
    def on_select(a):
        global Data
        global Name
        curItem = tree.focus()
        print(tree.item(curItem))
        Name=tree.item(curItem)['values'][2]
        Data=tree.item(curItem)['values']
        print(Name)
    
            
    def edit_contact():
        from Edit_contact_window import Edit_Contact_GUI
        global v
        try:
            global Data
            print(Data)
            if len(Data[2])>1:
                print(Data)
                Edit_Contact_GUI(Data[2],Data[3],Data[4],Data[5],Data[0])
        except:
            mb.showinfo('error','Please select the contact to edit',parent=v)
    
       
    def View_connection():
        global v
        global S
        try:       
            tree.delete(*tree.get_children())
            conn = sqlite3.connect('Contact_Database.db')
            c=conn.cursor()
            Name=c.execute('SELECT * FROM Contacts')
            S=c.fetchall()
            if type(S) == type(None):
                tree.insert("", 'end',values="")
                tree.pack()
            else:
                for i in S:
                    tree.insert("",'end',values=i)
                    tree.pack()
        except Exception as e:
            print(e)
        finally:
            c.close()
            conn.close()
    
    
    v = tk.Tk(screenName=None,  baseName=None,  className='',  useTk=1) 
    #v.geometry("700x650+400+90")
    v.geometry("600x650+400+30")
    v.configure(bg='palegreen')
    v.resizable(0, 0) 
    v.title('View Contacts')
    v.iconbitmap( r'D:\Nishu_works\Last_Year_projects\Contact_GUI\contact_icon.ico') 
    tk.Label(v, text="View Contact",bg='palegreen',fg="blue",font=("Helvetica", 16,"bold"),width=30,height=1,anchor='center').pack()      
    T= tk.Frame(v)
    T.pack()
    style = ttk.Style(T)
    style.theme_use("clam")               
    scrollbary = tk.Scrollbar(T,orient='vertical')        
    tree =ttk.Treeview(T, height=25, columns=("Tags"), show=["headings"],yscrollcommand=scrollbary.set)
    style.configure("Treeview.Heading", font=("aerial", 8,'bold'))
    tree['columns']=("ID","Date Time","First Name","Last Name","Email ID","Phone Number")   
    scrollbary.configure(command=tree.yview)
    scrollbary.pack(side='right',fill='y')
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
    
    tree.pack()
    View_connection()
    deleteauponsel()
    
       
    button_del = tk.Button(v, text="Delete",bg='orange',fg='white',width=10,height=1,command=lambda:delete())
    button_del.pack(padx=15,side='left')
    
    deletion = tk.Button(v, text ='Delete All Contacts', compound='right',bg='orange',fg='white',width=14,height=1,command=lambda:deleteallcontact())
    deletion.pack(padx=15,side='left')
    
    be = tk.Button(v, text ='Edit', compound='center',bg='orange',fg='white',width=10,height=1,command=lambda:edit_contact())
    be.pack(padx=15,side='left')
    
    br = tk.Button(v, text ='Refresh', compound='center',bg='blue',fg='white',width=10,height=1,command=lambda:View_connection())
    br.pack(padx=15,side='left')
    
    bmain = tk.Button(v, text ='Main Window', compound='center',bg='orange',fg='white',width=14,height=1,command=lambda:closewindow())
    bmain.pack(padx=15,side='left')
    
    def closewindow():
        v.destroy()
    v.mainloop()
        