from tkinter import *
root=Tk()
# displaying the list statement
def display():
    print(list1.get(ACTIVE))
#giving the entries to the list
list1=Listbox(root)
lst_entries=("data1","data2","data3","data4","data5","data6")

for v in lst_entries:
    list1.insert(END,v)

b1=Button(root,text="Get",command=display)
del_index=int(input("Enter index to delete:"))
#creayting a object and calling the function
list1.delete(del_index)
list1.pack()
b1.pack()
