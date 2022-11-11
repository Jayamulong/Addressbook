from tkinter import *

#Initializing tkinter
root = Tk()
#Setting window width and length
root.geometry('400x400')
#Address book's background color
root.config(bg = 'beige')
#Disabling window resizing
root.resizable(0,0)
#Setting window title
root.title('Address Book')

#Adding a list where inputs are placed
contactlist = []
firstName = StringVar()
lastName = StringVar()
Address = StringVar()
Number = StringVar()

#Add frame for organized widget
frame = Frame(root)
frame.pack(side = RIGHT)

#Adding options for user
scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox(frame, yscrollcommand = scroll.set, height=12)
scroll.config (command = select.yview)
scroll.pack(side=RIGHT, fill = Y)
select.pack(side=LEFT,  fill = BOTH, expand = 1)

#Returning selected value
def Selected():
    return int(select.curselection()[0])

#Adding new contact in the list
def AddContact():
    contactlist.append([firstName.get(),lastName.get(), Address.get(), Number.get()])
    Select_set()

#Editing existing contact in the list
def EDIT():
    contactlist[Selected()] = [firstName.get(), lastName.get(), Address.get(), Number.get()]
    Select_set()

#Deleting selected contact in the list
def DELETE():
    del contactlist[Selected()]
    Select_set()

#Viewing selected contact in the list
def SEARCH():
    FIRSTNAME, LASTNAME, ADDRESS, PHONE = contactlist[Selected()]
    firstName.set(FIRSTNAME)
    lastName.set(LASTNAME)
    Address.set(ADDRESS)
    Number.set(PHONE)

#Destroying mainloop
def EXIT():
    root.destroy()

#Setting the firstname, lastname, address and number field to empty string
def RESET():
    firstName.set('')
    lastName.set('')
    Address.set('')
    Number.set('')

#Sorting and managing the contact list
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for firstName, lastName, address, phone in contactlist :
        select.insert (END, firstName)
Select_set()

#Displaying text title and creating an input text field
Label(root, text = 'FIRST NAME :', font='tnr 10 bold', bg = 'beige').place(x= 30, y=10)
Entry(root, textvariable = firstName).place(x= 125, y = 10)
Label(root, text = 'LAST NAME :', font='tnr 10 bold', bg = 'beige').place(x= 30, y=35)
Entry(root, textvariable = lastName).place(x= 125, y = 35)
Label(root, text = 'ADDRESS :', font='tnr 10 bold', bg = 'beige').place(x = 30, y = 60)
Entry(root, textvariable = Address).place(x = 125, y = 60)
Label(root, text = 'PHONE NO. :', font='tnr 10 bold',bg = 'beige').place(x= 30, y=85)
Entry(root, textvariable = Number).place(x = 125, y = 85)

#Adding buttons to access the widget's
Button(root,text="ADD", font='arial 11 bold', bg ='white', command = AddContact).place(x = 50, y = 120)
Button(root,text="EDIT", font='arial 11 bold', bg ='white', command = EDIT).place(x = 50, y = 170)
Button(root,text="DELETE", font='arial 11 bold', bg ='white', command = DELETE).place(x = 50, y = 220)
Button(root,text="SEARCH", font='arial 11 bold', bg ='white', command = SEARCH).place(x = 50, y = 270)
Button(root,text="EXIT", font='arial 11 bold', bg ='Indianred', command = EXIT).place(x = 300, y = 320)
Button(root,text="RESET", font='arial 11 bold', bg ='white', command = RESET).place(x = 50, y = 320)
root.mainloop()