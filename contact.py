# Import Module 
from tkinter import *

# Create Object 
root = Tk() 

# Set geometry 
root.title("ContactBook Developed By - Farhan Khan") 
root.geometry('400x500') 
root.resizable()
root.minsize(550,400)  
root.configure(bg = "#90ee90")
# Information List 
datas = [] 

# Add Information 
def add(): 
	global datas 
	datas.append([Name.get(),Number.get()]) 
	update_book() 

# View Information 
def view(): 
	Name.set(datas[int(select.curselection()[0])][0]) 
	Number.set(datas[int(select.curselection()[0])][1]) 
	

# Delete Information 
def delete(): 
	del datas[int(select.curselection()[0])] 
	update_book() 

def reset(): 
	Name.set('') 
	Number.set('') 
	

# Update Information 
def update_book(): 
	select.delete(0,END) 
	for n,p in datas: 
		select.insert(END, n) 

# Add Buttons, Label, ListBox 
Name = StringVar() 
Number = StringVar() 

frame = Frame() 
frame.pack(pady=10) 

frame1 = Frame() 
frame1.pack() 

frame2 = Frame() 
frame2.pack(pady=10) 

Label(frame, text = 'Name', font='arial 12 bold').pack(side=LEFT) 
Entry(frame, textvariable = Name,width=50).pack() 

Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT) 
Entry(frame1, textvariable = Number,width=50).pack() 



Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270) 
Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310) 
Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350) 
Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390) 

scroll_bar = Scrollbar(root, orient=VERTICAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12) 
scroll_bar.config (command=select.yview) 
scroll_bar.pack(side=RIGHT, fill=Y) 
select.place(x=200,y=260) 

# Execute Tkinter 
root.mainloop()



